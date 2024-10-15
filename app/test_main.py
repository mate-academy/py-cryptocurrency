from unittest import mock

import pytest
from app.main import cryptocurrency_action


@pytest.fixture()
def mock_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as m_prediction:
        yield m_prediction


def test_exchange_rate_prediction(mock_prediction: object) -> None:
    mock_prediction.return_value = 1
    cryptocurrency_action(1)
    mock_prediction.assert_called_once_with(1), "Should be called once"


@pytest.mark.parametrize(
    "prediction,result",
    [
        pytest.param(
            2,
            "Buy more cryptocurrency",
            id="should return BUY MORE  if predicted exchange "
               "rate is more than 5% higher from the current"
        ),
        pytest.param(
            0.11,
            "Sell all your cryptocurrency",
            id="should return SELL ALL if predicted exchange "
               "rate is more than 5% lower from the current"
        ),
        pytest.param(
            0.95,
            "Do nothing",
            id="should not sell cryptocurrency when"
               " prediction_rate / current_rate >= 0.95"
        ),
        pytest.param(
            1.05,
            "Do nothing",
            id="should not buy cryptocurrency when"
               " prediction_rate / current_rate <= 1.05"
        )
    ]
)
def test_cryptocurrency_action(
        mock_prediction: object,
        prediction: int | float,
        result: str
) -> None:
    mock_prediction.return_value = prediction
    assert cryptocurrency_action(1) == result


def test_wrong_data_type(mock_prediction: object) -> None:
    mock_prediction.return_value = 1
    with pytest.raises(TypeError):
        cryptocurrency_action([1, 2]), "Should rise TypeError"
