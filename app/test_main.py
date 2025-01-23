import pytest
from unittest import mock
from typing import Union

import app.main as main


@pytest.mark.parametrize(
    "return_value, value, expected", [
        (95, 100, "Do nothing"),
        (105, 100, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: object,
        return_value: Union[int, float],
        value: Union[int, float],
        expected: object
) -> None:
    mock_get_exchange_rate_prediction.return_value = return_value
    assert main.cryptocurrency_action(value) == expected
