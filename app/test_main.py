from app.main import cryptocurrency_action
import pytest
from typing import Union
from pytest_mock import MockFixture


@pytest.mark.parametrize(
    "current_rate,prediction,expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 80, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing")
    ],
)
def test_cryptocurrency_action(mocker: MockFixture,
                               current_rate: Union[int, float],
                               prediction: Union[int, float],
                               expected: str) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction",
                 return_value=prediction)
    assert cryptocurrency_action(current_rate) == expected
