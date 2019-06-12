#!/usr/bin/env python
# coding=utf-8
from operator import attrgetter
from prettytable import PrettyTable


class Data:

    def __init__(self, name, subgragh, degree, eigenvector, information, betweenness, closeness
                 ):
        """
        name字段表示蛋白质的名字，剩下的是对应的8个属性
        """
        self.name = name
        self.subgragh = subgragh
        self.degree = degree
        self.eigenvector = eigenvector
        self.information = information
        self.betweenness = betweenness
        self.closeness = closeness


# 用来保存正确的中心节点集
essential = []

# 读取 essential.txt 导入中心节点集，保存在essential列表中 
for line in open("./essential.txt"):
    # strip()是对字符串进行去空格操作，去除字符串两边多余的空格
    essential.append(line.strip())


def judgeByAttr(array, attrName, size):
    # 开始根据各个属性进行排序，然后和essential进行对比
    sortedData = sorted(array, key=attrgetter(attrName), reverse=True)

    # 统计正确的数量
    correctRate = 0
    for index in range(0, size - 1):
        if sortedData[index].name.strip() in essential:
            correctRate += 1
    return correctRate


tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:^10}"


def deal(fileName, sizes):
    """
    本函数的职能是读取fileName表示的数据集文件，处理之后会在控制台打印出正确率的表格，并返回正确率结果
    @:param fileName    文件路径
    @:param sizes       取样数组，例如：[100, 200, 300, 400] => 表示分别对前100、前200、前300和前400个节点进行统计
    @:return 返回值的格式如下
    [
        {
            "information":21,
            "betweenness":24,
            "network":25,
            "degree":21,
            "lac":23,
            "subgragh":9,
            "closeness":17,
            "eigenvector":9,
            "size":100
        },
        {
            "information":49,
            "betweenness":53,
            "network":59,
            "degree":49,
            "lac":46,
            "subgragh":17,
            "closeness":36,
            "eigenvector":17,
            "size":200
        },
        {
            "information":77,
            "betweenness":83,
            "network":81,
            "degree":77,
            "lac":71,
            "subgragh":28,
            "closeness":53,
            "eigenvector":28,
            "size":300
        },
        {
            "information":106,
            "betweenness":108,
            "network":111,
            "degree":106,
            "lac":101,
            "subgragh":47,
            "closeness":74,
            "eigenvector":47,
            "size":400
        },
        {
            "information":136,
            "betweenness":142,
            "network":149,
            "degree":136,
            "lac":140,
            "subgragh":64,
            "closeness":89,
            "eigenvector":64,
            "size":500
        },
        {
            "information":171,
            "betweenness":167,
            "network":169,
            "degree":171,
            "lac":174,
            "subgragh":84,
            "closeness":100,
            "eigenvector":84,
            "size":600
        },
        {
            "information":194,
            "betweenness":199,
            "network":214,
            "degree":194,
            "lac":205,
            "subgragh":105,
            "closeness":125,
            "eigenvector":105,
            "size":700
        },
        {
            "information":217,
            "betweenness":218,
            "network":250,
            "degree":217,
            "lac":241,
            "subgragh":115,
            "closeness":151,
            "eigenvector":115,
            "size":800
        },
        {
            "information":247,
            "betweenness":250,
            "network":283,
            "degree":244,
            "lac":268,
            "subgragh":139,
            "closeness":173,
            "eigenvector":139,
            "size":900
        },
        {
            "information":278,
            "betweenness":274,
            "network":306,
            "degree":278,
            "lac":300,
            "subgragh":167,
            "closeness":196,
            "eigenvector":167,
            "size":1000
        }
    ]
    """
    print
    print "=============================== 处理" + fileName + " ==============================="
    print
    x = PrettyTable(
        ["Top", "subgragh", "degree", "eigenvector", "information",
         # "lac",
         "betweenness",
         "closeness",
         # "network"
         ])

    # 用来保存每行数据处理之后得到的Data对象
    datas = []

    # 逐行读取，对每一行进行处理
    for line in open(fileName):
        # 根据制表符进行分割得到一个列表
        lines = line.split("\t")

        # 过滤掉列表中的为空字符串的项，得到的数据格式如下：
        """
        ['1', 'YJR045C', 'Subgragh: 1.39658077E16', 'Degree: 174.0', 'Eigenvector: 0.16140151', 'Information: 
        4.1516886', 'LAC: 4.2413793', 'Betweenness: 468112.88', 'Closeness: 0.022894757', 'Network: 19.038797', 
        '\r\n'] 
        """
        lines = filter(lambda x: x != "", lines)

        # 然后根据上面的结果构造出一个Data对象
        datas.append(Data(
            lines[1],
            float(lines[2].split(":")[1].strip()),
            float(lines[3].split(":")[1].strip()),
            float(lines[4].split(":")[1].strip()),
            float(lines[5].split(":")[1].strip()),
            float(lines[7].split(":")[1].strip()),
            float(lines[8].split(":")[1].strip()),
        ))

    result = []  # 字典，用来存储返回值

    # 开始根据各个属性进行排序，然后和essential进行对比
    for size in sizes:
        item = {
            "size": size,
            "subgragh": judgeByAttr(datas, "subgragh", size),
            "degree": judgeByAttr(datas, "degree", size),
            "eigenvector": judgeByAttr(datas, "eigenvector", size),
            "information": judgeByAttr(datas, "information", size),
            "betweenness": judgeByAttr(datas, "betweenness", size),
            "closeness": judgeByAttr(datas, "closeness", size),

        }
        result.append(item)
        x.add_row([
            size,
            item["subgragh"],
            item["degree"],
            item["eigenvector"],
            item["information"],
            item["betweenness"],
            item["closeness"],
        ])
    print x
    return result


# deal("./dip_all.txt", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# deal("./gavin_all.txt", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# deal("./krogan_all.txt", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# deal("./dip_all.txt", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# deal("./mips_all.txt", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
