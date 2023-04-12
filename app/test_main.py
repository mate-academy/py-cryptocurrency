import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mock_exchange_rate() -> int:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_exchange_rate_prediction:
        yield mock_exchange_rate_prediction


@pytest.mark.parametrize(
    "exchange_rate,current_rate,expected_action",
    [
        (10, 2, "Buy more cryptocurrency"),
        (2, 10, "Sell all your cryptocurrency"),
        (9.5, 10, "Do nothing"),
        (10.5, 10, "Do nothing")
    ],
    ids=["result1 must be 'Buy more cryptocurrency'",
         "result2 must be 'Sell all your cryptocurrency'",
         "result3 must be 'Do nothing'",
         "result4 must be 'Do nothing'"])
def test_cryptocurrency_action(mock_exchange_rate: mock.Mock,
                               exchange_rate: float,
                               current_rate: float,
                               expected_action: str) -> None:
    mock_exchange_rate.return_value = exchange_rate
    with mock_exchange_rate:
        assert cryptocurrency_action(current_rate) == expected_action
