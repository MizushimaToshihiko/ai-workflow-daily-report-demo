以下の題材について、Antigravityに実装を依頼するための仕様書を作成してください。

題材:
架空の日報CSVを読み込み、顧客コードごとに活動履歴CSVを出力するPythonツール

入力ファイル:
daily_report.csv

入力列:
date, staff, customer_code, customer_name, activity, next_action

サンプルデータの特徴:
・customer_code は 0001 のように先頭ゼロを含むことがある
・customer_code が空欄の行がある
・activity が空欄の行がある
・同じ customer_code の行が複数ある

要件:
・Python標準ライブラリのみで実装する
・pandasなどの外部ライブラリは使わない
・daily_report.csv を読み込む
・customer_code が空欄の行は除外する
・activity が空欄の行は除外する
・customer_code ごとにCSVを分けて output フォルダへ出力する
・出力ファイル名は customer_顧客コード.csv とする
・customer_code は文字列として扱い、先頭ゼロを消さない
・各顧客ごとのデータは date 昇順で出力する
・出力列は date, staff, customer_code, customer_name, activity, next_action とする
・処理件数、出力件数、除外件数をコンソールに表示する
・既存の output フォルダがない場合は作成する

出力してほしい内容:

1. 目的
2. 入力ファイル仕様
3. 出力ファイル仕様
4. 処理手順
5. 除外条件
6. 注意点
7. Antigravityへ渡す実装依頼文
