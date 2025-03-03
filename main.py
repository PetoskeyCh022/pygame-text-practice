import pygame
import sys
import config # Import the config module

def init_game():
  pygame.init()
  screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
  pygame.display.set_caption(config.TITLE)
  return screen

def handle_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      return False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        return False
  return True


def draw_text(screen, text, font, color, x_cord, y_cord):
  img = font.render(text, True, color)
  screen.blit(img, (x_cord, y_cord))





def main():
  screen = init_game()
  clock = pygame.time.Clock() # Initialize the clock here
  running = True

  text_font1 = pygame.font.SysFont(None, 30, False, True)

  text_font2 = pygame.font.SysFont('Times New Roman', 50, True, False)

  text_font3 = pygame.font.Font("FreeMono.ttf", 30)



  while running:
    running = handle_events()
    screen.fill(config.WHITE) # Use color from config


    draw_text(screen, "Charles Petoskey", text_font1, config.GREEN, 300, 200)

    draw_text(screen, "Career Tech Center", text_font2, config.RED, 200, 300)

    draw_text(screen, "Career Tech Center", text_font3, config.RED, 200, 500)



    pygame.display.flip()

    # Limit the frame rate to the specified frames per second (FPS)
    clock.tick(config.FPS) # Use the clock to control the frame rate

  
  pygame.quit()
  sys.exit()






if __name__ == "__main__":
  main()
