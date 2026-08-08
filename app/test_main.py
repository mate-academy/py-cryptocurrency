import pytest
from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


current_rate = 1


@pytest.mark.parametrize(
    "exchange_rate_prediction,"
    "expected_result",
    [
        pytest.param(
            1.06,
            "Buy more cryptocurrency",
            id="should return prediction to buy more `Matecoin` "
               "if predicted rate is more than 1.05"
        ),
        pytest.param(
            1.03,
            "Do nothing",
            id="should return prediction to do nothing and wait a bit more "
               "if predicted rate is in range 0.95 to 1.05"
        ),
        pytest.param(
            0.92,
            "Sell all your cryptocurrency",
            id="should return prediction to sell all `Matecoin` "
               "if predicted rate is less than 0.95"
        ),
        pytest.param(
            1.05,
            "Do nothing",
            id="should return prediction to do nothing and wait a bit more "
               "if predicted rate is in range 0.95 to 1.05"
        ),
        pytest.param(
            0.95,
            "Do nothing",
            id="should return prediction to do nothing and wait a bit more "
               "if predicted rate is in range 0.95 to 1.05"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        predicted_rate: MagicMock,
        exchange_rate_prediction: float,
        expected_result: str
) -> None:
    predicted_rate.return_value = exchange_rate_prediction
    assert cryptocurrency_action(current_rate) == expected_result
