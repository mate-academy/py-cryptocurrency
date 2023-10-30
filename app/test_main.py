from unittest.mock import Mock, patch

import pytest

from app.main import cryptocurrency_action

@pytest.mark.parametrize(
    "mocked, result",
    [
        (3, "Buy more cryptocurrency"),
        (1, "Sell all your cryptocurrency"),
        (2.1, "Do nothing"),
        (1, 9, "Do nothing")

    ]
)
def test_get_currency_action(mocked: Mock, result: str):
    with patch('app.main.get_currency_action', return_value=mocked):
        assert cryptocurrency_action(2) == result
