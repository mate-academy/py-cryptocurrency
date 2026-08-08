import pytest

from unittest import mock

from app.main import cryptocurrency_action

test_data = [
    (1000, 1200, "Buy more cryptocurrency"),
    (1000, 1060, "Buy more cryptocurrency"),
    (1000, 900, "Sell all your cryptocurrency"),
    (1000, 940, "Sell all your cryptocurrency"),
    (100.0, 105.0, "Do nothing"),
    (1000, 1000, "Do nothing"),
    (100.0, 95.0, "Do nothing")
]

gen_keys = [(f"if current_rate is {current_rate} "
             f"and prediction_rate is {prediction_rate} "
             f"expected is {expected}") for
            current_rate,
            prediction_rate,
            expected in test_data]


@pytest.mark.parametrize("dataset",
                         test_data,
                         ids=gen_keys
                         )
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        dataset: list) -> None:
    (current_rate,
     prediction_rate,
     expected) = dataset
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate)
    mock_get_exchange_rate_prediction.assert_called_once_with(current_rate)
    assert result == expected
