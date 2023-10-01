import pytest
from unittest import mock
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate_predict,rate,expected_res",
    [
        (2, 1, "Buy more cryptocurrency"),
        (1, 2, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        rate_predict: Union[int, float],
        rate: Union[int, float],
        expected_res: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_predict:
        mocked_predict.return_value = rate_predict
        assert cryptocurrency_action(rate) == expected_res
