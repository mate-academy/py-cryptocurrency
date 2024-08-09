import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


# def test_buy_more_coins() -> None:
#     with patch("app.main.get_exchange_rate_prediction") as mock_rate_predict:
#         mock_rate_predict.return_value = 6
#
#         assert cryptocurrency_action(5) == "Buy more cryptocurrency"
#
#
# def test_sell_all_coins() -> None:
#     with patch("app.main.get_exchange_rate_prediction") as mock_rate_predict:
#         mock_rate_predict.return_value = 4
#
#         assert cryptocurrency_action(5) == "Sell all your cryptocurrency"
#
#
# def test_rate_95_do_nothing() -> None:
#     with patch("app.main.get_exchange_rate_prediction") as mock_rate_predict:
#         mock_rate_predict.return_value = 5.25
#
#         assert cryptocurrency_action(5) == "Do nothing"
#
#
# def test_rate_105_do_nothing() -> None:
#     with patch("app.main.get_exchange_rate_prediction") as mock_rate_predict:
#         mock_rate_predict.return_value = 4.75
#
#         assert cryptocurrency_action(5) == "Do nothing"


@pytest.mark.parametrize(
    "mock_func_result,current_rate,expected_value",
    [
        pytest.param(
            6, 5, "Buy more cryptocurrency",
            id="buy more coins"
        ),
        pytest.param(
            4, 5, "Sell all your cryptocurrency",
            id="sell all coins"
        ),
        pytest.param(
            5.25, 5, "Do nothing",
            id="rate 95 do nothing"
        ),
        pytest.param(
            4.75, 5, "Do nothing",
            id="rate 105 do nothing"
        )
    ]
)
def test_cryptocurrency_action(
        mock_func_result: int | float,
        current_rate: int | float,
        expected_value: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_rate_predict:
        mock_rate_predict.return_value = mock_func_result

        assert cryptocurrency_action(current_rate) == expected_value
