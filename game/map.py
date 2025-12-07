from typing import List, Tuple

type MapData = List[List[str]] # 二维字符列表
type Location = Tuple[int, int]

class Map:
    """
    推箱子游戏地图类
    地图元素说明:
    # - 墙壁 (Wall)
    x - 目标点 (Target)
    $ - 箱子 (Box)
    @ - 玩家 (Player)
    * - 在目标点上的箱子
    + - 在目标点上的玩家
    . - 空地 (Floor)

    数据格式为：
    1. 第一行的两个数字，表示地图的大小，行 * 列 （n * m）
    2. 接下来的 n 行，每一行有 m 个字符。每个字符含义如上所述


    """

    def __init__(self, data: MapData):
        """
        初始化地图
        
        Args:
            data (list[list[str]]): 地图数据
        """
        if not data or not data[0]:
            raise ValueError("Invalid map data")
        self.data = data
        self.width = len(data)
        self.height = len(data[0])

        # 添加地图元素
        self.targets = []
        self.boxes = []
        # for x in range(self.width):
        #     for y in range(self.height):
        #         element = self.data[y][x]
        #         if element == 'x':
        #             self.targets.append((x, y))
        #         elif element == '$':
        #             self.boxes.append((x, y))
        #         elif element == '@':
        #             self.player = (x, y)
        #         elif element == '*':
        #             self.boxes.append((x, y))
        #         elif element == '+':
        #             self.player = (x, y)

    def save(self, filename):
        """
        保存地图到文件
        
        Args:
            filename (str): 保存的文件名
        """
        with open(filename, 'w', encoding='utf-8') as f:
            # 写入地图尺寸
            f.write(f"{self.width} {self.height}\n")
            # 写入地图数据
            for row in self.data:
                f.write(''.join(row) + '\n')

    @classmethod
    def load(cls, filename):
        """
        从文件加载地图
        
        Args:
            filename (str): 加载的文件名
            
        Returns:
            Map: 加载的地图对象
        """
        with open(filename, 'r', encoding='utf-8') as f:
            # 读取地图尺寸
            dimensions = f.readline().strip().split()
            if len(dimensions) != 2:
                raise ValueError("Invalid map dimensions")
            width, height = int(dimensions[0]), int(dimensions[1])

            # 读取地图数据
            data = []
            for _ in range(height):
                line = f.readline()
                if line:
                    # 移除换行符并转换为字符列表
                    row = list(line.rstrip('\n'))
                    data.append(row)

            return cls(width, height, data)

    def get_element(self, x, y):
        """
        获取指定位置的地图元素
        
        Args:
            x (int): x坐标
            y (int): y坐标
            
        Returns:
            str: 地图元素字符
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.data[y][x]
        return None

    def set_element(self, x, y, element):
        """
        设置指定位置的地图元素
        
        Args:
            x (int): x坐标
            y (int): y坐标
            element (str): 要设置的元素字符
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.data[y][x] = element

    def display(self):
        """
        显示地图（用于调试）
        """
        for row in self.data:
            print(''.join(row))
