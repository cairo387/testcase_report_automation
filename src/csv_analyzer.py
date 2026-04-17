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
    ng_rate = ng_count / executed_count if executed_count else 0

    # 担当者別集計
    # df.groupby("担当者")["結果"]：dateframeを担当者ごとに分け結果列だけを参照
    # value_counts()：出現回数をカウント
    # unstack(fill_value=0)：視認性が悪いためMultiIndex形式をクロス集計表形式に変換
    person_summary = (
        df.groupby("担当者")["結果"].value_counts().unstack(fill_value=0)
    )
    # 実施件数列を追加（OK + NG）
    person_summary["実施件数"] = (
        person_summary.get("OK", 0) + person_summary.get("NG", 0)
    )
    # 成功率列を追加
    person_summary["成功率"] = (
        person_summary.get("OK", 0) / person_summary["実施件数"]
    ).fillna(0).round(2)
    
    # 実施日別集計
    date_summary = (
        df.groupby("実施日")["結果"].value_counts().unstack(fill_value=0)
    )

    # 日別進捗（実施件数）集計
    daily_progress = df[df["結果"].isin(["OK", "NG"])]

    daily_summary = (
        daily_progress.groupby("実施日")["結果"].count().reset_index()
    )

    daily_summary.columns = ["実施日", "実施件数"]

    # NG件数
    daily_ng = (
        df[df["結果"] == "NG"].groupby("実施日")["結果"].count().reset_index()
    )
    daily_ng.columns = ["実施日", "NG件数"]
    
    # マージ
    daily_summary = daily_summary.merge(
        daily_ng, on="実施日", how="left"
    ).fillna(0)

    daily_summary["NG件数"] = daily_summary["NG件数"].fillna(0).astype(int)

    # NG一覧抽出
    ng_list = df[df["結果"] == "NG"]

    reslut = {
        "サマリー":{
            "総件数": total_count,
            "OK件数": ok_count,
            "NG件数": ng_count,
            "未実施件数": not_executed_count,
            "実施済み件数": executed_count,
            "実施率": round(execution_rate, 2),
            "成功率": round(success_rate, 2),
            "NG率": round(ng_rate, 2),
        },
        "担当者別集計": person_summary,
        "日付別集計": date_summary,
        "日別進捗": daily_summary,
        "NG一覧": ng_list,
    }

    return reslut