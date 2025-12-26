import pytest

from app.main import cryptocurrency_action
from unittest import mock


@pytest.fixture()
def mock_func() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_func:
        yield mock_func


def test_cryptocurrency_action(mock_func: callable) -> None:
    mock_func.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
    mock_func.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
    mock_func.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"
    mock_func.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"
    mock_func.return_value = 0.94
    assert cryptocurrency_action(1) == \
           "Sell all your cryptocurrency"
