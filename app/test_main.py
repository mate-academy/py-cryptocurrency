import pytest
from unittest import mock
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected_msg",
    [
        (
            110,
            100,
            "Buy more cryptocurrency"
        ),
        (
            142,
            200,
            "Sell all your cryptocurrency"
        ),
        (
            210,
            200,
            "Do nothing"
        ),
        (
            95,
            100,
            "Do nothing"
        ),
        (
            300,
            300,
            "Do nothing"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: mock,
        prediction_rate: Union[int, float],
        current_rate: Union[int, float],
        expected_msg: str
) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_msg
