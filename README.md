# ICD测试工具

#### 介绍
> 将功能的操作细化到每个点击和按钮当中，通过组装不同的操作来组装流程，从而达到自动操作的目的。
主要用于ICD软件测试使用，六部为主要测试方向，在过程中不断地调整。

#### 软件架构
使用的技术栈：python+uiautomation+logging+allure+pytest

#### 使用说明
## 文件说明：
**1.common（公共方法）**
- bus.py---总线相关
- icd_signal--信号相关
- project--项目相关
- main--程序启动

**2.log(日志文件)**
- 自己封装python自带loggin日志
- 自定义日志格式，打印方式等

**3.report（测试报告）**
- allure生成测试报告

**4.testcase（测试用例）**
- 一个用例对应一个py文件

**5.main.py（启动入口）**
- 执行用例
- 生成报告
- 打开报告

**用包说明：**

uiautomation是定位控件的位置方法，明确定位的控件类型，控件名称和具体的控件位置来定位到具体的控件，从而为后续控制鼠标键盘做准备
```
import uiautomation as auto
    # 树型列表控件
    auto.TreeItemControl(Name="控件名称", foundIndex="索引位置")
    # 列表控件
    auto.ListItemControl(Name="控件名称", foundIndex="索引位置")
    # 菜单栏控件
    auto.MenuItemControl(Name="控件名称", foundIndex="索引位置")
    # 页签控件
    auto.TabItemControl(Name="控件名称", foundIndex="索引位置")
    # 编辑框控件
    auto.EditControl(Name="控件名称", foundIndex="索引位置")
    # 单元格控件
    auto.DataItemControl(Name="控件名称", foundIndex="索引位置")
    # 窗口控件
    auto.WindowControl(Name="控件名称", foundIndex="索引位置")
    # 按钮类型控件
    auto.ButtonControl(Name="控件名称", foundIndex="索引位置")
    # 选框控件
    auto.ComboBoxControl(Name="控件名称", foundIndex="索引位置")
```
    

找到控件位置之后，鼠标控制就是左点击和右点击的操作了
    
    auto.ButtonControl(Name="控件名称", foundIndex="索引位置").Click()
    auto.ButtonControl(Name="控件名称", foundIndex="索引位置").RightClick()
    
相关的操作可以搜索该包的操作进行完成

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

