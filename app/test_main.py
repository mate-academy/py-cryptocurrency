from unittest import mock

from app.main import cryptocurrency_action

import pytest


@pytest.fixture()
def mock_ex_rate_prediction() -> None:
    patcher = mock.patch("app.main.get_exchange_rate_prediction")
    mocked = patcher.start()
    yield mocked
    patcher.stop()


def test_cryptocurrency_action_with_uppper_limit_prediction(
        mock_ex_rate_prediction: None) -> None:
    current_rate = 1
    mock_ex_rate_prediction.return_value = 1.05 * current_rate
    assert cryptocurrency_action(current_rate) == "Do nothing"
    mock_ex_rate_prediction.assert_called_once()


def test_cryptocurrency_action_with_lower_limit_prediction(
        mock_ex_rate_prediction: None) -> None:
    current_rate = 1
    mock_ex_rate_prediction.return_value = 0.95 * current_rate
    assert cryptocurrency_action(current_rate) == "Do nothing"
    mock_ex_rate_prediction.assert_called_once()


def test_cryptocurrency_action_with_low_prediction(
        mock_ex_rate_prediction: None) -> None:
    current_rate = 1
    mock_ex_rate_prediction.return_value = 0.94 * current_rate
    assert (cryptocurrency_action(current_rate)
            == "Sell all your cryptocurrency")
    mock_ex_rate_prediction.assert_called_once()


def test_cryptocurrency_action_with_high_prediction(
        mock_ex_rate_prediction: None) -> None:
    current_rate = 1
    mock_ex_rate_prediction.return_value = 1.06 * current_rate
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"
    mock_ex_rate_prediction.assert_called_once()


def test_cryptocurrency_action_with_normal_prediction(
        mock_ex_rate_prediction: None) -> None:
    current_rate = 1
    mock_ex_rate_prediction.return_value = 1 * current_rate
    assert cryptocurrency_action(current_rate) == "Do nothing"
    mock_ex_rate_prediction.assert_called_once()
