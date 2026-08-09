import pytest

from app.main import cryptocurrency_action

from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, mock_prediction_result, expected",
    [
        pytest.param(
            5, 5.5,
            "Buy more cryptocurrency",
            id="more than 5% higher"
        ),
        pytest.param(
            5, 4.5,
            "Sell all your cryptocurrency",
            id="more than 5% lower"
        ),
        pytest.param(
            5, 5.25,
            "Do nothing",
            id="small profit"
        ),
        pytest.param(
            5, 4.75,
            "Do nothing",
            id="small loss"
        ),
    ]
)
def test_cryptocurrency(
        mock_rate: float | int,
        current_rate: float | int,
        mock_prediction_result: float | int,
        expected: str
) -> None:
    mock_rate.return_value = mock_prediction_result
    assert cryptocurrency_action(current_rate) == expected
