import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, prediction_rate, expected_action", [
    (3.1, 5.2, "Buy more cryptocurrency"),
    (5.1, 3.2, "Sell all your cryptocurrency"),
    (5.0, 5.25, "Do nothing"),
    (5.0, 4.75, "Do nothing")
])
def test_cryptocurrency_action(current_rate: float,
                               prediction_rate: float,
                               expected_action: str, mocker: callable) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction",
                 return_value=prediction_rate)
    result = cryptocurrency_action(current_rate)
    assert result == expected_action
