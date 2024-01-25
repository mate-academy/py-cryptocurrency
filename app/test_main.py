import pytest


from unittest import mock


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, result",
    [
        (103, "Do nothing"),
        (90, "Sell all your cryptocurrency"),
        (106, "Buy more cryptocurrency"),
        (100, "Do nothing"),
        (94, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
        mock_exchange_rate: mock.MagicMock,
        exchange_rate: int,
        result: str
) -> None:
    mock_exchange_rate.return_value = exchange_rate
    assert cryptocurrency_action(100) == result
