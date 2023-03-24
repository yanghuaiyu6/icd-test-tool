"""
创建一条完整的构型数，包括所有的节点
"""

# 打开软件的情况下,创建构型数（待完善）
from common import tree, bus, icd_signal, project


def full_tree(project_name="项目名称", model="brief", product_name="成品",
              plug_name="Plug", icd_name="ICD", message_id="H"):
    # 创建项目
    project.create_project(project_name, model)
    # 创建成品
    tree.create_product(project_name, product_name)
    # 创建插头组
    tree.create_plugs_group(product_name)
    # 创建插头
    tree.create_plug(plug_name)
    # 总线的添加直接添加所有，单独添加要定位不准确
    bus.bus_add("1394，1553,422,485，TTE")

    # # 创建1394总线节点
    tree.create_bus_point(plug_name, point_name="1394节点", bus_type="1394", point_type="CC")
    tree.create_icd("1394CC", message_id, "1394CC", 1)
    # 信号位置的准确性有待提高
    icd_signal.icd_signal_company()

    tree.create_bus_point(plug_name, point_name="1394节点", bus_type="1394", point_type="CCDL")
    tree.create_icd("1394CCDL", message_id, "1394CCDL", 2)
    icd_signal.icd_signal_company()

    tree.create_bus_point(plug_name, point_name="1553节点", bus_type="1553")
    tree.create_icd("1553", message_id, "1553", 3)
    # 1553 信号添加有问题
    # icd_signal.icd_signal_company()

    tree.create_bus_point(plug_name, point_name="422节点", bus_type="422")
    tree.create_icd("422", message_id, "422", 4)
    # 422 信号添加有问题
    # icd_signal.icd_signal_company()

    if model == "v100":
        # 创建TTE节点，特定模板才有TTE（V100）
        tree.create_bus_point(plug_name, point_name="TTE节点", bus_type="TTE")
        tree.create_icd("TTE", message_id, "TTE", 1)
        # icd_signal_company()

    # 创建无分区成品(非brief模板没有分区)
    tree.create_not_zone_product(project_name, product_name="无分区" + product_name)
    # 收起成品下的插头组
    tree.closeup("成品", 1)
    # 创建无分区成品下的插头
    tree.create_plug(plug_name)
    tree.create_bus_point(plug_name, point_name="无分区1394节点", bus_type="1394", point_type="CC")

    # 新建分区组
    tree.create_zone_group(product_name)
    # 新建分区
    tree.create_zone("分区")
    tree.create_icd("分区数据包", "H", "分区", out_num=1)

    # 新建HMC
    tree.create_hmc("成品")
    tree.create_hmc_pack("HMC")

    # 新建event
    tree.create_event("成品")
    tree.create_event_pack()

    # 新建故障库
    tree.create_fault_database("成品")
    tree.create_fault_pl()
    tree.create_fault_pb()

    pass


if __name__ == '__main__':
    full_tree(project_name="项目brief测试", model="brief", product_name="成品",
              plug_name="Plug", icd_name="ICD", message_id="H")
    # full_tree(project_name="项目briefV20", model="briefV20", product_name="成品",
    #           plug_name="Plug", icd_name="ICD", message_id="H")
    # full_tree(project_name="项目electric", model="electric", product_name="成品",
    #           plug_name="Plug", icd_name="ICD", message_id="H")
    # full_tree(project_name="项目V100", model="v100", product_name="成品",
    #           plug_name="Plug", icd_name="ICD", message_id="H")
    pass