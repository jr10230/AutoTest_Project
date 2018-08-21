from model import function, myunit
from LoginPage import *
import time
import paramunittest

# @paramunittest.parametrized(
#     {"un": "admin", "pw": "0816"},
#     {"un": "admin8", "pw": "10816"},
#     {"un": "admin9", "pw": "02816"},
#     {"un": "admin7", "pw": "08316"},
#     {"un": "admin6", "pw": "08146"},
#     {"un": "admin5", "pw": "08165"},
#     {"un": "admin4", "pw": "08156"},
#     {"un": "admin3", "pw": "08146"},
#     {"un": "admin2", "pw": "08176"},
#     {"un": "admin1", "pw": "08186"},
# )
class LoginTest(myunit.StartEnd):
    # def setParameters(self, un, pw):
    #     self.username = un
    #     self.password = pw

    def test_login(self):
        print("Start run...")
        po = LoginPage(self.driver)
        # po.Login_action(self.username, self.password)
        po.Login_action("admin", "0816")
        time.sleep(3)

        self.assertEqual(po.type_loginPass_hint(), '个人资料')