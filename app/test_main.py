from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=6)
def test_function_for_buy_more_result(
        mock_get_exchange_rate_prediction: int,
) -> None:
    response = cryptocurrency_action(5)
    assert response == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_function_for_do_noting_result(
        mock_get_exchange_rate_prediction: int,
) -> None:
    response = cryptocurrency_action(100)
    assert response == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_function_for_board_105_result(
        mock_get_exchange_rate_prediction: int,
) -> None:
    response = cryptocurrency_action(100)
    assert response == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=94)
def test_function_for_sell_all_result(
        mock_get_exchange_rate_prediction: int,
) -> None:
    response = cryptocurrency_action(100)
    assert response == "Sell all your cryptocurrency"
