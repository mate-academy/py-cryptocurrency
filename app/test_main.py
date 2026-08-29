import pytest
from pytest_mock import MockerFixture

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (5.55, 5.55 * 1.05, "Do nothing"),
        (5.55, 5.55 * 1.06, "Buy more cryptocurrency"),
        (5.55555, 5.55555 * 0.95, "Do nothing"),
        (5.55555, 5.55555 * 0.94, "Sell all your cryptocurrency"),
        (25, 25.05, "Do nothing"),
        (11, 0, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(mocker: MockerFixture,
                               current_rate: int | float,
                               prediction_rate: int | float,
                               result: str) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction",
                 return_value=prediction_rate)
    assert cryptocurrency_action(current_rate) == result


def test_cryptocurrency_action_zero_division(mocker: MockerFixture) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction", return_value=11)
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)
