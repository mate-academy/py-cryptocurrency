from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.fixture
def exchange_rate_mocked() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as rate_mock:
        yield rate_mock


@pytest.mark.parametrize(
    "exchange,current,result",
    [
        (106, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),
        (101, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing")
    ],
    ids=[
        "must buy when prognose up to 5%",
        "must cell when prognose low then 5%",
        "must do nothing when prognoze near 5%",
        "must do nothing when prognoze near 5%",
        "must do nothing when prognoze near 5%"
    ]
)
def test_for_each_param(
        exchange: int,
        current: int,
        result: str,
        exchange_rate_mocked: mock
) -> None:
    exchange_rate_mocked.return_value = exchange
    assert cryptocurrency_action(current) == result
