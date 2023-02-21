from unittest import mock


import pytest


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction,current,result",
    [
        pytest.param(
            10,
            8,
            "Buy more cryptocurrency",
            id="Buy more cryptocurrency case"
        ),
        pytest.param(
            8,
            10,
            "Sell all your cryptocurrency",
            id="Sell all your cryptocurrency case"
        ),
        pytest.param(
            10,
            10,
            "Do nothing",
            id="Do nothing case"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction: mock,
                               prediction: int | float,
                               current: int | float,
                               result: str) -> None:
    mock_get_exchange_rate_prediction.result_value = prediction
    assert cryptocurrency_action(current) == result
