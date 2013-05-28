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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                print("Key pressed: %s" % pygame.key.name(event.key))
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    box_y -= 1
                elif event.key == pygame.K_DOWN:
                    box_y += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                line_start = pygame.mouse.get_pos()
                pygame.draw.circle(background, (0, 0, 0), line_start, 5)
            elif event.type == pygame.MOUSEBUTTONUP:
                line_end = pygame.mouse.get_pos()
                pygame.draw.line(background, (0, 0, 0), line_start, line_end, 3)

        screen.blit(background, (0, 0))
        screen.blit(box, (box_x, box_y))
        pygame.display.flip()

if __name__ == "__main__":
    main()
