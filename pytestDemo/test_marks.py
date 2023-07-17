import pytest

@pytest.mark.smoke
def test_demoProgram():
    print("hello")
    msg = "hello"
    assert msg == "hello"

@pytest.mark.xfailpytest
def test_project():
    print("world")
    msg2 = "hi"
    assert msg2 =="hi"

@pytest.mark.smoke
def test_project():
    print("Mohan")
    msg2 = "automation"
    assert msg2 =="automation"


@pytest.mark.skip
def test_project():
    print("world")
    msg2 = "project"
    assert msg2 =="hi"