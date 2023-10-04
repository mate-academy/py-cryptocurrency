from unittest import mock

import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def tester(func: mock) -> None:
    func.return_value = 1
    cryptocurrency_action(2)

    func.assert_called_once()


@pytest.mark.parametrize(
    "value,ans",
    [
        (
            4,
            "Buy more cryptocurrency"
        ),
        (
            1,
            "Do nothing"
        ),
        (
            0.5,
            "Sell all your cryptocurrency"

        ),
        (
            1.05,
            "Do nothing"
        ),
        (
            0.95,
            "Do nothing"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell(func: mock, value: int, ans: str) -> None:
    func.return_value = value
    assert cryptocurrency_action(1) == ans
