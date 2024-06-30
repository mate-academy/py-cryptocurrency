from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted, current, expected",
    [
        (5, 2, "Buy more cryptocurrency"),
        (1, 2, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (3.15, 3, "Do nothing"),
    ]
)
def test_cryptocurrency_action_works_ok(predicted: int,
                                        current: int, expected: str) -> None:
    with mock.patch("app.main.get_exchange_ra"
                    "te_prediction", return_value=predicted):
        assert cryptocurrency_action(current) == expected


def test_rate_95_percent_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_r"
                    "ate_prediction", return_value=0.95):
        assert cryptocurrency_action(1) == "Do nothing"


def test_rate_105_percent_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate"
                    "_prediction", return_value=1.05):
        assert cryptocurrency_action(1) == "Do nothing"
