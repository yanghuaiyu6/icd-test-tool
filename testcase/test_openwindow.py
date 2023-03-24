import subprocess
import ctypes
import os
import time
#import win32con
#import win32gui
import uiautomation as auto

def test_windows():
    # 配置软件的启动地址，快捷方式
    os.system(r"C:\Users\WR\Desktop\ICMMain.exe.lnk")
    time.sleep(5)
    ps=auto.PaneControl(searchDepth=1,Name="项目选择框")
    time.sleep(3)
    #print(ps.Name)
    ps.ButtonControl(Name="取消").Click()
    auto.MenuItemControl(Name="项目").Click()
    auto.MenuItemControl(Name='新建项目').Click()
    #创建项目窗格
    np=auto.WindowControl(searchDepth=1,Name="创建项目")
    #print(np.Name)
    #输入项目名称
    name=np.TextControl(Name="名称：")
    pname=name.GetNextSiblingControl()
    pname.Click()

    #pname=np.TextControl(Name="名称")
    #print(pname.Name)
    auto.SendKeys("test")
    np.ButtonControl(Name="确定").Click()

    #创建成品
    auto.TreeItemControl(Name="项目test").RightClick()
    auto.MenuItemControl(Name='新建成品').Click()

    ncp = auto.WindowControl(searchDepth=1, Name="创建新成品")
    cpname=ncp.TextControl(Name="名称：")
    cpname = cpname.GetNextSiblingControl()
    cpname.Click()
    auto.SendKeys("test")
    ncp.ButtonControl(Name="确定").Click()

    #创建插头组
    auto.TreeItemControl(Name="成品test").RightClick()
    auto.MenuItemControl(Name='新建插头组').Click()
    nctz = auto.WindowControl(searchDepth=1, Name="创建新插头组")
    #cpname = ncp.TextControl(Name="名称：")
    #auto.SendKeys("test")
    nctz.ButtonControl(Name="确定").Click()

    #创建插头
    auto.TreeItemControl(Name="插头组").RightClick()
    auto.MenuItemControl(Name='新建Plug').Click()

    ncp = auto.WindowControl(searchDepth=1, Name="创建新Plug")
    cpname = ncp.TextControl(Name="名称：")
    cpname = cpname.GetNextSiblingControl()
    cpname.Click()
    auto.SendKeys("test")
    ncp.ButtonControl(Name="确定").Click()

    #创建总线
    auto.MenuItemControl(Name="项目操作").Click()
    auto.MenuItemControl(Name="总线信息").Click()
    auto.ButtonControl(Name="新增").Click()
    auto.ButtonControl(Name="保存").Click()

    #创建节点
    auto.TreeItemControl(Name="Plugtest").RightClick()
    auto.MenuItemControl(Name='新建1394节点').Click()
    xzx = auto.WindowControl(searchDepth=1, Name="选择总线")
    xzx.ButtonControl(Name="确定").Click()
    xjd = auto.WindowControl(searchDepth=1, Name="创建新1394节点")
    jdname = xjd.TextControl(Name="名称：")
    njdname = jdname.GetNextSiblingControl()
    njdname.Click()
    auto.SendKeys("test")
    auto.ButtonControl(Name="确定").Click()

    #创建ICD
    auto.TreeItemControl(Name="输出").RightClick()
    auto.MenuItemControl(Name="新建ICD").Click()
    auto.TabItemControl(Name="属性信息").Click()
    icdname = auto.TextControl(Name="数据包名称:")
    nicdname = icdname.GetNextSiblingControl()
    nicdname.Click()
    auto.SendKeys("test")
    messageid = auto.TextControl(Name="消息ID:")
    nmessageid = messageid.GetNextSiblingControl()
    nmessageid.Click()
    auto.SendKeys("1H")
    auto.TabItemControl(Name="域信息").Click()
    auto.ButtonControl(Name="保存数据").Click()

    #创建信号
    auto.ButtonControl(Name="显示空白").Click()
    auto.TreeItemControl(Name="36").DoubleClick()
    xjy = auto.WindowControl(searchDepth=1, Name="新建域")
    auto.ListItemControl(Name="整型域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("z")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("z")
    auto.ButtonControl(Name="确认").Click()














