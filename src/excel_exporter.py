import pandas as pd

def export_to_excel(result: dict, out_path: str):
    """
    分析結果をExcelファイルに出力する
    """

    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
        # ==========================
        # サマリー出力
        # ==========================
        summary_df = pd.DataFrame(
            list(result["サマリー"].items()),
            columns=["項目", "値"]
        )
        summary_df.to_excel(
            writer,
            sheet_name="サマリー",
            index=False
        )

        # ==========================
        # 担当者別集計
        # ==========================
        result["担当者別集計"].to_excel(
            writer,
            sheet_name="担当者別集計"
        )
        
        # ==========================
        # 日付別集計
        # ==========================
        result["日付別集計"].to_excel(
            writer,
            sheet_name="日付別集計"
        )

        # ==========================
        # 日別集計
        # ==========================
        result["日別進捗"].to_excel(
            writer,
            sheet_name="日別進捗",
            index=False
        )

        # ==========================
        # NG一覧
        # ==========================
        result["NG一覧"].to_excel(
            writer,
            sheet_name="NG一覧",
            index=False
        )

        print(f"Excel出力完了。 出力先：{out_path}")