from unittest import mock
from app.main import cryptocurrency_action
import pytest


def test_function_has_called() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=1
    ) as mock_rate_prediction:
        cryptocurrency_action(5)
        mock_rate_prediction.assert_called_once()


def test_logic_cryptocurrency() -> None:

    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=1.05
    ):
        assert cryptocurrency_action(1) == "Do nothing"

    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=0.95
    ):
        assert cryptocurrency_action(1) == "Do nothing"

    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=0.95
    ):
        assert cryptocurrency_action(5) == "Sell all your cryptocurrency"

    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=5
    ):
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_type_error_function() -> None:
    with pytest.raises(TypeError):
        cryptocurrency_action("5")
