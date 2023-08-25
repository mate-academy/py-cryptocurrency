from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate: mock) -> None:
    mock_get_exchange_rate.side_effect = [95, 100, 105, 94, 106]
    expected_results = [
        "Do nothing",
        "Do nothing",
        "Do nothing",
        "Sell all your cryptocurrency",
        "Buy more cryptocurrency"
    ]
    for result in expected_results:
        assert cryptocurrency_action(100) == result
