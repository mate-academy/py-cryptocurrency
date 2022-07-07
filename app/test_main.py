import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        pytest.param(
            5, 10, "Buy more cryptocurrency",
            id="should return 'Buy more cryptocurrency' "
               "if predicted exchange rate is more "
               "than 5% higher from the current"
        ),
        pytest.param(
            10, 5, "Sell all your cryptocurrency",
            id="should return 'Sell all your cryptocurrency' if"
               "predicted exchange rate is more than 5% lower from the current"
        ),
        pytest.param(
            25, 23.8, "Do nothing",
            id="should return 'Do nothing' if"
               "difference less than 5%"
        ),
        pytest.param(
            1, 1.05, "Do nothing",
            id="should return 'Do nothing' if"
               "difference less than 5%"
        ),
        pytest.param(
            1, 0.95, "Do nothing",
            id="should return 'Do nothing' if"
               "difference less than 5%"
        ),

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_correct_advise(mocked_func,
                                      current_rate,
                                      prediction_rate,
                                      expected):
    mocked_func.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
