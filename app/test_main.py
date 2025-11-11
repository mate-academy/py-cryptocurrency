import pytest

from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, current, expected",
    [
        (105.4, 100.4, "Do nothing"),
        (105.4, 100.0, "Buy more cryptocurrency"),
        (94.5, 100.5, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_with_float_values(
        mock_get_exchange_rate_prediction: MagicMock,
        prediction: float,
        current: float,
        expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction
    result = cryptocurrency_action(current)
    assert result == expected
    mock_get_exchange_rate_prediction.assert_called_once()


@pytest.mark.parametrize(
    "prediction, current, expected",
    [
        (4546, 2464, "Buy more cryptocurrency"),
        (4000, 4366, "Sell all your cryptocurrency"),
        (95, 100, "Do nothing"),
        (1051, 1000, "Buy more cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_with_integer_values(
        mock_get_exchange_rate_prediction: MagicMock,
        prediction: int,
        current: int,
        expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction
    result = cryptocurrency_action(current)
    assert result == expected
    mock_get_exchange_rate_prediction.assert_called_once()


@pytest.mark.parametrize(
    "prediction, current, expected",
    [
        (1.05, 1.0, "Do nothing"),
        (0.004954, 0.005, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_boundary_values(
        mock_get_exchange_rate_prediction: MagicMock,
        prediction: float,
        current: float,
        expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction
    result = cryptocurrency_action(current)
    assert result == expected
    mock_get_exchange_rate_prediction.assert_called_once()
