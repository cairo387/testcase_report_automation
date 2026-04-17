import pandas as pd

def analyze_testcase(csv_path: str) -> dict:
    """
    テストケースCSVを分析し、集計結果を辞書で返す
    """
    #CSV読み込み
    df = pd.read_csv(csv_path)

    total_count = len(df)

    ok_count = len(df[df["結果"] == "OK"])
    ng_count = len(df[df["結果"] == "NG"])
    not_executed_count = len(df[df["結果"] == "未実施"])

    executed_count = ok_count + ng_count

    execution_rate = executed_count / total_count if total_count else 0
    success_rate = ok_count / executed_count if ok_count else 0

    reslut = {
        "総件数": total_count,
        "OK件数": ok_count,
        "NG件数": ng_count,
        "未実施件数": not_executed_count,
        "実施済み件数": executed_count,
        "実施率": round(execution_rate, 2),
        "成功率": round(success_rate, 2),
    }

    return reslut