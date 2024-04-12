import pytest
from typing import Any
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    ("prediction_rate", "return_quote"),
    [pytest.param(
        1.06, "Buy more cryptocurrency",
        id="should buy crypto when exchange rate goes higher"
    ),
        pytest.param(
            0.94, "Sell all your cryptocurrency",
            id="should sell crypto when exchange rate goes higher"
    ),
        pytest.param(
            1.05, "Do nothing",
            id="should do nothing when prediction rate is 1.05"
    ),
        pytest.param(
            0.95, "Do nothing",
            id="should do nothing when prediction rate is 0.95"
    )
    ])
def test_all_outcomes(
        prediction_rate: Any,
        return_quote: Any) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as exchange:
        exchange.return_value = prediction_rate
        assert cryptocurrency_action(1.00) == return_quote
        exchange.assert_called_once_with(1.00)
