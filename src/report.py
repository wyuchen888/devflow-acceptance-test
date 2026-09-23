import csv


def export_csv(rows, path):
    """将报表数据写为 CSV 文件（F1）"""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return path
