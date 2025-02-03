import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mock_get_exchange_rate_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        yield mock_exchange


@pytest.mark.parametrize(
    "current_rate, mock_exchange, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
        (200, 210, "Do nothing"),
        (200, 189, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(current_rate: int,
                               mock_exchange: int,
                               expected: str,
                               mock_get_exchange_rate_prediction: mock.Mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = mock_exchange
    result = cryptocurrency_action(current_rate)
    assert result == expected
