import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,expected_action",
    [
        pytest.param(105, "Do nothing",
                     id="should do nothing when "
                        "prediction is exactly 5 percent higher"),
        pytest.param(95, "Do nothing",
                     id="should do nothing when "
                        "prediction is exactly 5 percent lower"),
        pytest.param(106, "Buy more cryptocurrency",
                     id="should buy when "
                        "prediction more than 5 percent higher"),
        pytest.param(94, "Sell all your cryptocurrency",
                     id="should sell when "
                        "prediction is more than 5 percent lower")

    ]
)
def test_cryptocurrency_action(
        prediction_rate: int,
        expected_action: str
) -> None:
    with mock.patch("app.main."
                    "get_exchange_rate_prediction") as mocked_pred_rate:
        mocked_pred_rate.return_value = prediction_rate
        assert cryptocurrency_action(100) == expected_action
