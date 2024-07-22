from pytemplate import method1


class TestCore:
    def test_ReturnsNone(self):
        response = method1()
        assert response == None
