import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "first_name, last_name, full_name, expected_first_name", [
        (None, "Holy", "Jack Holy", "Jack"),
        ("", "Adams", "Mike Adams", ""),
        ("John", "Doe", "John Doe", "John"),
    ])
def test_restore_names(
        first_name: str,
        last_name: str,
        full_name: str,
        expected_first_name: str) -> None:
    users = [{"first_name": first_name,
              "last_name": last_name,
              "full_name": full_name
              }]
    restore_names(users)
    assert users[0]["first_name"] == expected_first_name
