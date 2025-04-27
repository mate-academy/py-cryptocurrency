from unittest import mock
import pytest


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,rate_prediction_return,result",
    [
        pytest.param(105, 95, "Do nothing",
                     id="test_rate_95_percent_do_nothing"),
        pytest.param(8, 7, "Sell all your cryptocurrency",
                     id="test_rate_105_percent_sell_all_your_cryptocurrency"),
        pytest.param(7.7, 8.2, "Buy more cryptocurrency",
                     id="test_rate_less_95_percent_buy_more_cryptocurrency"),
    ])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_rate: object,
                               current_rate: int | float,
                               rate_prediction_return: int | float,
                               result: str) -> None:
    mock_rate.return_value = rate_prediction_return

    assert cryptocurrency_action(current_rate) == result
