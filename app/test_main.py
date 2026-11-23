import pytest
from unittest import mock


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_exchange_rate, "
    "future_exchange_rate, "
    "expected_result", [
        pytest.param(70000,
                     100000,
                     "Buy more cryptocurrency",
                     id="Cryptocurrency increase significantly."),
        pytest.param(100000,
                     70000,
                     "Sell all your cryptocurrency",
                     id="Cryptocurrency falls to previous Exchange rate."),
        pytest.param(70000,
                     71000,
                     "Do nothing",
                     id="Cryptocurrency rises a bit."),
        pytest.param(71000,
                     70000,
                     "Do nothing",
                     id="Cryptocurrency falls a bit."),
        pytest.param(70000,
                     70000,
                     "Do nothing",
                     id="Cryptocurrency stay the same."),
        pytest.param(100000,
                     105000,
                     "Do nothing",
                     id="Cryptocurrency rises of 5%."),
        pytest.param(100000,
                     95000,
                     "Do nothing",
                     id="Cryptocurrency falls of 5%."),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_predicted_rate: mock.Mock,
                               future_exchange_rate: int | float,
                               current_exchange_rate: int | float,
                               expected_result: str) -> None:
    mocked_predicted_rate.return_value = future_exchange_rate
    assert cryptocurrency_action(current_exchange_rate) == expected_result
