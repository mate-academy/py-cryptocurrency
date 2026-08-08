from typing import Union
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "course_difference, result",
    [
        pytest.param(
            1.05,
            "Do nothing",
            id="Should return 'Do nothing' on boundary value",
        ),
        pytest.param(
            0.95,
            "Do nothing",
            id="Should return 'Do nothing' on boundary value",
        ),
        pytest.param(
            1.06,
            "Buy more cryptocurrency",
            id="Should return 'Buy more cryptocurrency' "
            "if prediction will be more than 5%",
        ),
        pytest.param(
            0.94,
            "Sell all your cryptocurrency",
            id="Should return 'Sell all your cryptocurrency' "
            "if prediction will be lower than -5%",
        ),
        pytest.param(
            0.97,
            "Do nothing",
            id="Should return 'Do nothing' "
            "if prediction won't be more than 5% difference",
        ),
    ],
)
def test_cryptocurrency_action(
    course_difference: Union[int, float],
    result: str,
) -> None:
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda args: course_difference
    )
    assert cryptocurrency_action(1) == result
