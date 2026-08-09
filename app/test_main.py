import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize("prediction_rate, current_rate, result", [
    (1.06, 1, "Buy more cryptocurrency"),
    (0.94, 1, "Sell all your cryptocurrency"),
    (1.05, 1, "Do nothing"),
    (0.95, 1, "Do nothing"),
])
def test_cryptocurrency_action_return(
        prediction_rate: int | float,
        current_rate: int | float,
        result: str
) -> None:

    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange):

        mocked_get_exchange.return_value = prediction_rate

        cryptocurrency_action_res = cryptocurrency_action(current_rate)
        mocked_get_exchange.assert_called_once_with(current_rate)

        assert cryptocurrency_action_res == result
