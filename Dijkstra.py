import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((683,684))

# used to create and populate the screen with a grid
# that will be used to place nodes and barriers
def grid():
    height = 21
    width = 21
    margin = 1

    gridArr = []
    for row in range(31):
        for col in range(31):
            gridArr.append(pygame.draw.rect(screen,(255,255,255),[(margin+width)*col+margin,(margin+height)*row+margin,width,height]))

# main function that builds game screen
# and handles click events
def main():
    pygame.display.set_caption("Dijkstra's Pathfinding")
    grid()
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("click")

if __name__ == "__main__":
    main()