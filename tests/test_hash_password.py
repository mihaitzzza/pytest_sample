from data import hash_password


def test_hash_password():
    mocked_password = "python123"
    hashed_password = hash_password(mocked_password)

    assert type(hashed_password) == str
    assert set(hashed_password) == set(mocked_password)
