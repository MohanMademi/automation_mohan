import pytest
@pytest.mark.usefixtures("Loaddata")
class turnFixtures1:
    def test_editprofile(self,Loaddata):
        print(Loaddata[1])