import pytest
from typing import Union
from unittest import mock


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,expected",
    [
        pytest.param(1,
                     "Do nothing",
                     id="exchange rate is the same"),
        pytest.param(1.05,
                     "Do nothing",
                     id="exchange rate at the upper acceptable limit"),
        pytest.param(0.95,
                     "Do nothing",
                     id="exchange rate at the lower acceptable limit"),
        pytest.param(1.45,
                     "Buy more cryptocurrency",
                     id="exchange rate is more than 5% higher"),
        pytest.param(0.85,
                     "Sell all your cryptocurrency",
                     id="exchange rate is more than 5% lower")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_function(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        prediction_rate: Union[int, float],
        expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(1) == expected


def test_function_exchange_rate_prediction_zero_value() -> None:
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_function_exchange_rate_prediction_called(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1
    cryptocurrency_action(1)
    mock_get_exchange_rate_prediction.assert_called_once_with(1)
