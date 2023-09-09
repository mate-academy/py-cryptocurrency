from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_funct_value_if_exchange_rate_higher_current_rate(
    mock_rate: mock.MagicMock
) -> None:
    mock_rate.return_value = 1.051

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_funct_value_if_exchange_rate_lower_current_rate(
    mock_rate: mock.MagicMock
) -> None:
    mock_rate.return_value = 0.949

    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_funct_value_if_difference_not_much(
    mock_rate: mock.MagicMock
) -> None:
    mock_rate.return_value = 1

    assert cryptocurrency_action(1) == "Do nothing"
