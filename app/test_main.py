import pytest

from app import main


@pytest.mark.parametrize(
    ("predicted_rate", "expected_action"),
    [
        (106, "Buy more cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
        (105, "Do nothing"),
        (95, "Do nothing"),
        (100, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    monkeypatch, predicted_rate, expected_action
):
    def mock_prediction(current_rate):
        assert current_rate == 100
        return predicted_rate

    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)

    assert main.cryptocurrency_action(100) == expected_action
