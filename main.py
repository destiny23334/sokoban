import pygame
from game import Map
from game.game import Sokoban


def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    
    # 加载示例地图
    game_map = Map.load("data/sample_map.txt")
    print("Loaded map:")
    game_map.display()

    map_data = Map.load("data/sample_map.txt")
    game = Sokoban(map_data)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    main()