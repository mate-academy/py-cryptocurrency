import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,expected_result",
    (
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing")
    )
)
def test_get_exchange_rate_prediction(
    prediction_rate: float,
    expected_result: str
) -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mocked_get_exchange_rate_prediction
    ):
        mocked_get_exchange_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(1.) == expected_result
        mocked_get_exchange_rate_prediction.assert_called_once_with(1.)
