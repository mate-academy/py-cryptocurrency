import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_get_exchange_rate_prediction() -> mock.Mock:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_test_get_exchange_rate_prediction):
        yield mock_test_get_exchange_rate_prediction


@pytest.mark.parametrize(
    "prediction,current,message",
    [
        pytest.param(1, 1, "Do nothing",
                     id="Do nothing if both rates are the same"),
        pytest.param(2.1, 2, "Do nothing",
                     id="Do nothing rates coefficient is 1,05"),
        pytest.param(0.475, 0.5, "Do nothing",
                     id="Do nothing rates coefficient is 0,95"),
        pytest.param(1.06, 1, "Buy more cryptocurrency",
                     id="Buy more cryptocurrency "
                        "if rates coefficient higher 1,05"),
        pytest.param(0.94, 1, "Sell all your cryptocurrency",
                     id="Sell cryptocurrency if rates coefficient lower 0,95")
    ]
)
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.Mock,
        prediction: int | float,
        current: int | float,
        message: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction
    assert cryptocurrency_action(current) == message
