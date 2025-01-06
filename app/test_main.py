from unittest.mock import patch


from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_if_more_than_5_higher(mock_exchange_rate: int)\
        -> None:
    mock_exchange_rate.return_value = 16

    result = cryptocurrency_action(10)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_if_more_than_5_lower_than_the_current(mock_exchange_rate: int)\
        -> None:
    mock_exchange_rate.return_value = 9

    result = cryptocurrency_action(10)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_if_the_difference_is_small(mock_exchange_rate: float) -> None:
    mock_exchange_rate.return_value = 10.5

    result = cryptocurrency_action(10)
    assert result == "Do nothing"
