import pytest
from pytest_mock import MockerFixture


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    ("prediction", "expected_action"),
    [
        (106.0, "Buy more cryptocurrency"),
        (94.0, "Sell all your cryptocurrency"),
        (103.0, "Do nothing"),
        (98.0, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    mocker: MockerFixture,
    prediction: float,
    expected_action: str,
) -> None:
    mock_prediction = mocker.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=prediction,
    )

    result = cryptocurrency_action(100.0)

    assert result == expected_action
    mock_prediction.assert_called_once()
