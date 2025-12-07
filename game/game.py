from copy import deepcopy

from common import ActionEnum
from .map import Map


class Sokoban:

    def __init__(self, game_map: Map):
        self._game_map = game_map


    def is_win(self):
        """
        判断游戏是否胜利
        """
        pass

    def is_done(self):
        """
        是否没有可移动的操作了

        Returns:

        """

    def step(self, action: ActionEnum):
        pass


    def get_map(self) -> Map:
        return deepcopy(self._game_map)