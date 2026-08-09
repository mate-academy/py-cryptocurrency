from unittest import mock

from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "predict, expected_result",
    [
        pytest.param(100 * 1.05, "Do nothing"),
        pytest.param(100 * 0.95, "Do nothing"),
        pytest.param(100 * 1.06, "Buy more cryptocurrency"),
        pytest.param(100 * 0.94, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.MagicMock,
        predict: float | int,
        expected_result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = predict
    test_result = cryptocurrency_action(100)
    assert test_result == expected_result
