from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more_cryptocurrency(
    mocked_get_exchange_rate_prediction: MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 106

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_sell_all_cryptocurrency(
    mocked_get_exchange_rate_prediction: MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 94

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_difference_is_small(
    mocked_get_exchange_rate_prediction: MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 105

    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_difference_is_small_down(
    mocked_get_exchange_rate_prediction: MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 95

    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_prediction_equals_current_rate(
    mocked_get_exchange_rate_prediction: MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 100

    assert cryptocurrency_action(100) == "Do nothing"


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 110, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (50, 53, "Buy more cryptocurrency"),
        (50, 52, "Do nothing"),
        (50, 48, "Do nothing"),
        (50, 47, "Sell all your cryptocurrency"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_returns_expected_result(
    mocked_get_exchange_rate_prediction: MagicMock,
    current_rate: int,
    predicted_rate: int,
    expected: str,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate

    assert cryptocurrency_action(current_rate) == expected
