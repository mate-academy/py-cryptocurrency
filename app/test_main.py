from app.main import cryptocurrency_action
from unittest.mock import patch
import pytest
from typing import Union


@pytest.mark.parametrize("current_rate, predicted_rate, expected", [
    (100, 106, "Buy more cryptocurrency"),
    (100, 105.01, "Buy more cryptocurrency"),
    (100, 105, "Do nothing"),
    (100, 104.99, "Do nothing"),
    (100, 95.01, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 94.99, "Sell all your cryptocurrency"),
    (100, 94, "Sell all your cryptocurrency"),
])
def test_cryptocurrency_action(current_rate: Union[int, float],
                               predicted_rate: Union[int, float],
                               expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expected

# from app.main import cryptocurrency_action
# import pytest
# from unittest.mock import patch, MagicMock


# @pytest.fixture
# def mock_prediction_high() -> MagicMock:
#     with (patch("app.main.get_exchange_rate_prediction",
#                 return_value=105)) as mock:
#         yield mock


# @pytest.fixture
# def mock_prediction_low() -> MagicMock:
#     with (patch("app.main.get_exchange_rate_prediction",
#                 return_value=95)) as mock:
#         yield mock


# @pytest.fixture
# def mock_prediction_same() -> MagicMock:
#     with (patch("app.main.get_exchange_rate_prediction",
#                 return_value=100)) as mock:
#         yield mock


# def test_should_buy_more(mock_prediction_high: None) -> None:
#     assert cryptocurrency_action(100) == "Buy more cryptocurrency"


# def test_should_sell_all(mock_prediction_low: None) -> None:
#     assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


# def test_should_do_nothing(mock_prediction_same: None) -> None:
#     assert cryptocurrency_action(100) == "Do nothing"


# @pytest.mark.parametrize("mock_prediction_value", [105, 95])
# def test_should_do_nothing_on_boundary(mock_prediction_value: int) -> None:
#     with (patch("app.main.get_exchange_rate_prediction",
#                 return_value=mock_prediction_value)):
#         assert cryptocurrency_action(100) == "Do nothing"
