import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mock_exchange_prediction() -> callable:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as exchange_prediction):
        yield exchange_prediction


@pytest.mark.parametrize(
    "prediction_rate,current_rate,exp_result",
    [
        (1.06, 1.0, "Buy more cryptocurrency"),
        (1.05, 1.0, "Do nothing"),
        (0.95, 1.0, "Do nothing"),
        (0.94, 1.0, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action_based_on_rate(
        mock_exchange_prediction: callable,
        prediction_rate: float,
        current_rate: float,
        exp_result: str
) -> None:
    mock_exchange_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == exp_result
