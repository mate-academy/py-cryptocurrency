import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        current_rate: int,
        prediction_rate: int,
        expected_action: str
) -> None:
    with (
        mock.patch("get_exchange_rate_prediction") as
        mocked_get_exchange_rate_prediction
    ):
        mocked_get_exchange_rate_prediction.return_value = prediction_rate

        assert cryptocurrency_action(current_rate) == expected_action
