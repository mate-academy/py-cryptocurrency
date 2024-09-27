from unittest import mock

import pytest

from app import main


@pytest.fixture()
def mocked_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_prediction:
        yield mock_prediction


def test_do_nothing_0_95(mocked_prediction: mock.MagicMock) -> None:
    mocked_prediction.return_value = 0.95
    assert main.cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_1_05(mocked_prediction: mock.MagicMock) -> None:
    mocked_prediction.return_value = 1.05
    assert main.cryptocurrency_action(1) == "Do nothing"
