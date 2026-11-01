from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        # значительно выше, чем +5%
        (100, 120, "Buy more cryptocurrency"),
        # чуть выше границы +5%
        (100, 105.01, "Buy more cryptocurrency"),
        # ровно +5% - не больше, чем 5%
        (100, 105, "Do nothing"),
        # внутри диапазона
        (100, 102, "Do nothing"),
        # курс не изменился
        (100, 100, "Do nothing"),
        (100, 98, "Do nothing"),
        # ровно -5% - не меньше, чем 5%
        (100, 95, "Do nothing"),
        # чуть ниже границы -5%
        (100, 94.99, "Sell all your cryptocurrency"),
        # значительно ниже, чем -5%
        (100, 80, "Sell all your cryptocurrency"),
    ],
    ids=[
        "much higher -> buy",
        "just above +5% -> buy",
        "exactly +5% -> nothing",
        "slightly higher -> nothing",
        "no change -> nothing",
        "slightly lower -> nothing",
        "exactly -5% -> nothing",
        "just below -5% -> sell",
        "much lower -> sell",
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_prediction: mock.MagicMock,
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    mocked_prediction.return_value = predicted_rate

    assert cryptocurrency_action(current_rate) == expected
    mocked_prediction.assert_called_once_with(current_rate)
