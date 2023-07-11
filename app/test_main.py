from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate,result",
    [
        (1, "Do nothing"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing"),
        (1.23, "Buy more cryptocurrency"),
        (0.89, "Sell all your cryptocurrency")

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_rate_prediction: mock.MagicMock,
        rate: int | float,
        result: str
) -> None:
    mock_rate_prediction.return_value = rate
    assert cryptocurrency_action(1) == result
