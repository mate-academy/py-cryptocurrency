from typing import Generator
from unittest import mock


import pytest


from app.main import cryptocurrency_action


@pytest.fixture
def mock_rate_prediction() -> Generator:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_prediction):
        yield mocked_prediction


@pytest.mark.parametrize("current_rate, coefficient, output", [
    pytest.param(1000, 1.01, "Do nothing"),
    pytest.param(199, 1.049, "Do nothing"),
    pytest.param(100, 1.05, "Do nothing"),
    pytest.param(333, 1.051, "Buy more cryptocurrency"),
    pytest.param(30, 10, "Buy more cryptocurrency"),
    pytest.param(10, 0.951, "Do nothing"),
    pytest.param(450, 0.95, "Do nothing"),
    pytest.param(100, 0.949, "Sell all your cryptocurrency"),
    pytest.param(777, 0.5, "Sell all your cryptocurrency"),
])
def test_cryptocurrency_action(
        current_rate: float | int,
        coefficient: float | int,
        output: str,
        mock_rate_prediction: mock.MagicMock
) -> None:
    mock_rate_prediction.return_value = coefficient * current_rate
    assert cryptocurrency_action(current_rate) == output
    mock_rate_prediction.assert_called_with(current_rate)
