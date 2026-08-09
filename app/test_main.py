from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
    mock_get_exchange_rate_prediction: float
) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 106.00
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
    mock_get_exchange_rate_prediction: float
) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 94.00
    assert cryptocurrency_action(current_rate) == \
        "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_one(
    mock_get_exchange_rate_prediction: float
) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 95.00
    assert cryptocurrency_action(current_rate) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_two(
    mock_get_exchange_rate_prediction: float
) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 100.00
    assert cryptocurrency_action(current_rate) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_three(
    mock_get_exchange_rate_prediction: float
) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 105.00
    assert cryptocurrency_action(current_rate) == "Do nothing"
