import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will be executing after test project")


@pytest.fixture()
def Loaddata():
    print("mohan details")
    return ["mohan","mademi","mademimohan99@gmail.com"]