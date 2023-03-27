import random
import string
import uiautomation as auto

# 新建成品
from common.bus import bus_add
from common.utile import win_exist, delete_text


def create_product(project_name, product_name):
    win_exist()
    # 点击项目启动
    auto.TreeItemControl(Name=project_name).RightClick()
    auto.MenuItemControl(Name='新建成品').Click()
    a = auto.EditControl(Name='', foundIndex=1, ProcessId=25088)
    a.Click()
    # 删除已有字符
    delete_text()
    a.SendKeys(product_name)
    auto.ButtonControl(Name='确定').Click()


# 新建插头组
def create_plugs_group(product_name):
    win_exist()
    auto.TreeItemControl(Name=product_name).RightClick()
    auto.MenuItemControl(Name="新建插头组").Click()
    auto.ButtonControl(Name='确定').Click()


# 创建多个插头
def create_plugs(plug_name, times):
    win_exist()
    times = int(times)
    if times == 1:
        create_plug(plug_name)
    if times > 1:
        for i in range(times):
            name = plug_name + str(i + 1)
            create_plug(name)


# 新建插头
def create_plug(plug_name):
    win_exist()
    auto.TreeItemControl(Name="插头组").RightClick()
    auto.MenuItemControl(Name="新建Plug").Click()
    a = auto.EditControl(Name='', foundIndex=1)
    a.Click()
    # 删除已有字符
    delete_text()
    a.SendKeys(plug_name)
    auto.ButtonControl(Name='确定').Click()


# 创建多个成品的插头组
def create_plugs_groups(product_name, times):
    win_exist()
    for i in range(times):
        name = product_name + str(i + 1)
        print(name)
        auto.TreeItemControl(Name=name).RightClick()
        auto.MenuItemControl(Name="新建插头组").Click()
        auto.ButtonControl(Name='确定').Click()


# 创建总线类型节点,默认CC总线
# 总线命名以及多条创建需要改进
def create_bus_point(plug_name, point_name, bus_type, point_type="CC"):
    # 给1394总线类型的专属变量
    bus_point_type = bus_type + point_type
    win_exist()
    auto.TreeItemControl(Name=plug_name).RightClick()
    auto.MenuItemControl(Name="新建" + bus_type + "节点").Click()
    # 需要添加总线
    bus = auto.WindowControl(Name='提示').Exists()
    # 未添加总线的情况
    if bus:
        auto.ButtonControl(Name='好的 Enter').Click()
        bus_add(bus_type)
        auto.TreeItemControl(Name=plug_name).RightClick()
        auto.MenuItemControl(Name="新建" + bus_type + "节点").Click()

    # 选择总线
    auto.ComboBoxControl(Name=" Down").Click()
    if bus_type == "1394":
        auto.ListItemControl(Name=bus_type + point_type).Click()
    else:
        auto.ListItemControl(Name=bus_type + "总线").Click()
    auto.ButtonControl(Name="确定").Click()
    auto.WindowControl(Name="创建新" + bus_type + "节点").Click()
    edit = auto.EditControl(Name="", foundIndex=1)
    edit.Click()
    # 删除已有字符
    delete_text()
    edit.SendKeys(point_name)
    # 选择节点类型RN/CC
    if bus_point_type == "1394CCDL":
        auto.ComboBoxControl(foundIndex=1).Click()
        # 1394CCDL类型节点暂不设置
        auto.ListItemControl(Name="CCDL-RX").Click()
    if bus_point_type == "1394CC":
        auto.ComboBoxControl(foundIndex=1).Click()
        auto.ListItemControl(Name=point_type).Click()
    if bus_point_type == "1553":
        # 1553节点类型不一样
        auto.ComboBoxControl(Name=" Down", foundIndex=1).Click()
        # auto.ListItemControl(Name=point_type).Click()
    if bus_point_type == "422":
        auto.ComboBoxControl(Name=" Down", foundIndex=1).Click()
        # auto.ListItemControl(Name=point_type).Click()
    if bus_point_type == "TTE":
        auto.ComboBoxControl(Name=" Down", foundIndex=1).Click()
        # auto.ListItemControl(Name=point_type).Click()

    auto.ButtonControl(Name="确定").Click()


# 创建多条总线节点
def create_1394points(plug_name, point_name, bus_type, times):
    times = int(times)
    for i in range(times):
        name = point_name + str(i + 1)
        plug_new_name = plug_name + str(i + 1)
        print(name, plug_new_name, times)
        create_bus_point(plug_new_name, name, bus_type)


# 新建ICD
def create_icd(icd_name, message_id, bus_type, out_num):
    win_exist()
    auto.TreeItemControl(Name="输出", foundIndex=out_num).RightClick()
    # 根据总线类型点击选项
    if bus_type == "1394CC":
        auto.MenuItemControl(Name="新建ICD").Click()
    if bus_type == "1394CCDL":
        auto.MenuItemControl(Name="新建CCDL包").Click()
    if bus_type == "1553":
        auto.MenuItemControl(Name="新建1553包").Click()
    if bus_type == "422":
        auto.MenuItemControl(Name="新建422包").Click()
    if bus_type == "TTE":
        auto.MenuItemControl(Name="新建TTE包").Click()
    if bus_type == "分区":
        auto.MenuItemControl(Name="新建分区表").Click()

    auto.TabItemControl(Name="属性信息").Click()
    edit = auto.EditControl(foundIndex=2)
    edit.Click()
    delete_text()
    edit.SendKeys(icd_name + "_" + random.choice(string.ascii_letters))
    edit = auto.EditControl(foundIndex=3)
    edit.Click()

    # 判断消息ID是否有数字
    strs = message_id
    for s in strs:
        if s.isdigit():
            print("包含数字")
            edit.SendKeys(message_id)
            break
    else:
        print("不包含数字")
        edit.SendKeys(str(out_num + random.randint(0, 100)) + message_id)

    auto.TabItemControl(Name="域信息").Click()
    auto.ButtonControl(Name="保存数据").Click()


# 新建ICD
def create_stof(stof_name):
    win_exist()
    auto.TreeItemControl(Name="输出").RightClick()
    auto.MenuItemControl(Name="新建stof包").Click()
    # auto.MenuItemControl(Name="新建CCDL包").Click()
    auto.TabItemControl(Name="属性信息").Click()
    edit = auto.EditControl(foundIndex=2)
    edit.Click()
    delete_text()
    edit.SendKeys(stof_name)
    edit = auto.EditControl(foundIndex=3)
    edit.Click()
    auto.TabItemControl(Name="域信息").Click()
    auto.ButtonControl(Name="保存数据").Click()


# 新建多条ICD
def create_icds(icd_name, message_id, times):
    times = int(times)
    for i in range(times):
        icd_new_name = icd_name + str(i + 1)
        icd_id = str(i + 1) + message_id
        create_icd(icd_new_name, icd_id)


# 新建无分区成品
def create_not_zone_product(project_name, product_name):
    win_exist()
    # 点击项目启动
    auto.TreeItemControl(Name=project_name).RightClick()
    auto.MenuItemControl(Name='新建无分区成品').Click()
    a = auto.EditControl(Name='', foundIndex=1, ProcessId=25088)
    a.Click()
    # 删除已有字符
    delete_text()
    a.SendKeys(product_name)
    auto.ButtonControl(Name='确定').Click()


# 创建多个无分区成品
def create_not_zone_products(project_name, product_name, times):
    win_exist()
    for i in range(times):
        print("创建第" + str(i) + "成品！")
        name = product_name + str(i + 1)
        create_not_zone_product(project_name, name)


# 展开
def expand(point_name, index):
    auto.TreeItemControl(Name=point_name, foundIndex=index).RightClick()
    auto.MenuItemControl(Name="展开").Click()


# 展开所有
def expand_all(point_name, index):
    win_exist()
    auto.TreeItemControl(Name=point_name, foundIndex=index).RightClick()
    auto.MenuItemControl(Name="展开所有").Click()


# 收起
def closeup(point_name, index):
    win_exist()
    auto.TreeItemControl(Name=point_name, foundIndex=index).RightClick()
    auto.MenuItemControl(Name="收起").Click()


# 收起所有
def closeup_all(point_name, index):
    win_exist()
    auto.TreeItemControl(Name=point_name, foundIndex=index).RightClick()
    auto.MenuItemControl(Name="收起所有").Click()


# 新建分区组
def create_zone_group(product_name):
    win_exist()
    auto.TreeItemControl(Name=product_name).RightClick()
    auto.MenuItemControl(Name="新建分区组").Click()
    auto.ButtonControl(Name='确定').Click()


# 创建多个成品的分区组
def create_zone_groups(product_name, times):
    win_exist()
    for i in range(times):
        name = product_name + str(i + 1)
        print(name)
        auto.TreeItemControl(Name=name).RightClick()
        auto.MenuItemControl(Name="新建分区组").Click()
        auto.ButtonControl(Name='确定').Click()


# 新建分区
def create_zone(zone_name):
    win_exist()
    auto.TreeItemControl(Name="分区组").RightClick()
    auto.MenuItemControl(Name="新建分区").Click()
    a = auto.EditControl(Name='', foundIndex=1)
    a.Click()
    # 删除已有字符
    delete_text()
    a.SendKeys(zone_name)
    auto.ButtonControl(Name='确定').Click()


# 创建多个分区
def create_zones(zone_name, times):
    win_exist()
    for i in range(times):
        name = zone_name + str(i + 1)
        create_zone(name)


# 新建成品下的HCM
def create_hmc(product_name):
    win_exist()
    auto.TreeItemControl(Name=product_name).RightClick()
    auto.MenuItemControl(Name="新建HMC").Click()
    auto.ButtonControl(Name="确定").Click()


# 创建HMC包
def create_hmc_pack(HCM_name):
    win_exist()
    auto.TreeItemControl(Name=HCM_name).RightClick()
    auto.MenuItemControl(Name="新建Hmc").Click()


# 无分区成品下的Hmc
def not_zone_hmc():
    win_exist()
    auto.TreeItemControl(Name='无分区成品').Click()
    auto.TreeItemControl(Name='HMC').RightClick()
    auto.MenuItemControl(Name='新建Hmc').Click()


# 新建成品下的EVENT
def create_event(product_name):
    win_exist()
    auto.TreeItemControl(Name=product_name).RightClick()
    auto.MenuItemControl(Name="新建EVENT").Click()
    auto.ButtonControl(Name="确定").Click()


# 创建event包
def create_event_pack():
    win_exist()
    auto.TreeItemControl(Name="EVENT").RightClick()
    auto.MenuItemControl(Name="新建Event").Click()


# 新建故障库
def create_fault_database(product_name):
    auto.ButtonControl(Name="确定").Click()
    win_exist()
    auto.TreeItemControl(Name=product_name).RightClick()
    auto.MenuItemControl(Name="新建故障库").Click()


# 新建PB故障库
def create_fault_pb():
    win_exist()
    auto.TreeItemControl(Name="PB").RightClick()
    auto.MenuItemControl(Name="新建PB故障库").Click()


# 新建PL故障库
def create_fault_pl():
    win_exist()
    auto.TreeItemControl(Name="PL").RightClick()
    auto.MenuItemControl(Name="新建PL故障库").Click()


# 剪切功能
def cut(point_name):
    win_exist()
    auto.TreeItemControl(Name=point_name).RightClick()
    auto.MenuItemControl(Name="剪切").Click()


# 复制功能
def copy(point_name):
    win_exist()
    auto.TreeItemControl(Name=point_name).RightClick()
    auto.MenuItemControl(Name="复制").Click()


# 删除节点
def delete(point_name):
    win_exist()
    auto.TreeItemControl(Name=point_name).RightClick()
    auto.MenuItemControl(Name="删除").Click()
    auto.ButtonControl(Name="是的 Enter").Click()


# 导出ICD,其余功能待完善
def export_icd(icd_name, import_address):
    win_exist()
    auto.TreeItemControl(Name=icd_name).RightClick()
    auto.MenuItemControl(Name="导出ICD(Excel)").Click()
    import_window = auto.WindowControl(Name="ICD导出")
    import_window.Click()
    import_window.EditControl(foundIndex=1).Click()
    auto.SendKeys(import_address)
    import_window.ButtonControl(Name="全选").Click()
    import_window.ButtonControl(Name="确认").Click()


# 粘贴
def paste(num):
    win_exist()
    for i in range(num):
        auto.TreeItemControl(Name="输出").RightClick()
        auto.MenuItemControl(Name="粘贴").Click()


# 粘贴为引用
def paste_reference(num):
    win_exist()
    for i in range(num):
        auto.TreeItemControl(Name="输出").RightClick()
        auto.MenuItemControl(Name="粘贴为引用").Click()
