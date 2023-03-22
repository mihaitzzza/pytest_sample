import pytest
from unittest.mock import MagicMock
from data import User


@pytest.fixture
def mocked_hash_password():
    return MagicMock(return_value="mocked_password")


@pytest.fixture
def mock_user(monkeypatch, mocked_hash_password):
    def _(email="a@gmail.com", password="python123"):
        monkeypatch.setattr("data.hash_password", mocked_hash_password)
        return User(email, password)

    return _


def test_user_email(mock_user):
    user = mock_user()
    assert user.email == "a@gmail.com"


def test_user_password(mock_user, mocked_hash_password):
    user = mock_user(password="qwerty")

    assert user._User__password == "mocked_password"
    mocked_hash_password.assert_called_with("qwerty")
