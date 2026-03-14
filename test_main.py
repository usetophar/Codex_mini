from time_utils import get_local_time_text, get_utc_time_text


def test_local_time_has_t_separator() -> None:
    text = get_local_time_text()
    assert "T" in text


def test_utc_time_contains_utc_marker() -> None:
    text = get_utc_time_text()
    assert text.endswith("+00:00")
