import pytest
from unittest import mock
from .main import cryptocurrency_action


@pytest.mark.parametrize(
    "value,value_multiplier,result",
    [
        (100, 0.9, "Buy more cryptocurrency"),
        (5, 1.0, "Do nothing"),
        (-1, 0.5, "Buy more cryptocurrency")
    ]
)
def test_get_exchange_rate_prediction_increase(
        value: int,
        value_multiplier: float,
        result: float
) -> None:

    with mock.patch("app.main.random.choice", return_value="increase"), \
         mock.patch("app.main.random.random", return_value=value_multiplier):
        assert cryptocurrency_action(value) == result


def test_get_exchange_rate_prediction_zerodivision_error() -> None:
    with pytest.raises(ZeroDivisionError):
        with mock.patch("app.main.random.choice", return_value="increase"), \
                mock.patch("app.main.random.random", return_value=0.0):
            assert cryptocurrency_action(5)


@pytest.mark.parametrize(
    "value,value_multiplier,result",
    [
        (100, 0.9, "Sell all your cryptocurrency"),
        (5, 1.0, "Do nothing"),
        (-1, 0.5, "Sell all your cryptocurrency")
    ]
)
def test_get_exchange_rate_prediction_decrease(
        value: int,
        value_multiplier: float,
        result: float
) -> None:

    with mock.patch("app.main.random.choice", return_value="decrease"), \
         mock.patch("app.main.random.random", return_value=value_multiplier):
        assert cryptocurrency_action(value) == result


def test_cryptocurrency_action_bigger_prediction_rate() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=100):
        assert cryptocurrency_action(20) == "Buy more cryptocurrency"


def test_cryptocurrency_action_lower_prediction_rate() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=1):
        assert cryptocurrency_action(20) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=3.8):
        assert cryptocurrency_action(4) == "Do nothing"
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=4.2):
        assert cryptocurrency_action(4) == "Do nothing"
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=5):
        assert cryptocurrency_action(5) == "Do nothing"
