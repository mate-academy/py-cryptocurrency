from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate_return,result_action",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1, "Do nothing"),
        (1, 0.94, "Sell all your cryptocurrency"),
    ],
    ids=[
        "test when need to buy crypto",
        "test when do nothing",
        "test when do nothing",
        "test when do nothing",
        "test when need to sell crypto",
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        prediction_rate_return: float,
        result_action: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_prediction_rate):
        mocked_prediction_rate.return_value = prediction_rate_return

        result = cryptocurrency_action(current_rate)

        mocked_prediction_rate.assert_called_once_with(current_rate)
        assert result == result_action
