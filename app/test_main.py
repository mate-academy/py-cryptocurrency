from unittest import mock
from app.main import cryptocurrency_action


def test_higher_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as prediction:
        prediction.return_value = 15
        result = cryptocurrency_action(10)
        prediction.assert_called_once()
        assert result == "Buy more cryptocurrency"


def test_lower_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as prediction:
        prediction.return_value = 5
        result = cryptocurrency_action(10)
        prediction.assert_called_once()
        assert result == "Sell all your cryptocurrency"


def test_same_as_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as result:
        result.return_value = 10
        function = cryptocurrency_action(10)
        result.assert_called_once()
        assert function == "Do nothing"


def test_border_95_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as result:
        result.return_value = 9.5
        function = cryptocurrency_action(10)
        result.assert_called_once()
        assert function == "Do nothing"


def test_border_105_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as result:
        result.return_value = 10.5
        function = cryptocurrency_action(10)
        result.assert_called_once()
        assert function == "Do nothing"
