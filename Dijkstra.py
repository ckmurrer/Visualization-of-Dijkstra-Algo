import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((683,684))

gridArr = []
height = 21
width = 21
margin = 1

# used to create and populate the screen with a grid
# that will be used to place nodes and barriers
def grid():

    for row in range(31):
        tmpArr = []
        for col in range(31):
            tmpArr.append((pygame.draw.rect(screen,(255,255,255),[(margin+width)*col+margin,(margin+height)*row+margin,width,height])))
            gridArr.append(tmpArr)

# placement function for walls that block the path of
# the algorithm to make it pathfind around it
def walls():
    print("walls")

# placement function of the starting position(green) and the ending
# position(red) that the algorithm has to find the path for
def start_stop_nodes(row,col,count):
    if count == 0:
        gridArr[col][row] = pygame.draw.rect(screen,(0,255,0),[(margin+width)*row+margin,(margin+height)*col+margin,width,height])
        pygame.display.flip()
    elif count == 1:
        gridArr[col][row] = pygame.draw.rect(screen,(255,0,0),[(margin+width)*row+margin,(margin+height)*col+margin,width,height])
        pygame.display.flip()

# main function that builds game screen
# and handles click events
def main():
    count = 0
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
                row,col = pygame.mouse.get_pos()
                row = row // (width+margin)
                col = col // (height+margin)

                if event.button == 1:
                    start_stop_nodes(row,col,count)
                    count+=1

                if event.button == 3:
                    if event.type == pygame.MOUSEMOTION:
                        walls()


if __name__ == "__main__":
    main()