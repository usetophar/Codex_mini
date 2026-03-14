from datetime import datetime, timezone


def get_local_time_text() -> str:
    """回傳本地時間（ISO 8601 格式）。"""
    return datetime.now().astimezone().isoformat(timespec="seconds")


def get_utc_time_text() -> str:
    """回傳 UTC 時間（ISO 8601 格式）。"""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")