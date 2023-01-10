from collections import namedtuple
from time import sleep
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    sleep(1)
    """_asdict() should return a dictionary"""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected


def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'brain', False)
    t_after = t_before._replace(id=10, done=True)
    t_excpected = Task('finish book', 'brain', True, 10)
    assert t_after == t_excpected

