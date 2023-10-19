from app.main import cryptocurrency_action

from unittest import mock


@mock.patch("main.get_exchange_rate_prediction")
def test_function_has_called(mocked_exchange: mock) -> None:
    mocked_exchange.return_value(1.1)
    cryptocurrency_action(100)
    mocked_exchange.assert_called_once_with("Buy more cryptocurrency")
