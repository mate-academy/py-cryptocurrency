import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize("rate, expected_result", [
    (1.06, "Buy more cryptocurrency"),
    (0.94, "Sell all your cryptocurrency"),
    (1.05, "Do nothing"),
    (0.95, "Do nothing"),
    (any(
        [num for num in range(1000) if num not in [1.06, 0.94]]
    ), "Do nothing"),
])
def test_exchange_rate_prediction(
        rate: float, expected_result: str
) -> None:

    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:

        mock_prediction.return_value = 1 * rate
        result = cryptocurrency_action(1)
        assert result == expected_result
