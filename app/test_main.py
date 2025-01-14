from typing import Any
from unittest import mock, TestCase

import pytest

from app.main import cryptocurrency_action


class TestCryptocurrencyActionDependenciesClass(TestCase):
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_calls_dependencies(
            self,
            mock_get_exchange_rate_prediction: mock.MagicMock
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 3.3
        result = cryptocurrency_action(1.1)
        mock_get_exchange_rate_prediction.assert_called_once()

        self.assertEqual(result, "Buy more cryptocurrency")


class TestCryptocurrencyActionRightDataClass:

    @pytest.mark.parametrize(
        "current_rate, expected_error",
        [
            pytest.param("QWE", TypeError,
                         id="test_cryptocurrency_action_right_data"),
            pytest.param("123123123", TypeError,
                         id="test_cryptocurrency_action_right_data"),
            pytest.param([123], TypeError,
                         id="test_cryptocurrency_action_right_data"),
        ]
    )
    def test_cryptocurrency_action_right_data(
            self,
            current_rate: Any,
            expected_error: TypeError) -> None:
        with pytest.raises(expected_error):
            cryptocurrency_action(current_rate)

    @pytest.mark.parametrize(
        "current_rate, second_rate, expected_error",
        [
            pytest.param(1, 2, TypeError,
                         id="test_cryptocurrency_action_one_number"),
            pytest.param("123123123", 2, TypeError,
                         id="test_cryptocurrency_action_one_number"),
            pytest.param(3, "2", TypeError,
                         id="test_cryptocurrency_action_one_number"),
        ]
    )
    def test_cryptocurrency_action_one_current_rate(
            self,
            current_rate: Any,
            second_rate: Any,
            expected_error: TypeError) -> None:
        with pytest.raises(expected_error):
            cryptocurrency_action(current_rate, second_rate)

    @pytest.mark.parametrize(
        "current_rate, mock_return, expected_result",
        [
            (1.0, 1.1, "Buy more cryptocurrency"),
            (1.0, 0.9, "Sell all your cryptocurrency"),
            (1.0, 1.0, "Do nothing"),
        ],
        ids=[
            "Rate increase above threshold",
            "Rate decrease below threshold",
            "Rate within threshold",
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_right_return(
            self,
            mock_get_exchange_rate_prediction: Any,
            current_rate: int | float,
            mock_return: int | float,
            expected_result: str
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = mock_return
        result = cryptocurrency_action(current_rate)
        assert result == expected_result
