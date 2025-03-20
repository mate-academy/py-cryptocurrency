import pytest
from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_is_calling_get_exchange_rate_prediction(
        get_exchange_rate_prediction: mock.MagicMock) -> None:

    get_exchange_rate_prediction.return_value = 1
    cryptocurrency_action(1)
    get_exchange_rate_prediction.assert_called_once_with(1)


@pytest.mark.parametrize(
    "exchange_rate_prediction,result",
    [
        pytest.param(
            1.06,
            "Buy more cryptocurrency",
            id="tast rate is increasing"
        ),
        pytest.param(
            0.94,
            "Sell all your cryptocurrency",
            id="tast rate is decreasing"
        ),
        pytest.param(
            0.95,
            "Do nothing",
            id="tast rate is not moving enough"
        ),
        pytest.param(
            1.05,
            "Do nothing",
            id="tast rate is not moving enough"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_rate_changes(
        get_exchange_rate_prediction: mock.MagicMock,
        exchange_rate_prediction: float | int,
        result: str) -> None:

    get_exchange_rate_prediction.return_value = exchange_rate_prediction
    assert cryptocurrency_action(1) == result
