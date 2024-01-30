import pytest
from unittest import mock
from typing import Callable

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_prediction:
        yield mock_prediction


def test_crypto_action_should_work_correctly_if_predicted_bigger(
        mocked_prediction: Callable
) -> None:
    mocked_prediction.return_value = 1.06
    result = cryptocurrency_action(1)
    expected = "Buy more cryptocurrency"
    assert result == expected


def test_crypto_action_should_work_correctly_if_predicted_less(
        mocked_prediction: Callable
) -> None:
    mocked_prediction.return_value = 0.94
    result = cryptocurrency_action(1)
    expected = "Sell all your cryptocurrency"
    assert result == expected


def test_crypto_action_work_correctly_if_predicted_equal(
        mocked_prediction: Callable
) -> None:
    mocked_prediction.return_value = 0.1
    result = cryptocurrency_action(0.1)
    expected = "Do nothing"
    assert result == expected


def test_crypto_action_should_work_correctly_if_predicted_bigger_but_close(
        mocked_prediction: Callable
) -> None:
    mocked_prediction.return_value = 1.05
    result = cryptocurrency_action(1)
    expected = "Do nothing"
    assert result == expected

# WATERMARK, DONT STILL MY SOLUTION BIM BIM BAM BAM


def test_crypto_action_should_work_correctly_if_predicted_less_but_close(
        mocked_prediction: Callable
) -> None:
    mocked_prediction.return_value = 0.95
    result = cryptocurrency_action(1)
    expected = "Do nothing"
    assert result == expected


def test_crypto_action_should_raise_error(
        mocked_prediction: Callable
) -> None:
    mocked_prediction.return_value = 0.95
    with pytest.raises(TypeError):
        cryptocurrency_action("1")


def test_crypto_action_work_correctly_if_predicted_very_close_big(
        mocked_prediction: Callable
) -> None:
    mocked_prediction.return_value = 1.051
    result = cryptocurrency_action(1)
    expected = "Buy more cryptocurrency"
    assert result == expected


def test_crypto_action_work_correctly_if_predicted_very_close_les(
        mocked_prediction: Callable
) -> None:
    mocked_prediction.return_value = 0.949
    result = cryptocurrency_action(1)
    expected = "Sell all your cryptocurrency"
    assert result == expected
