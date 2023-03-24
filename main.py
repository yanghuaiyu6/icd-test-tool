import os
import pytest

# 主函数要写在测试用例外边才行
if __name__ == '__main__':
    # 执行测试用例生成测试结果
    pytest.main()
    # 生成测试报告
    os.system(r"allure generate ./report/test-results -o ./report/test-report --clean")
    # 打开测试报告
    os.system("allure open -h 127.0.0.1 -p 8883 ./report/test-report")
