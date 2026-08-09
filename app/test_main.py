import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        # --- основні сценарії ---
        (100.0, 106.0, "Buy more cryptocurrency"),      # > +5%
        (100.0, 94.0, "Sell all your cryptocurrency"),   # > -5%
        (100.0, 104.9, "Do nothing"),                   # within 5%
        (100.0, 95.1, "Do nothing"),                    # within 5%

        # --- граничні значення ---
        (100.0, 105.0, "Do nothing"),                   # рівно +5%
        (100.0, 95.0, "Do nothing"),                    # рівно -5%
        (100.0, 105.0000002, "Buy more cryptocurrency"),  # трохи > +5%
        (100.0, 94.9999998, "Sell all your cryptocurrency"),  # трохи < -5%

        # --- різні типи ---
        (200, 210.1, "Buy more cryptocurrency"),        # int current
        (200.0, 189.9, "Sell all your cryptocurrency"),  # float current

        # --- дуже великі/малі значення ---
        (1e6, 1.06e6, "Buy more cryptocurrency"),       # велике число
        (1e-6, 1.06e-6, "Buy more cryptocurrency"),     # дуже мале число
        (1e-6, 0.94e-6, "Sell all your cryptocurrency"),  # дуже мале, < -5%

        # --- кейси з одиницею ---
        (1.0, 1.05, "Do nothing"),                      # рівно +5%
        (1.0, 1.050000001, "Buy more cryptocurrency"),  # трохи > +5%
    ],
)
def test_cryptocurrency_action_with_mock(
    current_rate: float,
    predicted_rate: float,
    expected_action: str,
) -> None:
    """
    Test cryptocurrency_action with mocked prediction results.
    Covers boundary, precision, type, and extreme value cases.
    """
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ):
        result: str = cryptocurrency_action(current_rate)
        assert result == expected_action


def test_zero_or_negative_rate() -> None:
    """
    Verify behavior with invalid current_rate values (zero or negative).
    Should raise ValueError since current_rate must be positive.
    """
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=100.0,
    ):
        with pytest.raises(ValueError):
            cryptocurrency_action(0)

        with pytest.raises(ValueError):
            cryptocurrency_action(-10)
