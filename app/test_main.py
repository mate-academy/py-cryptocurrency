from unittest import mock
from app.main import cryptocurrency_action


def test_function_has_been_called() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_prediction):
        mocked_prediction.return_value = 110
        cryptocurrency_action(100)
        mocked_prediction.assert_called_with(100)
