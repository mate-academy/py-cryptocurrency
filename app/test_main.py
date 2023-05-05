import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction():
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        yield mocked_prediction


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected_result",
    [
        pytest.param(
            110,
            100,
            "Buy more cryptocurrency",
            id="Buy more when prediction_rate more than 5 percent higher"
        ),
        pytest.param(
            90,
            100,
            "Sell all your cryptocurrency",
            id="Sell all when prediction_rate more than 5 percent lower"
        ),
        pytest.param(
            95,
            100,
            "Do nothing",
            id="Do nothing when prediction_rate exactly 5 percent lower"
        ),
        pytest.param(
            105,
            100,
            "Do nothing",
            id="Do nothing when prediction_rate exactly 5 percent higher"
        ),
        pytest.param(
            102,
            100,
            "Do nothing",
            id="Do nothing when prediction_rate less than 5 percent higher"
        ),
        pytest.param(
            98,
            100,
            "Do nothing",
            id="Do nothing when prediction_rate less than 5 percent lower"
        ),

    ]
)
def test_cryptocurrency_action(
        prediction_rate,
        current_rate,
        expected_result,
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    initial_rate = current_rate
    result = cryptocurrency_action(initial_rate)
    assert result == expected_result

