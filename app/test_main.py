import pytest
from unittest import mock
from app.main import cryptocurrency_action


# def test_buy_more_when_predicted_more_than_5_percent():
#     current = 100
#     predicted = 106  # > 5% вище
#     with patch('app.main.get_exchange_rate_prediction',
#     return_value=predicted):
#         result = cryptocurrency_action(current)
#         assert result == "Buy more cryptocurrency"
#
# def test_sell_all_when_predicted_more_than_5_percent_lower():
#     current = 100
#     predicted = 94  # >5% нижче
#     with patch('app.main.get_exchange_rate_prediction',
#     return_value=predicted):
#         result = cryptocurrency_action(current)
#         assert result == "Sell all your cryptocurrency"
#
# def test_do_nothing_within_5_percent_range():
#     current = 100
#     for predicted in (95, 100, 105):
#         with patch('app.main.get_exchange_rate_prediction',
#         return_value=predicted):
#             result = cryptocurrency_action(current)
#             assert result == "Do nothing"


@pytest.mark.parametrize(
    "current, predicted, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
    ]
)
def test_can_access_google_page(current: int,
                                predicted: int,
                                expected: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_predict:
        mocked_predict.return_value = predicted
        assert cryptocurrency_action(current) == expected
