import networkx as nx
import matplotlib.pyplot as plt
import random


def network():
    # 定义交换机和终端的数量
    num_switches = 5
    num_terminals = 3

    # 生成交换机和终端的名称
    switches = ['switch{}'.format(i + 1) for i in range(num_switches)]
    terminals = ['terminal{}'.format(i + 1) for i in range(num_terminals)]

    # 生成随机的网络拓扑
    connections = []
    for switch in switches:
        # 每个交换机连接2-4个其他设备
        num_connections = random.randint(2, 4)
        for i in range(num_connections):
            if random.choice([True, False]):
                # 连接终端
                connections.append((switch, random.choice(terminals)))
            else:
                # 连接交换机
                connections.append((switch, random.choice(switches)))

    # 创建一个空的有向图
    G = nx.DiGraph()

    # 添加所有节点
    G.add_nodes_from(switches + terminals)

    # 添加所有边
    G.add_edges_from(connections)

    # 绘制网络拓扑图
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
