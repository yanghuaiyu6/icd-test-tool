import random
import string
import sys
import time
import uiautomation as auto
from common.utile import win_exist, delete_text, warning, first_creat

# 设置全局超时时间
auto.SetGlobalSearchTimeout(3)


# 新建项目
def create_project(project_name, model):
    # icd软件是否启动，可到util配置地址
    win_exist()
    # first_creat()  # 第一次创建时使用，第一次启动会有提示
    # 点击菜单项目
    auto.MenuItemControl(Name="项目").Click()
    auto.MenuItemControl(Name='新建项目').Click()
    auto.ComboBoxControl(Name=" Down").Click()
    # 项目模板的选择ICDModel_brief  & ICDModel_briefV20 & ICDModel_electric  &  ICDModel_v100
    try:
        auto.ListItemControl(Name="ICDModel_" + model).Click()
    except LookupError:
        print("模板不存在，请输入有效模板！")
        # 异常后强制终止程序
        sys.exit()
    # # 文本类型控件
    edit = auto.WindowControl(Name='创建项目').EditControl(Name='', foundIndex=2)
    edit.Click()
    # 删除已有字符
    delete_text()
    # 发送字符
    edit.SendKeys(project_name)
    auto.ButtonControl(Name='确定').Click()
    # 判断是否项目名称重复
    while warning():
        edit.Click()
        # 删除已有字符
        delete_text()
        # 发送字符
        edit.SendKeys(project_name + random.choice(string.ascii_letters))
        auto.ButtonControl(Name='确定').Click()
        if warning():
            auto.ButtonControl(Name='确定').Click()
        else:
            break
    return "success"


# 载入项目
def import_project(project_name):
    win_exist()
    auto.MenuItemControl(Name="项目").Click()
    auto.MenuItemControl(Name='载入项目').Click()
    auto.TreeItemControl(Name=project_name, foundIndex=1).DoubleClick()


#  载入所有项目
def import_project_all():
    win_exist()
    while True:
        auto.MenuItemControl(Name="项目").Click()
        auto.MenuItemControl(Name='载入项目').Click()
        try:
            auto.TreeItemControl(foundIndex=1).DoubleClick()
        except LookupError:
            print("项目加载完了")
            auto.ButtonControl(Name="选定 Enter").Click()
            break


# 载入其他(输入地址有问题待完善)
def import_other_project(address):
    win_exist()
    auto.MenuItemControl(Name="项目").Click()
    time.sleep(1)
    auto.MenuItemControl(Name="载入其它").Click()
    time.sleep(1)
    auto.ButtonControl(Name="上一个位置").Click()
    delete_text()
    auto.SendKeys(address)
    auto.PressKey(auto.Keys.VK_ENTER)
    auto.EditControl(Name="类型", foundIndex=2).Click()
    auto.ButtonControl(Name="打开(O)").Click()
    # 还有异常处理的情况，打开了已存在项目的文件，后续再处理
    auto.ButtonControl(Name="放入项目库后打开").Click()


# 项目合并(待完善)
def project_merge(address):
    win_exist("CCk")
    auto.MenuItemControl(Name="项目").Click()
    auto.MenuItemControl(Name="项目合并").Click()
    merge = auto.WindowControl(Name="项目合并")
    merge.ButtonControl(Name="", foundIndex=3).Click()
    auto.ButtonControl(Name="上一个位置").Click()
    delete_text()
    auto.SendKeys(address)
    auto.PressKey(auto.Keys.VK_ENTER)
    auto.EditControl(Name="类型", foundIndex=2).Click()
    auto.ButtonControl(Name="打开(O)").Click()
    # 点击比较
    merge.ButtonControl(Name="", foundIndex=3).Click()
    # 出现提示框“模板不一样不能比较”
    tip = auto.TextControl(Name="不能比较，因为模板不一致！").Exists()
    if tip:
        auto.ButtonControl(Name="好的 Enter").Click()
        auto.ButtonControl(Name="关闭").Click()
    else:
        merge.ButtonControl(Name="", foundIndex=1).Click()


# 切换项目
def switch_items(project_name):
    win_exist()
    auto.TabItemControl(Name=project_name).Click()


# 重启软件
def restart_project():
    win_exist()
    auto.MenuItemControl(Name="项目").Click()
    auto.MenuItemControl(Name="重启软件").Click()


# 关闭指定项目
def closer_project(project_name):
    win_exist()
    try:
        auto.TabItemControl(Name=project_name).Click()
    except LookupError:
        print("没有该项目，请检查是否打开了该项目！")
        sys.exit()
    auto.MenuItemControl(Name="项目").Click()
    auto.MenuItemControl(Name='关闭项目').Click()


# 关闭所有项目
def closer_project_all():
    win_exist()
    while True:
        auto.MenuItemControl(Name="项目").Click()
        auto.MenuItemControl(Name='关闭项目').Click()
        try:
            auto.TabItemControl(Name='项目目录').Click()
            break
        except LookupError:
            print("继续关闭项目！")
            continue
