from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_function() -> mock.MagicMock:
    with mock.patch("app.main.get_exchange_rate_prediction") as get_rate:
        yield get_rate


def test_rate_is_bigger_than_1_05(mocked_function: mock.MagicMock) -> None:
    mocked_function.return_value = 2
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_rate_is_1_05(mocked_function: mock.MagicMock) -> None:
    mocked_function.return_value = 2.1
    assert cryptocurrency_action(2) == "Do nothing"


def test_rate_is_less_than_0_95(mocked_function: mock.MagicMock) -> None:
    mocked_function.return_value = 2
    assert cryptocurrency_action(3) == "Sell all your cryptocurrency"


def test_rate_is_0_95(mocked_function: mock.MagicMock) -> None:
    mocked_function.return_value = 1.9
    assert cryptocurrency_action(2) == "Do nothing"


def test_rate_is_1(mocked_function: mock.MagicMock) -> None:
    mocked_function.return_value = 3
    assert cryptocurrency_action(3) == "Do nothing"
