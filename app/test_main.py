from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize("exchange_rate, expected_result",
                         [
                             (3.5, "Sell all your cryptocurrency"),
                             (3.8, "Do nothing"),
                             (4, "Do nothing"),
                             (4.2, "Do nothing"),
                             (4.5, "Buy more cryptocurrency"),
                         ]

                         )
@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_expected_action_based_on_exchange_rate_prediction(
        mocked_get_exchange_rate_prediction: MagicMock,
        exchange_rate: int | float,
        expected_result: str,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = exchange_rate

    result = cryptocurrency_action(4)

    mocked_get_exchange_rate_prediction.assert_called_once_with(4)

    assert result == expected_result
