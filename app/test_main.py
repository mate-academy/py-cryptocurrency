import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, expected",
    [
        (110, "Buy more cryptocurrency"),
        (90, "Sell all your cryptocurrency"),
        (103, "Do nothing"),
        (105, "Do nothing"),
        (95, "Do nothing")
    ],
    ids=[
        "buy_more_if_predicted_high",
        "sell_all_if_predicted_low",
        "do_nothing_if_predicted_close",
        "do_nothing_at_105_percent",
        "do_nothing_at_95_percent"
    ]
)
def test_cryptocurrency_action(prediction_rate: int, expected: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = prediction_rate
        assert cryptocurrency_action(100) == expected
