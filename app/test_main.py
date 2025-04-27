from unittest import mock
import pytest


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate_prediction_return,current_rate,result",
    [
        pytest.param(95, 100, "Do nothing",
                     id="test_rate_95_percent_do_nothing"),
        pytest.param(105, 100, "Do nothing",
                     id="test_rate_105_percent_do_nothing"),
        pytest.param(95, 105, "Sell all your cryptocurrency",
                     id="test_rate_more_105_percent_"
                        "sell_all_your_cryptocurrency"),
        pytest.param(105, 95, "Buy more cryptocurrency",
                     id="test_rate_less_95_percent_buy_more_cryptocurrency"),
    ])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_rate: object,
                               current_rate: int | float,
                               rate_prediction_return: int | float,
                               result: str) -> None:
    mock_rate.return_value = rate_prediction_return

    assert cryptocurrency_action(current_rate) == result
