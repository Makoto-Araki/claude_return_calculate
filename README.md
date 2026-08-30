# claude_return_calculate

2個の正の整数に対して四則演算(加算・減算・乗算・除算)を行う、シンプルなAPIサーバー。

> 本リポジトリは現時点では仕様のみの段階です。実装状況の詳細は [CLAUDE.md](CLAUDE.md) を参照してください。

## API仕様

| 演算 | エンドポイント | リクエストボディ | 成功時レスポンス |
|---|---|---|---|
| 加算 | `POST /calculate/add` | `{"a": 10, "b": 3}` | `{"operation": "add", "a": 10, "b": 3, "result": 13}` |
| 減算 | `POST /calculate/subtract` | `{"a": 10, "b": 3}` | `{"operation": "subtract", "a": 10, "b": 3, "result": 7}` |
| 乗算 | `POST /calculate/multiply` | `{"a": 10, "b": 3}` | `{"operation": "multiply", "a": 10, "b": 3, "result": 30}` |
| 除算 | `POST /calculate/divide` | `{"a": 10, "b": 3}` | `{"operation": "divide", "a": 10, "b": 3, "result": 3.3333333333333335}` |

- `a`, `b` は**正の整数(1以上)のみ**を受け付ける。`0`・負数・小数・非数値・欠落はすべて `422 Unprocessable Entity` を返す。
- 各エンドポイントの詳細な受け入れ基準・設計は [`specs/{add,subtract,multiply,divide}/`](specs/) を参照。

## 技術スタック(計画)

Python 3.12+ / FastAPI / Pydantic v2 / pytest + httpx

## 実行環境: Kubernetes (Docker Desktop)

ローカルPC上のDocker Desktopで有効化したKubernetesクラスタ上で、専用Namespace `calculator-api` 配下に`Deployment`リソースとして動作させる想定。リソース節約を最優先し、以下の最小構成とする。

- Namespace: 専用の `calculator-api`(`default`は使用しない)
- レプリカ数: `1`
- ヘルスチェック(`livenessProbe`/`readinessProbe`): 設定しない
- CPU/メモリの`requests`/`limits`: 最小限(例: cpu `50m`/`100m`、memory `64Mi`/`128Mi`)
- `Service`/`Ingress`はスコープ外(動作確認は `kubectl port-forward` を使用)

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: calculator-api
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: calculator-api
  namespace: calculator-api
  labels:
    app: calculator-api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: calculator-api
  template:
    metadata:
      labels:
        app: calculator-api
    spec:
      containers:
        - name: calculator-api
          image: calculator-api:local
          ports:
            - containerPort: 8000
          resources:
            requests:
              cpu: "50m"
              memory: "64Mi"
            limits:
              cpu: "100m"
              memory: "128Mi"
```

設計判断の詳細・理由は [`specs/deployment/design.md`](specs/deployment/design.md) を参照。

## ドキュメント構成

- [`specs/`](specs/) — 演算ごと・Deploymentの要件定義(`requirements.md`)、設計(`design.md`)、実装タスク(`tasks.md`)
- [`CLAUDE.md`](CLAUDE.md) — Claude Codeなど、実装を担当するAI向けの開発ガイド(ディレクトリ構成・テスト方針など)
