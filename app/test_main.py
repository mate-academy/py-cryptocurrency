import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "actual_prediction, expected_prediction",
    [
        pytest.param(
            1.9,
            "Buy more cryptocurrency",
            id="should return 'Buy more cryptocurrency' "
               "if predicted exchange higher then current more then 5 %"
        ),
        pytest.param(
            2.2,
            "Sell all your cryptocurrency",
            id="should return 'Sell all your cryptocurrency' "
               "if predicted exchange lower then current more then 5 %"
        ),
        pytest.param(
            2,
            "Do nothing",
            id="should return 'Do nothing' "
               "if predicted exchange not higher and not lower current"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction", return_value=2)
def test_should_return_correct_prediction(
        mocked,
        actual_prediction,
        expected_prediction,

):
    assert round(cryptocurrency_action(actual_prediction), 3) == expected_prediction
