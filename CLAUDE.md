# CLAUDE.md

このファイルは、このリポジトリで作業するClaude Code (claude.ai/code) に向けたガイダンスを提供します。

## プロジェクトの現状

このリポジトリは現時点では**仕様のみ**の状態です。アプリケーションコード、`pyproject.toml`、テストスイートはまだ存在せず、要件・設計の整理段階で作成した `specs/` ディレクトリのみが存在します。実装が始まるまで、ビルド・lint・テストの実行コマンドはありません。

## プロジェクトの目的

2個の**正の整数**パラメータに対して四則演算(加算・減算・乗算・除算)を行うシンプルなAPIサーバー。想定している技術スタック(design.mdに記載済みだが、まだ実装はされていない)は Python 3.12+、FastAPI、バリデーション用のPydantic v2、テスト用のpytest + httpx。

## スペック駆動のワークフロー

各演算は `specs/` 配下にそれぞれ独立したフィーチャーフォルダを持ち、requirements → design → tasks の3ファイル構成に従う。

```
specs/{add,subtract,multiply,divide}/
├── requirements.md   # EARS記法(WHEN/THEN/SHALL)による受け入れ基準
├── design.md         # エンドポイント仕様、Pydanticモデル、処理フロー、エラーハンドリング
└── tasks.md          # 実装チェックリスト。各項目は対応する要件番号を明記
```

機能を実装する際は、リクエスト/レスポンスの形式やエラー挙動の詳細をその機能の `design.md` から確認し、実装が完了した `tasks.md` の項目にはチェックを入れること。各タスクは親の `requirements.md` 内のどの要件を満たすものかが番号で紐づいている。新しい演算・機能を追加する場合も、同様に `specs/<feature>/` に同じ3ファイル構成を作成してこの形式を維持すること。

## 4演算に共通する主要な設計判断

- 全エンドポイントは `POST /calculate/<operation>` で、JSONボディ `{"a": integer, "b": integer}` を受け取り、成功時は `{"operation", "a", "b", "result"}` を返す。
- `a`/`b` は**正の整数(> 0)のみ**を許容する(Pydanticの `PositiveInt` を使用)。`0`・負数・小数・非数値・欠落はすべてFastAPI/Pydantic標準の `422` レスポンスに委ねる。独自のバリデーションを実装しないこと。
- `divide` の `b == 0` も上記の正の整数バリデーションで弾かれるため、ゼロ除算専用の `400` エラーハンドリングは実装しない(`ZeroDivisionError` が発生する経路自体が存在しない)。
- 認証・永続化・CORSはスコープ外。

## 実装時のディレクトリ構成

アプリケーションコードは `app/` ではなく **`apps/`** ディレクトリ配下に実装すること(各 `specs/<operation>/tasks.md` のファイルパスもこれに合わせて記載済み)。`apps/routers/` は `tests/unit/` と同様に**演算ごとにファイルを分割**し、1ファイルに複数演算のハンドラをまとめないこと。

```
apps/
├── main.py            # FastAPIアプリ、各ルーターの登録
├── routers/
│   ├── add.py         # POST /calculate/add
│   ├── subtract.py    # POST /calculate/subtract
│   ├── multiply.py    # POST /calculate/multiply
│   └── divide.py      # POST /calculate/divide
└── schemas.py         # Pydanticモデル(リクエスト/レスポンス)
tests/
└── unit/
    ├── test_add.py
    ├── test_subtract.py
    ├── test_multiply.py
    └── test_divide.py
```

## ユニットテストの方針

各演算の実装には**必ずユニットテストコードを併せて出力する**こと。出力先は `tests/unit/` 配下とし、演算ごとに個別のテストファイル(`test_add.py` など)に分ける。テストケースは各 `specs/<operation>/tasks.md` に列挙された正常系・異常系の項目を網羅すること。
