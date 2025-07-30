import pytest

from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected_result",
    [
        pytest.param(
            10, 9, "Do nothing", id="should return 'Do nothing'"
        ),
        pytest.param(
            10, 11, "Sell all your cryptocurrency",
            id="should return 'Sell all your cryptocurrency'"
        ),
        pytest.param(
            10, 8, "Buy more cryptocurrency",
            id="should return 'Buy more cryptocurrency'"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate: mock.MagicMock,
        prediction_rate: int,
        current_rate: int,
        expected_result: str
) -> None:
    mocked_exchange_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
