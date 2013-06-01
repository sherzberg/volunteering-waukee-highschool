import pygame
pygame.init()


def main():
    screen = pygame.display.set_mode((640, 480))

    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill(pygame.color.Color('Yellow'))

    box = pygame.Surface((25, 25))
    box = box.convert()
    box.fill((0, 0, 0))
    box_x = 20
    box_y = 20

    running = True
    clock = pygame.time.Clock()

    direction = (0, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                print("Key pressed: {key}".format(key=key))
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    direction = (0, 1)
                elif event.key == pygame.K_DOWN:
                    direction = (0, -1)
            elif event.type == pygame.KEYUP:
                direction = (0, 0)

        screen.blit(background, (0, 0))
        box_x += direction[0]
        box_y += direction[1]
        screen.blit(box, (box_x, box_y))
        pygame.display.flip()

if __name__ == "__main__":
    main()
