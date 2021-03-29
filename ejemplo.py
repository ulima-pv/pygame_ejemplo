import sys, pygame

def main():

    # Setup inicial
    pygame.init()
    size = width, height = 800, 600
    black = 0, 0, 0
    speed = 4
    screen = pygame.display.set_mode(size) # Creamos pantalla
    ball = pygame.image.load("intro_ball.gif")
    ballrect = ball.get_rect()

    #Game Lopp
    while True:
        #1. Get input
        movement = [0, 0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    movement[1] -= speed
                elif event.key == pygame.K_DOWN:
                    movement[1] += speed
                elif event.key == pygame.K_LEFT:
                    movement[0] -= speed
                elif event.key == pygame.K_RIGHT:
                    movement[0] += speed

        #2. Update state
        ballrect = ballrect.move(movement)

        #3. Render
        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()