# Testcase Report Automation

テストケース実施結果のCSVファイルを分析し、
集計結果をExcel形式で出力する自動化ツールです。

## 📌 概要

本ツールは以下の処理を自動で実行します。

1. テストケース実施状況CSVの分析
2. 分析結果のExcel出力
3. Excelの体裁調整（罫線・色付け・列幅調整など）

---

## 📂 ディレクトリ構成
testcase_report_automation/
│
├── main.py
├── config.py
│
├── data/
│   ├── input/
│   │   └── testcase_result.csv
│   └── output/
│       └── testcase_report.xlsx
│
├── src/
│   ├── csv_analyzer.py
│   ├── excel_exporter.py
│   └── excel_formatter.py
│
├── requirements.txt
└── README.md

## 🛠 必要環境

- Python 3.10 以上
- pip

### 使用ライブラリ

- pandas
- openpyxl

---

## 📦 セットアップ手順

① 仮想環境作成（推奨）
② 仮想環境有効化
bash python -m venv venv
③ 必要ライブラリインストール
bash pip install -r requirements.txt