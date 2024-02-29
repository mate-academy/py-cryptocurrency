import pytest

from app import main
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate,result",
    [
        pytest.param(105, "Do nothing",
                     id="Do nothing if 5% increase"),
        pytest.param(106, "Buy more cryptocurrency",
                     id="Buy more if more than 5% increase"),
        pytest.param(94, "Sell all your cryptocurrency",
                     id="Sell all if more than 5% decrease"),
        pytest.param(95, "Do nothing",
                     id="Do nothing if 5% decrease")
    ]
)
def test_cryptocurrency(monkeypatch: callable,
                        predicted_rate: int,
                        result: str) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda _: predicted_rate)
    assert cryptocurrency_action(100) == result
