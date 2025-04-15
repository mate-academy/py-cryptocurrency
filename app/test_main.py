from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_95_do_nothing(mock_prediction) -> None:
    mock_prediction.return_value = 14285.71
    assert cryptocurrency_action(15000) == "Do nothing"

@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_105_do_nothing(mock_prediction) -> None:
    mock_prediction.return_value = 190.48
    assert cryptocurrency_action(200) == "Do nothing"
