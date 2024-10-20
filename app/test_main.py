from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,expected_rate,expected_result",
    [
        (1, 1, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 1.1, "Buy more cryptocurrency"),
        (1, 0.9, "Sell all your cryptocurrency")
    ],
    ids=[
        "current rate 1 and expected rate 1 = Do nothing",
        "current rate 1 and expected rate 0.95 = Do nothing",
        "current rate 1 and expected rate 1.05 = Do nothing",
        "current rate 1 and expected rate 1.1 = Buy more cryptocurrency",
        "current rate 1 and expected rate 0.9 = Sell all your cryptocurrency",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_rate_prediction: mock.MagicMock,
                               current_rate: int | float,
                               expected_rate: int | float,
                               expected_result: str) -> None:
    mocked_rate_prediction.return_value = expected_rate

    assert cryptocurrency_action(current_rate) == expected_result
