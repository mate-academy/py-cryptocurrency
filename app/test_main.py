# write your code here
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, expected_instruction",
    [
        pytest.param(
            106,
            "Buy more cryptocurrency",
            id="Test if the predicted exchange rate is much more"
        ),
        pytest.param(
            94,
            "Sell all your cryptocurrency",
            id="Test if the predicted exchange rate is much less"
        ),
        pytest.param(
            105,
            "Do nothing",
            id="Test if the predicted exchange rate is not much more"
        ),
        pytest.param(
            95,
            "Do nothing",
            id="Test if the predicted exchange rate is not much less"
        )
    ]
)
def test_cryptocurrency_action(
        monkeypatch: pytest.MonkeyPatch,
        predicted_rate: int,
        expected_instruction: str)\
        -> None:

    def mock_prediction(current_rate: int) -> int:
        return predicted_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction
    )
    assert cryptocurrency_action(100) == expected_instruction
