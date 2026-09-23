import csv
import sys


def export_csv(rows, path):
    """将报表数据写为 CSV 文件（F1）"""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return path


def _selftest():
    rows = [["name", "score"], ["alice", 90], ["bob", 85]]
    p = export_csv(rows, "selftest_out.csv")
    with open(p, "r", encoding="utf-8", newline="") as f:
        back = list(csv.reader(f))
    assert back == rows, f"CSV 回读不一致: {back}"
    print(f"selftest ok: {len(back)} rows round-trip")
    return 0


if __name__ == "__main__":
    sys.exit(_selftest())
