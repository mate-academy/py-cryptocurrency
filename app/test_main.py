import pytest

from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture
def mocked_prediction_rate() -> mock.MagicMock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked:
        yield mocked


@pytest.mark.parametrize(
    "action, mock_return, result",
    [
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.06, "Buy more cryptocurrency"),
    ]
)
def test_cryptocurrency_action_expected_do_nothing(
        mocked_prediction_rate: mock.MagicMock,
        action: int,
        mock_return: float,
        result: str) -> None:
    mocked_prediction_rate.return_value = mock_return
    assert cryptocurrency_action(action) == result
