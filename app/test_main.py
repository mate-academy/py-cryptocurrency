import pytest
from typing import Union, Any
from unittest import mock


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_conclusion",
    [
        (100, 94, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
        (84, 101, "Buy more cryptocurrency"),
        (94, 100, "Buy more cryptocurrency"),
        (96, 100, "Do nothing"),
        (54, 58, "Buy more cryptocurrency")
    ],
    ids=[
        "predicted rate is lower than current by more than 5%",
        "predicted rate is lower than current by exactly 5%",
        "predicted rate is higher than current by exactly than 5%",
        "current rate is lower than predicted by more than 5%",
        "current rate is lower than predicted by more than 5%",
        "current rate is lower than predicted by less than 5%",
        "current rate is lower than predicted by more than 5%"
    ]
)
def test_should_return_correct_conclusion(mocked_get_exchange: Any,
                                          current_rate: Union[int, float],
                                          predicted_rate: Union[int, float],
                                          expected_conclusion: str) -> None:
    mocked_get_exchange.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_conclusion
