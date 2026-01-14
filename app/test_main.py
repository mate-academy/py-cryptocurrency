from unittest import mock
from .main import cryptocurrency_action


def test_cryptocurrency_action_higher_5_percentage() -> None:
    with mock.patch("app.main.cryptocurrency_action",
                    return_value="Buy more cryptocurrency"):

        result = cryptocurrency_action(71.51500000)

        assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_higher_5_lower_percentage() -> None:
    with mock.patch("app.main.cryptocurrency_action",
                    return_value="Sell all your cryptocurrency"):

        result = cryptocurrency_action(41.51500000)

        assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_no_difference() -> None:
    with mock.patch("app.main.cryptocurrency_action",
                    return_value="Do nothing"):

        result = cryptocurrency_action(11.51500000)

        assert result == "Do nothing"
