import pytest
from unittest.mock import MagicMock, patch
from app.main import cryptocurrency_action


@pytest.fixture
def mock_prediction() -> MagicMock:
    with patch("app.main.get_exchange_rate_prediction") as mocked:
        yield mocked


@pytest.mark.parametrize(
    "prediction, expected",
    [
        (106, "Buy more cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
        (103, "Do nothing"),
        (97, "Do nothing"),
        (105, "Do nothing"),
        (95, "Do nothing"),
    ]
)
def test_crypto_actions(
    mock_prediction: MagicMock,
    prediction: int,
    expected: str
) -> None:
    mock_prediction.return_value = prediction
    assert cryptocurrency_action(100) == expected
