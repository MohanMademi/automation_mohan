import pytest
@pytest.mark.usefixtures("setup")
class TestExamples():

    def test_demo1(self):
        print("demo 1")

    def test_demo2(self):
        print("demo 2")

    def test_demo3(self):
        print("demo 3")

    def test_demo4(self):
        print("demo 4")