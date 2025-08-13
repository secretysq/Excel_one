# # # pytest 自动找test_开头的测试用例
import pytest
import os
if __name__ == '__main__':
    pytest.main(['-vs',"--alluredir", "./result", "--clean-alluredir"])
    os.system("allure generate ./result -o ./report_allure --clean")