import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture
def mocked_get_exchange_rate_prediction(
        request: any) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_get_exchange_rate_prediction:
        exchange_rate = request.param
        mocked_get_exchange_rate_prediction.return_value = exchange_rate
        yield mocked_get_exchange_rate_prediction


@pytest.mark.parametrize("exchange_rate, expected_action", [
    (95.0, "Sell all your cryptocurrency"),
    (105.0, "Buy more cryptocurrency"),
])
def test_cryptocurrency_action(exchange_rate: int,
                               expected_action: str,
                               mocked_get_exchange_rate_prediction: any
                               ) -> None:

    assert cryptocurrency_action(100) == expected_action
