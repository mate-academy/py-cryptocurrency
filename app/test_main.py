import pytest
from unittest import mock
from app.main import cryptocurrency_action


def test_function_return_message() -> None:
    assert isinstance(cryptocurrency_action(3), str)
    assert isinstance(cryptocurrency_action(3.5), str)


def test_function_raise_error_while_incorrect_data_entered() -> None:
    with pytest.raises(TypeError):
        cryptocurrency_action("5")


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_function_calls(mocked: mock) -> None:
    mocked.return_value = 5
    cryptocurrency_action(5)
    mocked.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction")
def test_not_to_buy_before_prediction(mocked: mock) -> None:
    mocked.return_value = 5.25
    if mocked.return_value / 5 == 1.05:
        assert cryptocurrency_action(5) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_not_to_sell_before_prediction(mocked: mock) -> None:
    mocked.return_value = 4.75
    if mocked.return_value / 5 == 0.95:
        assert cryptocurrency_action(5) == "Do nothing"
