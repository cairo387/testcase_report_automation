from src.csv_analyzer import analyze_testcase
from config import INPUT_CSV_PATH

def main():
    result = analyze_testcase(INPUT_CSV_PATH)

    print("=== サマリー ===")
    for key,value in result["サマリー"].items():
        print(f"{key}: {value}")

    print("\n=== 担当者別集計 ===")
    print(result["担当者別集計"])

    print("\n=== 日付別集計 ===")
    print(result["日付別集計"])

    print("\n=== 日別進捗 ===")
    print(result["日別進捗"])

    print("\n=== NG一覧 ===")
    print(result["NG一覧"])

if __name__ == "__main__":
    main()