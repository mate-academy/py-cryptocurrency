import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,result",
    [
        (1, 1.06, "Buy more cryptocurrency"),  # get 1.06
        (1, 2, "Buy more cryptocurrency"),  # get 2
        (1, 0.94, "Sell all your cryptocurrency"),  # get 0.94
        (2, 1, "Sell all your cryptocurrency"),  # get 0.5
        (1, 1.05, "Do nothing"),  # get 1.05
        (1, 0.95, "Do nothing"),  # get 0.95
        (1, 1, "Do nothing")  # get 1
    ],
    ids=[
        "Buy more test float params and result 1.06",
        "Buy more test int params",
        "Sell all test float params and result 0.94",
        "Sell all test int params",
        "Do nothing test float params and result 1.05",
        "Do nothing test float params and result 0.95",
        "Do nothing test int params"
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        prediction_rate: int | float,
        result: str,
        monkeypatch: pytest.MonkeyPatch
) -> None:
    def mock_get_exchange_rate_prediction(exchange_rate: int | float) -> float:
        return prediction_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )

    assert cryptocurrency_action(current_rate) == result
