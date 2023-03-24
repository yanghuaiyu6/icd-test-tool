import uiautomation as auto

from common.utile import win_exist, delete_text

"""
一个项目添加多条总线，只能调用一次，将所有需要的总线第一次写上去，多次调用定位不准确
"""


# 添加总线信息
def bus_add(bus):
    win_exist("CC飞机飞管计算机全连接架构内总线数据流设计开发", r"C:\Users\YANG\Desktop\ICMMain.lnk")
    auto.MenuItemControl(Name="项目操作").Click()
    auto.MenuItemControl(Name="总线信息").Click()
    # 新增多条总线
    index = 0
    if "1394" in bus:
        for i in range(2):
            index += 1
            auto.ButtonControl(Name="新增").Click()
            if index > 2:
                choose_bus_type = auto.DataItemControl(Name="", foundIndex=index * 3)
            else:
                choose_bus_type = auto.DataItemControl(Name="", foundIndex=index + (index - 1) * 2)
            choose_bus_type.Click()
            position = choose_bus_type.GetPosition()
            print("当前控件的坐标为：", position)
            x = position[0]
            y = position[1]
            if i == 0:
                auto.Click(x, y + 20)
                auto.DataItemControl(Name="bus_0").DoubleClick()
                delete_text()
                auto.SendKeys("1394CC")
            if i == 1:
                auto.Click(x, y + 40)
                auto.DataItemControl(Name="bus_1").DoubleClick()
                delete_text()
                auto.SendKeys("1394CCDL")
            auto.ButtonControl(Name='保存').Click()
    # if "1394CCDL" in bus:
    #     index += 1
    #     auto.ButtonControl(Name="新增").Click()
    #     if index > 2:
    #         choose_bus_type = auto.DataItemControl(Name="", foundIndex=index * 3)
    #     else:
    #         choose_bus_type = auto.DataItemControl(Name="", foundIndex=index + (index - 1) * 2)
    #     choose_bus_type.Click()
    #     position = choose_bus_type.GetPosition()
    #     print("当前控件的坐标为：", position)
    #     x = position[0]
    #     y = position[1]
    #     auto.Click(x, y + 40)
    #     auto.ButtonControl(Name='保存').Click()

    if "1553" in bus:
        index += 1
        auto.ButtonControl(Name="新增").Click()
        if index > 2:
            choose_bus_type = auto.DataItemControl(Name="", foundIndex=index * 3)
        else:
            choose_bus_type = auto.DataItemControl(Name="", foundIndex=index + (index - 1) * 2)
        choose_bus_type.Click()
        position = choose_bus_type.GetPosition()
        print("当前控件的坐标为：", position)
        x = position[0]
        y = position[1]
        auto.Click(x, y + 60)
        auto.DataItemControl(Name="bus_" + str(index - 1)).DoubleClick()
        delete_text()
        auto.SendKeys("1553总线")
        auto.ButtonControl(Name='保存').Click()

    if "422" in bus:
        index += 1
        auto.ButtonControl(Name="新增").Click()
        if index > 2:
            choose_bus_type = auto.DataItemControl(Name="", foundIndex=index * 3)
        else:
            choose_bus_type = auto.DataItemControl(Name="", foundIndex=index + (index - 1) * 2)
        choose_bus_type.Click()
        position = choose_bus_type.GetPosition()
        print("当前控件的坐标为：", position)
        x = position[0]
        y = position[1]
        auto.Click(x, y + 70)
        auto.DataItemControl(Name="bus_" + str(index - 1)).DoubleClick()
        delete_text()
        auto.SendKeys("422总线")
        auto.ButtonControl(Name='保存').Click()

    if "485" in bus:
        # index += 1
        # auto.ButtonControl(Name="新增").Click()
        # auto.Click(x, y + 100)
        pass

    if "TTE" in bus:
        index += 1
        auto.ButtonControl(Name="新增").Click()
        if index > 2:
            choose_bus_type = auto.DataItemControl(Name="", foundIndex=index * 3)
        else:
            choose_bus_type = auto.DataItemControl(Name="", foundIndex=index + (index - 1) * 2)
        choose_bus_type.Click()
        position = choose_bus_type.GetPosition()
        print("当前控件的坐标为：", position)
        x = position[0]
        y = position[1]
        auto.Click(x, y + 120)
        auto.DataItemControl(Name="bus_" + str(index - 1)).DoubleClick()
        delete_text()
        auto.SendKeys("TTE总线")
        auto.ButtonControl(Name='保存').Click()
