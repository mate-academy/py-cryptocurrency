import pytest
from app.main import cryptocurrency_action
from unittest.mock import patch
from typing import Union


@pytest.mark.parametrize("input_current_rate,expected,get_exchange_rate", [
    pytest.param(100, "Buy more cryptocurrency", 110.0,
                 id="Should buy more when rate increases by >5%"),
    pytest.param(100, "Do nothing", 105.0,
                 id="Should do nothing when rate increases exactly by 5%"),
    pytest.param(100, "Do nothing", 95.0,
                 id="Should do nothing when rate decreases exactly by 5%"),
    pytest.param(100, "Sell all your cryptocurrency", 90.0,
                 id="Should sell all when rate decreases by >5%"),
    pytest.param(100, "Do nothing", 102.0,
                 id="Should do nothing when rate changes less than ±5%"),
])
def test_cryptocurrency_action(input_current_rate: Union[int, float],
                               expected: str,
                               get_exchange_rate: Union[int, float]
                               ) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_exchange_rate:
        mock_exchange_rate.return_value = get_exchange_rate
        assert cryptocurrency_action(input_current_rate) == expected
