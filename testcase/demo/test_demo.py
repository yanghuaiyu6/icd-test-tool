# import allure
# from allure_commons.types import LinkType, Severity
#
# """
# 使用案例案例
# """
#
#
# @allure.parent_suite('我是父套件')
# @allure.suite('我是儿子套件')
# @allure.sub_suite('我是孙子套件')
# @allure.epic("功能总体描述")
# @allure.feature('功能描述')
# @allure.story('故事描述')
# class Test_demo:
#     @allure.id('我是id')
#     @allure.title('用例标题')
#     @allure.link('https://www.baidu.com/', LinkType.ISSUE, '我是link_ISSUE')
#     @allure.label('我是label')
#     @allure.issue('https://www.baidu.com/', '我是issue')  # 可以挂连接
#     @allure.description('我是description')  # 描述
#     @allure.severity(Severity.BLOCKER)  # 优先级
#     @allure.tag('我是tag')
#     @allure.testcase('https://www.baidu.com/', 'testcase')  # 挂连接到测试用例上面
#     def test_demo1(self):
#         assert 10 == 10  # 断言
#
#     @allure.step('测试的步骤')
#     @allure.title('测试用例2')
#     def test_demo2(self):
#         # log.debug("测试BUG")
#         assert 10 == 11
