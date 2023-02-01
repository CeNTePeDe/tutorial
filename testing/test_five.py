import pytest

@pytest.fixture()
def a_tuple():
    return (1, 'foo', None, {'bar': 123})

def test_a_tuple(a_tuple):
    assert a_tuple[3]['bar'] == 23