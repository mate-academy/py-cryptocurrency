import pytest
from unittest import mock
from app import main


@pytest.mark.parametrize(
    "current_rate,predicted,expected_result",
    [
        (100, 106, "Buy more cryptocurrency"),
        (200, 188, "Sell all your cryptocurrency"),
        (50, 52.5, "Do nothing"),
        (100, 102, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_action(
        mock_prediction: int | float,
        current_rate: int | float,
        predicted: int | float,
        expected_result: str
) -> None:
    mock_prediction.return_value = predicted
    assert (main.cryptocurrency_action
            (current_rate) == expected_result)

# @mock.patch("app.main.get_exchange_rate_prediction")
# def test_main(mock_exchange_rate: int | float) -> None:
#     mock_exchange_rate.return_value = 106
#
#
# @mock.patch("app.main.cryptocurrency_action")
# def test_buy(mock_currency_action: int | float) -> None:
#     mock_currency_action.return_value = 106 + 6%
#
