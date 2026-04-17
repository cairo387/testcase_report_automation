from src.csv_analyzer import analyze_testcase
from config import INPUT_CSV_PATH

def main():
    result = analyze_testcase(INPUT_CSV_PATH)

    print("=== サマリー ===")
    for key,value in result["サマリー"].items():
        print(f"{key}: {value}")

    print("\n=== 担当者別集計 ===")
    print(result["担当者別集計"])

if __name__ == "__main__":
    main()