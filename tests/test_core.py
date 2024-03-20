from pytemplate import core

class TestCore():
   def test_ReturnsNone(self):
      response = core()
      assert(response == None)