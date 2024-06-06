from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_result",
    [
        pytest.param(
            100,
            120,
            "Buy more cryptocurrency",
            id="Test predicted rate +20%"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="Test predicted rate +5%"
        ),
        pytest.param(
            100,
            80,
            "Sell all your cryptocurrency",
            id="Test predicted rate -20%"
        ),
        pytest.param(
            100,
            98,
            "Do nothing",
            id="Test predicted rate -2%"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="Test predicted rate -5%"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_rate_prediction: callable,
    current_rate: int | float,
    prediction_rate: int | float,
    expected_result: str
) -> None:
    mocked_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
