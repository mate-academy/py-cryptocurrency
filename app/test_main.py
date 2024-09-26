import pytest

from app.main import cryptocurrency_action

from unittest import mock


@pytest.mark.parametrize(
    "rate,result",
    [

        (0.94, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1, "Do nothing"),
        (1.05, "Do nothing"),
        (1.06, "Buy more cryptocurrency"),

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange: mock.MagicMock,
        rate: int | float,
        result: str
) -> None:
    mock_get_exchange.return_value = rate
    assert cryptocurrency_action(1) == result
