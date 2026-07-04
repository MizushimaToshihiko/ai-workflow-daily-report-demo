import csv
import os
import sys
from collections import defaultdict

def main():
    input_file = "daily_report.csv"
    output_dir = "output"
    
    # 1. 入力ファイルが存在しない場合のエラー処理
    if not os.path.exists(input_file):
        print(f"{input_file} が見つかりません。")
        sys.exit(1)

    total_rows = 0
    valid_rows_count = 0
    excluded_rows_count = 0
    groups = defaultdict(list)
    
    required_columns = ['date', 'staff', 'customer_code', 'customer_name', 'activity', 'next_action']

    try:
        with open(input_file, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            
            if fieldnames is None:
                print("CSVヘッダーを読み込めませんでした。")
                sys.exit(1)
            
            # 2. 必須列チェック
            missing_columns = [col for col in required_columns if col not in fieldnames]
            if missing_columns:
                print(f"必須列が不足しています: {', '.join(missing_columns)}")
                sys.exit(1)
            
            for row in reader:
                total_rows += 1
                
                # トリム処理（全角・半角スペースをトリム）
                customer_code = row.get("customer_code", "")
                activity = row.get("activity", "")
                
                customer_code_trimmed = customer_code.strip() if customer_code else ""
                activity_trimmed = activity.strip() if activity else ""
                
                # 3. 除外条件チェック（customer_code または activity が空欄・空白のみ）
                if not customer_code_trimmed or not activity_trimmed:
                    excluded_rows_count += 1
                    continue
                
                valid_rows_count += 1
                
                # トリムした値を格納（ファイル名やデータ整合性を保つため）
                row_to_save = {k: v for k, v in row.items()}
                row_to_save["customer_code"] = customer_code_trimmed
                row_to_save["activity"] = activity_trimmed
                
                groups[customer_code_trimmed].append(row_to_save)
                
    except Exception as e:
        print(f"CSVファイルの読み込み中にエラーが発生しました: {e}")
        sys.exit(1)

    # 4. 各グループ内の行を date 昇順で並べ替え
    for code, rows in groups.items():
        rows.sort(key=lambda x: x.get("date") or "")

    # 5. output フォルダが存在しない場合は作成
    os.makedirs(output_dir, exist_ok=True)

    # 6. 顧客コードごとに CSV ファイルを出力
    created_files_count = 0
    for code, rows in groups.items():
        file_name = f"customer_{code}.csv"
        file_path = os.path.join(output_dir, file_name)
        
        try:
            # 既存ファイルがある場合は上書き（他のファイルは削除しない）
            with open(file_path, "w", encoding="utf-8-sig", newline="") as out_f:
                writer = csv.DictWriter(out_f, fieldnames=required_columns)
                writer.writeheader()
                writer.writerows(rows)
            created_files_count += 1
        except Exception as e:
            print(f"ファイル書き込み中にエラーが発生しました ({file_path}): {e}")
            sys.exit(1)

    # 7. 処理結果のコンソール表示
    print(f"読み込んだ総行数: {total_rows}")
    print(f"出力対象となった行数: {valid_rows_count}")
    print(f"除外された行数: {excluded_rows_count}")
    print(f"作成したCSVファイル数: {created_files_count}")

if __name__ == "__main__":
    main()
