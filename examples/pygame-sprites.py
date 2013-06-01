import pygame
pygame.init()


VELOCITY = 1


class Ball(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ball.png")
        self.image = self.image.convert()
        self.image.convert_alpha()
        key = self.image.get_at((0, 0))
        self.image.set_colorkey(key, pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.centerx = start_x
        self.rect.centery = start_y

    def set_direction(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("wall.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()


def main():
    screen = pygame.display.set_mode((640, 480))

    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill(pygame.color.Color('Yellow'))

    wall = Wall()
    ball = Ball(25, 25)

    running = True
    clock = pygame.time.Clock()

    sprites = pygame.sprite.Group(ball, wall)

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
                    direction = (0, VELOCITY)
                elif event.key == pygame.K_DOWN:
                    direction = (0, -VELOCITY)
            elif event.type == pygame.KEYUP:
                direction = (0, 0)

        if ball.rect.colliderect(wall.rect):
            print("COLLISION!!!!!!!!")

        screen.blit(background, (0, 0))
        ball.set_direction(direction[0], direction[1])

        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
