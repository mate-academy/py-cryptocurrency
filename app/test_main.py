from os import write

from app.main import cryptocurrency_action
import pytest
from unittest.mock import patch


@pytest.mark.parametrize(
    "options, value, course, result",
    [
        ("increase", 20, 0.4, "Buy more cryptocurrency"),
        ("decrease", 20, 0.4, "Sell all your cryptocurrency"),
        ("increase", 100, 1, "Do nothing"),
        ("decrease", 20, 0.95, "Do nothing"),
        ("decrease", 20, 1.05, "Do nothing"),
    ]
)
def test(options, value, course, result) -> None:
    with (patch('random.choice', return_value=options),
          patch('random.random', return_value=course)):
        assert cryptocurrency_action(value) == result
