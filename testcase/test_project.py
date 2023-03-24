import allure
import pytest
from allure_commons.types import Severity

from common import project
from common.project import import_project
from common.utile import open_ICD_app, close_ICD_app, win_exist


@allure.epic("项目模块")
class TestProject:

    @staticmethod
    def setup_class():
        print("类执行前的前置操作:启动软件")
        open_ICD_app()

    @staticmethod
    def setup():
        print("每个用例前执行的操作：前置窗口")
        win_exist("CC飞机飞管计算机全连接架构内总线数据流设计开发", r"C:\Users\YANG\Desktop\ICMMain.lnk")

    @staticmethod
    def teardown():
        print("每个用例后执行的操作 ")

    @staticmethod
    def teardown_class():
        print("每个类之后执行的操作,关闭软件")
        close_ICD_app()

    @allure.severity(Severity.BLOCKER)  # 优先级  BLOCKER阻塞;CRITICAL严重;NORMAL一般;MINOR次要;TRIVIAL轻微
    @allure.feature("新建项目")
    @allure.story('创建不同模板的项目')
    @allure.title('创建项目')
    @allure.description('该用例适合用来创建不同模板下的项目')
    @pytest.mark.parametrize("project_name,model",
                             [("测试brief项目", "brief"),
                              ("测试briefV20项目", "briefV20"),
                              ("测试electric项目", "electric"),
                              ("测试v100项目", "v100")
                              ])  # 配置参数化进行组合
    @allure.step('1.点击新建项目')
    @allure.step('2.选择不同模板')
    @allure.step('3.给项目命名')
    @allure.step('4.点击确定')
    def test_create_project(self, project_name, model):
        result = project.create_project(project_name, model)
        assert result == "success"

    @allure.feature("载入项目")
    @allure.title('载入A项目')
    def test_import_project(self):
        pass

    @allure.feature("载入所有项目")
    @allure.title('载入所有项目')
    def test_import_project_all(self):
        pass

    @allure.feature("载入其他")
    @allure.title('载入其他项目')
    def test_import_other_project(self):
        pass

    @allure.feature("项目合并")
    @allure.title('合并A和B项目')
    def test_project_merge(self):
        pass
