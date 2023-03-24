import allure
import pytest

from common import tree


@allure.epic("构型树模块")
class TestTree:
    @pytest.mark.parametrize("project_name,model",
                             [("测试brief项目", "brief"),
                              ("测试briefV20项目", "briefV20"),
                              ("测试electric项目", "electric"),
                              ("测试v100项目", "v100")])  # 配置参数化进行组合
    def test_create_product(self, project_name, model):
        tree.create_product(project_name, model)
