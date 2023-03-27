import ctypes
import os
import time
import win32con
import win32gui
import uiautomation as auto


# 设置ICD路径,根据自己的ICD地址修改路径
ICD_NAME = "CC飞机飞管计算机全连接架构内总线数据流设计开发"
ICD_PATH = r"C:\Users\WR\Desktop\ICMMain.exe.lnk"


# 置顶操作的窗口
def show_win(win_name):
    hwnd = win32gui.FindWindow(None, win_name)
    # 窗口需要正常大小且在后台，不能最小化
    # win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    # 窗口需要最大化且在后台，不能最小化
    ctypes.windll.user32.ShowWindow(hwnd, 3)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
    # 已展示在第一页面，取消置顶
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                          win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)


# 判断ICD软件窗口是否存在,没存在的话他的输入它exe存放地址
def win_exist(win_name=ICD_NAME, path=ICD_PATH):
    try:
        # 切换到当前ICMMain应用，将窗口放于窗口前
        show_win(win_name)
    except Exception as ex:
        print(ex)
        print("没有该窗口！软件没有启动！")
        # 启动ICMMain软件
        os.startfile(path)
        time.sleep(5)
        auto.ButtonControl(Name='取消').Click()


# 项目目录未有过项目，会出现提示窗口
def first_creat():
    # 项目目录没有过项目会出现新窗口提示
    flag = True
    try:
        auto.WindowControl(Name="提示").Click()
    except Exception as ex:
        print(ex)
        print("此窗口不存在，继续执行")
        flag = False
    if flag:
        auto.ButtonControl(Name='好的 Enter').Click()


# 删除已有字符
def delete_text():
    # log.info("删除原有输入框字符")
    auto.SendKeys('{Ctrl}(A)')
    auto.SendKeys('{Delete}')


# 关闭应用程序
def close_ICD_app():
    os.system("taskkill /F /IM ICMMain.exe")


# 启动软件
def open_ICD_app():
    # 配置软件的启动地址，快捷方式
    os.system("start " + ICD_PATH)
    print("xxxx")
    time.sleep(3)
    # 关闭初打开软件弹出的项目窗口
    auto.ButtonControl(Name="取消").Click()
    print("xxxx")


# 输入框提示名称相同
def warning():
    try:
        exist = auto.WindowControl(Name="不能继续").Exists()
        auto.ButtonControl(Name="好的 Enter").Click()
        return exist
    except Exception:
        return False
