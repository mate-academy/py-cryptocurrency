from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.fixture
def mocked_get_prediction() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_test_prediction):
        yield mock_test_prediction


def test_predicted_exchange_gt_5p(mocked_get_prediction: mock) -> None:
    value = 100
    mocked_get_prediction.return_value = (value / 0.94)
    assert cryptocurrency_action(value) == "Buy more cryptocurrency"


def test_predicted_exchange_lt_5p(mocked_get_prediction: mock) -> None:
    value = 100
    mocked_get_prediction.return_value = (value * 0.94)
    assert cryptocurrency_action(value) == "Sell all your cryptocurrency"


def test_predicted_exchange_others_cond(mocked_get_prediction: mock) -> None:
    value = 100
    mocked_get_prediction.return_value = (value / 0.96)
    assert cryptocurrency_action(value) == "Do nothing"

    mocked_get_prediction.return_value = (value * 0.96)
    assert cryptocurrency_action(value) == "Do nothing"


def test_boundary_conditions(mocked_get_prediction: mock) -> None:
    value = 100
    mocked_get_prediction.return_value = 105
    assert cryptocurrency_action(value) == "Do nothing"

    mocked_get_prediction.return_value = 95
    assert cryptocurrency_action(value) == "Do nothing"
