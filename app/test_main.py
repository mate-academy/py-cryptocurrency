from unittest import mock
import pytest

from app.main import get_exchange_rate_prediction
from app.main import cryptocurrency_action


@mock.patch("random.choice", return_value="increase")
@mock.patch("random.random", return_value=0.8)
def test_get_exchange_rate_prediction_when_increase(
        mock_increase: mock,
        mock_random: mock
) -> None:
    expected_result = round(1 / 0.8, 2)
    assert get_exchange_rate_prediction(1) == expected_result


@mock.patch("random.choice", return_value="decrease")
@mock.patch("random.random", return_value=0.8)
def test_get_exchange_rate_prediction_when_decrease(
        mock_increase: mock,
        mock_random: mock
) -> None:
    expected_result = round(2 * 0.8, 2)
    assert get_exchange_rate_prediction(2) == expected_result


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.7)
def test_cryptocurrency_action_buy_more(
        mock_get_exchange_rate_prediction: mock
) -> None:
    expected_result = "Buy more cryptocurrency"
    assert cryptocurrency_action(1) == expected_result


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.8)
def test_cryptocurrency_action_sell_all(
        mock_get_exchange_rate_prediction: mock
) -> None:
    expected_result = "Sell all your cryptocurrency"
    assert cryptocurrency_action(1) == expected_result


@pytest.mark.parametrize(
    "value,expect_result",
    [
        pytest.param(
            0.95, "Do nothing", id="when value is 0.95"
        ),
        pytest.param(
            1.05, "Do nothing", id="when value is 1.05"
        ),
        pytest.param(
            0.99, "Do nothing", id="when value is 0.99"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        mock_get_exchange_rate_prediction: mock,
        value: float,
        expect_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = value
    assert cryptocurrency_action(1) == expect_result
