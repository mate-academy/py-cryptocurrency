from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_rate_prediction() -> callable:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:
        yield mock_prediction


@pytest.mark.parametrize(
    "prediction_value, expected_result",
    [
        pytest.param(0.01, "Sell all your cryptocurrency", id="should sell"),
        pytest.param(0.94, "Sell all your cryptocurrency", id="should sell"),
        pytest.param(0.95, "Do nothing", id="should do nothing"),
        pytest.param(1.05, "Do nothing", id="should do nothing"),
        pytest.param(1.06, "Buy more cryptocurrency", id="should buy"),
        pytest.param(30, "Buy more cryptocurrency", id="should buy")
    ]
)
def test_cryptocurrency_action(mock_rate_prediction: callable,
                               prediction_value: float,
                               expected_result: str) -> None:
    mock_rate_prediction.return_value = prediction_value
    assert cryptocurrency_action(1) == expected_result
