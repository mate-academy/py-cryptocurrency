import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,expected_result",
    (
        (12.5, "Buy more cryptocurrency"),
        (0.3, "Sell all your cryptocurrency")
    )
)
def test_cryptocurrency_action(
    current_rate: int,
    expected_result: str
) -> None:
    assert cryptocurrency_action(current_rate) == expected_result


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
    mocked_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 10.0
    cryptocurrency_action(5.5)
    mocked_get_exchange_rate_prediction.assert_called_once_with(5.5)
