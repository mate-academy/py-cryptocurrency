import pytest
from app.main import cryptocurrency_action
from unittest.mock import patch


@pytest.mark.parametrize(
    "actual_prediction, exchange_rate, expected_prediction",
    [
        pytest.param(
            1.5,
            1.41,
            "Sell all your cryptocurrency",
            id="should return 'Sell all your cryptocurrency' "
               "if predicted exchange lower then current more then 5 %"
        ),
        pytest.param(
            1.5,
            1.58,
            "Buy more cryptocurrency",
            id="should return 'Buy more cryptocurrency' "
               "if predicted exchange higher then current more then 5 %"
        ),
        pytest.param(
            1.5,
            1.5,
            "Do nothing",
            id="should return 'Do nothing' "
               "if predicted exchange not higher and not lower current"
        ),
        pytest.param(
            2,
            2.1,
            "Do nothing",
            id="should return 'Do nothing' "
               "if predicted exchange is equal 1.05"
        ),
        pytest.param(
            4,
            3.8,
            "Do nothing",
            id="should return 'Do nothing' "
               "if predicted exchange is equal 0.95"
        )
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_should_return_correct_prediction(
        mocked,
        actual_prediction,
        exchange_rate,
        expected_prediction,
):
    mocked.return_value = exchange_rate
    assert cryptocurrency_action(actual_prediction) == expected_prediction
