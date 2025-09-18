import pytest

from app.main import cryptocurrency_action, get_exchange_rate_prediction
from unittest.mock import MagicMock, patch


@pytest.mark.parametrize(
    "mock_prediction, current_rate, expected",
    [
        (94, 100, "Sell all your cryptocurrency"),
        (95, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (106, 100, "Buy more cryptocurrency"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_all_the_possible_messages_in_limits(
    mocked_get_prediction: MagicMock,
    mock_prediction: int,
    current_rate: int,
    expected: str
) -> None:
    mocked_get_prediction.return_value = mock_prediction
    actual = cryptocurrency_action(current_rate)
    assert isinstance(actual, str)
    assert actual == expected
    mocked_get_prediction.assert_called_once()


@pytest.mark.parametrize(
    "rate",
    [
        100, 50, 25, 10, 1000, 0
    ]
)
def test_get_exchange_rate_prediction_returns_float(rate: int) -> None:
    prediction = get_exchange_rate_prediction(rate)
    str_prediction = f"{prediction: .2f}"

    assert isinstance(prediction, float)
    assert prediction >= 0
    assert float(str_prediction) == prediction
