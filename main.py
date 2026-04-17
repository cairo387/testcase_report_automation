from src.csv_analyzer import analyze_testcase
from src.excel_exporter import export_to_excel
from config import INPUT_CSV_PATH, OUTPUT_EXCEL_PATH

def main():
    result = analyze_testcase(INPUT_CSV_PATH)
    
    # Excel出力
    export_to_excel(result, OUTPUT_EXCEL_PATH)

if __name__ == "__main__":
    main()