from pytest import fixture, mark
from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


@fixture
def mocked_exchange_rate_prediction() -> None:
    with patch("app.main.get_exchange_rate_prediction") as exchange_rate:
        yield exchange_rate


@mark.parametrize(
    "current_rate, rate_prediction, action",
    [
        (100, 120.00, "Buy more cryptocurrency"),
        (100, 60.00, "Sell all your cryptocurrency"),
        (100, 102.00, "Do nothing"),
        (115.04, 250.09, "Buy more cryptocurrency"),
    ],
    ids=[
        "rate increases - buy",
        "rate drops - sell",
        "rate increases by 2% - do nothing",
        "significant rate surge - buy",
    ]
)
def test_cryptocurrency_action(
        mocked_exchange_rate_prediction: MagicMock,
        rate_prediction: int | float,
        current_rate: int | float,
        action: str,
) -> None:
    mocked_exchange_rate_prediction.return_value = rate_prediction

    assert cryptocurrency_action(current_rate) == action
