from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def current_rate() -> int:
    return 100


@pytest.mark.parametrize(
    "predict, expected",
    [
        (106, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (93, "Sell all your cryptocurrency"),
        (95, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        current_rate: int,
        predict: int,
        expected: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = predict
        result = cryptocurrency_action(current_rate)
        assert result == expected
