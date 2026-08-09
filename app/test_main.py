import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as exchange_rate:
        yield exchange_rate


@pytest.mark.parametrize("current_rate,expected_result", [
    pytest.param(1.06, "Buy more cryptocurrency",
                 id="should return Buy more cryptocurrency"),
    pytest.param(0.94, "Sell all your cryptocurrency",
                 id="should return Sell all your cryptocurrency"),
    pytest.param(1.04, "Do nothing",
                 id="should return Do nothing"),
    pytest.param(1.05, "Do nothing", id="should return Do nothing"),
    pytest.param(0.95, "Do nothing", id="should return Do nothing"),
    pytest.param(0.98, "Do nothing", id="should return Do nothing"),
])
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: callable,
        current_rate: float,
        expected_result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = current_rate
    assert cryptocurrency_action(1) == expected_result
