from src.csv_analyzer import analyze_testcase
from config import INPUT_CSV_PATH

def main():
    result = analyze_testcase(INPUT_CSV_PATH)

    print("=== テストケース分析結果 ===")
    for key,value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()