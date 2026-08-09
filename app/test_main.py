import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, expected",
    [
        pytest.param(10.6, "Buy more cryptocurrency", id="> +5%"),
        pytest.param(10.5, "Do nothing", id="= +5%"),
        pytest.param(9.5, "Do nothing", id="= -5%"),
        pytest.param(9.3, "Sell all your cryptocurrency", id="< -5%"),
        pytest.param(10.02, "Do nothing", id="almost same"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: mock.MagicMock,
        predicted_rate: int | float,
        expected: str
) -> None:
    mock_prediction.return_value = predicted_rate
    assert cryptocurrency_action(10) == expected
