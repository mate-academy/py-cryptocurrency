from unittest.mock import patch, Mock


from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 110

    result = cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_more_cryptocurrency(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 94

    result = cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_cryptocurrency_95(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 95

    result = cryptocurrency_action(100)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_cryptocurrency_105(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 105

    result = cryptocurrency_action(100)

    assert result == "Do nothing"
