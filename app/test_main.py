from app.main import get_exchange_rate_prediction, cryptocurrency_action
from unittest import mock
from pytest import mark, param


test_prediction_data = [
    param("increase", 0.3, 33.33, id="increase_03"),
    param("decrease", 0.6, 6, id="decrease_03"),
    param("increase", 0.6, 16.67, id="increase_06"),
    param("decrease", 0.3, 3, id="decrease_06"),
]

test_action_data = [
    param(33.33, "Buy more cryptocurrency", id="good_course"),
    param(3.0, "Sell all your cryptocurrency", id="bad_course"),
    param(9.5, "Do nothing", id="neutral_course_0,95"),
    param(10.5, "Do nothing", id="neutral_course_1,05")
]

@mark.parametrize(
    ("setted_choise,setted_random,expected_res"),
    test_prediction_data
)
@mock.patch("random.random")
@mock.patch("random.choice")
def test_get_exchange_rate_prediction(
        mock_choise: object,
        mock_random: object,
        setted_choise: str,
        setted_random: float,
        expected_res: float,
) -> None:
    mock_choise.return_value = setted_choise
    mock_random.return_value = setted_random
    assert get_exchange_rate_prediction(10) == expected_res


@mark.parametrize(
    ("setted_rate,profeсy"),
    test_action_data
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: object,
        setted_rate: float,
        profeсy: str,
) -> None:
    mocked_prediction.return_value = setted_rate
    assert cryptocurrency_action(10) == profeсy


if __name__ == "__main__":
    pass
