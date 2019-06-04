#!/usr/bin/env python
# coding=utf-8
from operator import attrgetter
from prettytable import PrettyTable


class Data:

    def __init__(self, name, subgragh, degree, eigenvector, information, lac, betweenness, closeness, network):
        """
        name字段表示蛋白质的名字，剩下的是对应的8个属性
        """
        self.name = name
        self.subgragh = subgragh
        self.degree = degree
        self.eigenvector = eigenvector
        self.information = information
        self.lac = lac
        self.betweenness = betweenness
        self.closeness = closeness
        self.network = network


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
    print
    print "=============================== 处理" + fileName + " ==============================="
    print
    x = PrettyTable(
        ["Top", "subgragh", "degree", "eigenvector", "information", "lac", "betweenness", "closeness", "network"])

    """
    本函数的职能是读取fileName表示的数据集文件，处理之后输出正确率
    """

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
            float(lines[6].split(":")[1].strip()),
            float(lines[7].split(":")[1].strip()),
            float(lines[8].split(":")[1].strip()),
            float(lines[9].split(":")[1].strip()),
        ))

    # 开始根据各个属性进行排序，然后和essential进行对比
    for size in sizes:
        x.add_row([
            size,
            judgeByAttr(datas, "subgragh", size),
            judgeByAttr(datas, "degree", size),
            judgeByAttr(datas, "eigenvector", size),
            judgeByAttr(datas, "information", size),
            judgeByAttr(datas, "lac", size),
            judgeByAttr(datas, "betweenness", size),
            judgeByAttr(datas, "closeness", size),
            judgeByAttr(datas, "network", size),
        ])
    print x


# deal("./dip_all.txt", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# deal("./gavin_all.txt", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# deal("./krogan_all.txt", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# deal("./dip_all.txt", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# deal("./mips_all.txt", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
