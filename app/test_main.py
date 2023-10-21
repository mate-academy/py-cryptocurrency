import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, prediction_rate, expected_action", [
    (4.7, 9.3, "Buy more cryptocurrency"),
    (1.0, 1.3, "Do nothing"),
    (15.0, 7.1, "Sell all your cryptocurrency"),
    (2.0, 2.75, "Do nothing")
])
def test_cryptocurrency_action(current_rate: float,
                               prediction_rate: float,
                               expected_action: str, mocker: None) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction",
                 return_value=prediction_rate)
    result = cryptocurrency_action(current_rate)
    assert result == expected_action
