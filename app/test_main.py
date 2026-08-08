import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.fixture()
def mocked_get_exchange_rate() -> callable:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        yield mocked_get_exchange_rate_prediction


@pytest.mark.parametrize("get_exchange_rate, current_num, result",
                         [(50, 67, "Sell all your cryptocurrency"),
                          (100, 70, "Buy more cryptocurrency"),
                          (90.25, 95, "Do nothing"),
                          (105, 100, "Do nothing")])
def test_cryptocurrency_action4(mocked_get_exchange_rate: callable,
                                get_exchange_rate: int,
                                current_num: int,
                                result: str) -> None:
    mock_get_exchange_rate = mocked_get_exchange_rate
    mock_get_exchange_rate.return_value = get_exchange_rate
    current = current_num
    resulto = cryptocurrency_action(current)
    assert resulto == result
