import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "prediction_rate, expected",
    [
        pytest.param(1.7, "Buy more cryptocurrency",
                     id="exchange rate is 5% higher from the current"),
        pytest.param(0.93, "Sell all your cryptocurrency",
                     id="exchange rate is 5% lower from the current"),
        pytest.param(1, "Do nothing",
                     id="exchange rate without changing"),
        pytest.param(1.05, "Do nothing",
                     id="exchange higher boundary condition"),
        pytest.param(0.95, "Do nothing",
                     id="exchange lower boundary condition"),
    ]
)
def test_cryptocurrency_action(
        prediction_rate: float,
        expected: str
) -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction") as mocked_get_rate
    ):
        mocked_get_rate.return_value = prediction_rate
        assert cryptocurrency_action(1) == expected
