from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def exchange_rate_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mocked_rate_prediction:
        yield mocked_rate_prediction


@pytest.mark.parametrize(
    "exchange_prediction_rate, expected_recommendation",
    [
        (
            pytest.param(
                50,
                "Buy more cryptocurrency"
            )
        ),
        (
            pytest.param(
                42,
                "Do nothing"
            )
        ),
        (
            pytest.param(
                38,
                "Do nothing"
            )
        ),
        (
            pytest.param(
                28,
                "Sell all your cryptocurrency"
            )
        )
    ]
)
def test_cryptocurrency_action(
    exchange_rate_prediction,
    exchange_prediction_rate,
    expected_recommendation
):
    exchange_rate_prediction.return_value = exchange_prediction_rate
    assert cryptocurrency_action(40) == expected_recommendation

