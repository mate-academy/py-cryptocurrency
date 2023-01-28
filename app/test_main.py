from unittest import mock

# import pytest

from app.main import cryptocurrency_action


# @mock.patch("app.main.get_exchange_rate_prediction")
# def test_should_get_exchange_rate_prediction(mocked_get_exchange_rate_prediction) -> None:
#     cryptocurrency_action(4)
#
#     mocked_get_exchange_rate_prediction.assert_called_once()


def test_should_return_the_purchase_of_assets_if_the_forecast_rate_is_exceeded_by_5_percent(mocker):
    mocker.patch("app.main.get_exchange_rate_prediction", return_value=1.06)
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


# @pytest.fixture()
# def mocked_exchange_rate_prediction():
#     with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
#         yield mocked_rate

# def test_should_return_resale_assets_if_the_forecast_rate_is_by_5_percent_lower(
#         # mocked_exchange_rate_prediction
# ) -> None:
#     cryptocurrency_action(1)
#
#
# def test_should_return_the_purchase_of_assets_if_the_forecast_rate_is_exceeded_by_5_percent(
#         mocked_exchange_rate_prediction
# ) -> None:
#     pass
