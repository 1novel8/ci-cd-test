from funcs.base_funcs import say_hello
from main import hello


def test_say_hello():
    assert say_hello() == "Hello, World"


def test_hello_endpoint():
    assert hello() == {"message": "Hello, World"}
