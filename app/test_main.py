from app.main import cryptocurrency_action
import pytest
from unittest import mock


@pytest.fixture
def mock_get_exchange_rate_prediction() -> float:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mock_exchange_rate_prediction:
        yield mock_exchange_rate_prediction


@pytest.mark.parametrize("current_rate", [(1.0), (3.14), (2.71)])
def test_dependant_function(current_rate: float,
                            mock_get_exchange_rate_prediction: None
                            ) -> None | AssertionError:
    mock_get_exchange_rate_prediction.return_value = 1.06
    cryptocurrency_action(current_rate)
    mock_get_exchange_rate_prediction.assert_called_once_with(current_rate)


@pytest.mark.parametrize(
    "current_rate,return_get_exchange_rate_prediction,result",
    [
        (1.0, 1.07, "Buy more cryptocurrency"),
        (3.14, 1.45, "Sell all your cryptocurrency"),
        (1000, 960, "Do nothing"),
        (1000, 1050, "Do nothing"),
        (1000, 950, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float,
    return_get_exchange_rate_prediction: float,
    result: str,
    mock_get_exchange_rate_prediction: None,
) -> None | AssertionError:
    mock_get_exchange_rate_prediction. \
        return_value = return_get_exchange_rate_prediction
    assert (
        cryptocurrency_action(current_rate) == result
    ), f"Function should return {result}"
