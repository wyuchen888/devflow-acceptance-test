import argparse
import sys

VALID_FORMATS = ("csv", "json")


def main(argv=None):
    parser = argparse.ArgumentParser(prog="app")
    parser.add_argument("--format", choices=VALID_FORMATS, default="csv",
                        help="输出格式（F2）")
    args = parser.parse_args(argv)
    if args.format not in VALID_FORMATS:
        print(f"错误：不支持的格式 {args.format}")
        return 2
    print(f"app runs with format={args.format}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
