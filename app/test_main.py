from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_when_increase(
        mock_random: type[mock]
) -> None:
    mock_random.return_value = 106

    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_when_decrease(
        mock_random: type[mock]
) -> None:
    mock_random.return_value = 94

    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_when_stable_100(
        mock_random: type[mock]
) -> None:
    mock_random.return_value = 100

    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_when_stable_95(
        mock_random: type[mock]
) -> None:
    mock_random.return_value = 95

    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_when_stable_105(
        mock_random: type[mock]
) -> None:
    mock_random.return_value = 105

    result = cryptocurrency_action(100)
    assert result == "Do nothing"
