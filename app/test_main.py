import pytest
from unittest import mock

from typing import Union

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked() -> mock.MagicMock:
    with (mock.patch("app.main.get_exchange_rate_prediction", return_value=1)
          as mock_get_exchange_rate_prediction):
        yield mock_get_exchange_rate_prediction


@pytest.mark.parametrize(
    "prediction_rate, current_rate, result",
    [
        (2, 1, "Buy more cryptocurrency"),
        (1, 2, "Sell all your cryptocurrency"),
        (1.5, 1.5, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ]
)
def test_return_expected_values(
        mocked: mock.MagicMock,
        prediction_rate: Union[int, float],
        current_rate: Union[int, float],
        result: str
) -> None:
    mocked.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == result


def test_get_exchange_rate_prediction_called(mocked: mock.MagicMock) -> None:
    cryptocurrency_action(1)

    mocked.assert_called_once_with(1)
