import uiautomation as auto

from common.utile import win_exist, delete_text

"""
ICD信号创建
自家电脑可以，公司电脑定位有问题
"""


# 创建ICD信号，自家用
def icd_signal():
    win_exist("CC飞机飞管计算机全连接架构内总线数据流设计开发", r"C:\Users\YANG\Desktop\ICMMain.lnk")
    auto.ButtonControl(Name="显示空白").Click()
    auto.TreeItemControl(Name="", foundIndex=8).DoubleClick()
    auto.ListItemControl(Name="整型域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("整型域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("A")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=14).DoubleClick()
    auto.ListItemControl(Name="Bit域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("Bit域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("B")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=20).DoubleClick()
    auto.ListItemControl(Name="组合域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("组合域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("C")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=26).DoubleClick()
    auto.ListItemControl(Name="Float域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("Float域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("D")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=32).DoubleClick()
    auto.ListItemControl(Name="布尔域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("布尔域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("E")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=38).DoubleClick()
    auto.ListItemControl(Name="枚举域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("枚举域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("F")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=44).DoubleClick()
    auto.ListItemControl(Name="标签域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("标签域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("G")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=50).DoubleClick()
    auto.ListItemControl(Name="字节域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("字节域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("H")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=66).DoubleClick()
    auto.ListItemControl(Name="Double域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("Double域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("I")
    auto.ButtonControl(Name="确认").Click()

    # 向下滑动
    auto.TreeItemControl(Name="", foundIndex=72).Click()
    auto.WheelDown(3)
    auto.TreeItemControl(Name="", foundIndex=59).DoubleClick()
    auto.ListItemControl(Name="BCD域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("BCD域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("J")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=65).DoubleClick()
    auto.ListItemControl(Name="字符域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("字符域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("K")
    auto.ButtonControl(Name="确认").Click()

    # 字符串跳跃1格
    auto.TreeItemControl(Name="", foundIndex=81).DoubleClick()
    auto.ListItemControl(Name="字符串域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("字符串域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("L")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=87).DoubleClick()
    auto.ListItemControl(Name="Unicode域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("Unicode域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("M")
    auto.ButtonControl(Name="确认").Click()

    #  套表域需要修改
    # auto.TreeItemControl(Name="", foundIndex=102).DoubleClick()
    # auto.ListItemControl(Name ="套表域").Click()
    # auto.EditControl(Name="", foundIndex=1).Click()
    # auto.SendKeys("套表域")
    # auto.EditControl(Name="", foundIndex=2).Click()
    # auto.SendKeys("N")
    # auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=103).DoubleClick()
    auto.ListItemControl(Name="占位域").Click()
    auto.SpinnerControl(Name="", foundIndex=3).Click()
    delete_text()
    auto.SendKeys("1")
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("占位域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("O")
    auto.ButtonControl(Name="确认").Click()
    # 保存数据
    auto.ButtonControl(Name="保存数据").Click()


# 公司用ICD创建(每次增加9)
# 准确性还有待提高
def icd_signal_company():
    win_exist("CC飞机飞管计算机全连接架构内总线数据流设计开发", r"C:\Users\YANG\Desktop\ICMMain.lnk")
    auto.ButtonControl(Name="显示空白").Click()
    auto.TreeItemControl(Name="", foundIndex=15).DoubleClick()
    auto.ListItemControl(Name="整型域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("整型域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("A")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=24).DoubleClick()
    auto.ListItemControl(Name="Bit域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("Bit域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("B")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=33).DoubleClick()
    auto.ListItemControl(Name="组合域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("组合域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("C")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=42).DoubleClick()
    auto.ListItemControl(Name="Float域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("Float域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("D")
    auto.ButtonControl(Name="确认").Click()
    #
    auto.TreeItemControl(Name="", foundIndex=51).DoubleClick()
    auto.ListItemControl(Name="布尔域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("布尔域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("E")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=60).DoubleClick()
    auto.ListItemControl(Name="枚举域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("枚举域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("F")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=69).DoubleClick()
    auto.ListItemControl(Name="标签域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("标签域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("G")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=78).DoubleClick()
    auto.ListItemControl(Name="字节域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("字节域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("H")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=100).DoubleClick()
    auto.ListItemControl(Name="Double域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("Double域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("I")
    auto.ButtonControl(Name="确认").Click()

    # 向下滑动
    auto.TreeItemControl(Name="", foundIndex=109).Click()
    auto.WheelDown(3)
    auto.TreeItemControl(Name="", foundIndex=86).DoubleClick()
    auto.ListItemControl(Name="BCD域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("BCD域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("J")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=95).DoubleClick()
    auto.ListItemControl(Name="字符域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("字符域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("K")
    auto.ButtonControl(Name="确认").Click()

    # 字符串跳跃1格
    auto.TreeItemControl(Name="", foundIndex=117).DoubleClick()
    auto.ListItemControl(Name="字符串域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("字符串域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("L")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=126).DoubleClick()
    auto.ListItemControl(Name="Unicode域").Click()
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("Unicode域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("M")
    auto.ButtonControl(Name="确认").Click()

    auto.TreeItemControl(Name="", foundIndex=135).DoubleClick()
    auto.ListItemControl(Name="占位域").Click()
    auto.SpinnerControl(Name="", foundIndex=3).Click()
    delete_text()
    auto.SendKeys("1")
    auto.EditControl(Name="", foundIndex=1).Click()
    auto.SendKeys("占位域")
    auto.EditControl(Name="", foundIndex=2).Click()
    auto.SendKeys("O")
    auto.ButtonControl(Name="确认").Click()
    # 保存数据
    auto.ButtonControl(Name="保存数据").Click()


#  套表域需要修改
# auto.TreeItemControl(Name="", foundIndex=102).DoubleClick()
# auto.ListItemControl(Name ="套表域").Click()
# auto.EditControl(Name="", foundIndex=1).Click()
# auto.SendKeys("套表域")
# auto.EditControl(Name="", foundIndex=2).Click()
# auto.SendKeys("N")
# auto.ButtonControl(Name="确认").Click()


if __name__ == '__main__':
    icd_signal_company()
