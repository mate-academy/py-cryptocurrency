import pytest
from unittest.mock import patch


from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize("current, predicted, result", [
    (100, 106, "Buy more cryptocurrency"),
    (100, 100, "Do nothing"),
    (100, 94, "Sell all your cryptocurrency"),
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing")
])
def test_is_it_worth_buying(
        mock_prd: object,
        current: int | float,
        predicted: int | float,
        result: str
) -> None:
    mock_prd.return_value = predicted
    assert cryptocurrency_action(current) == result
