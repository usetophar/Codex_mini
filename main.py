"""專案執行入口。"""

from time_utils import get_local_time_text, get_utc_time_text


def main() -> None:
    print("Hello, Codex_mini!")
    print(f"Local time: {get_local_time_text()}")
    print(f"UTC time:   {get_utc_time_text()}")


if __name__ == "__main__":
    main()
