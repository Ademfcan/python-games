  # import the pygame module, so you can use it
import pygame
import pygame.key

black = (0,0,0)

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("the game of games")
    image = pygame.image.load("4AIG.gif")
    image.set_colorkey((255,0,255))
    #image.set_alpha(128)
    # create a surface on screen that has the size of 240 x 180
    #screen = pygame.display.set_mode((1930,1020))
    screenInfo = pygame.display.Info()
    screen = pygame.display.set_mode((screenInfo.current_w, screenInfo.current_h), pygame.DOUBLEBUF | pygame.NOFRAME | pygame.FULLSCREEN)
    
    x = 200
    y = 200;
    screen.blit(image, (x,y))
    pygame.display.flip()          


    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                print("Quiting")
                running = False
                break
            elif event.type == pygame.KEYUP:
                if event.key == ord ( "w" ) or event.key == pygame.K_UP:
                 if y > 10:
                     y = y - 10;
                 screen.fill((black))
                 pygame.display.update()
                 screen.blit(image, (x, y))
                 pygame.display.flip()
                elif event.key == ord ( "s" ) or event.key == pygame.K_DOWN:
                 if (y < 1020):
                         y = y + 10;
                 screen.fill((black))
                 pygame.display.update()
                 screen.blit(image, (x, y))
                 pygame.display.flip()
                elif event.key == ord ( "a" ) or event.key == pygame.K_LEFT:
                 if (x > 10):
                     x = x - 10;
                 screen.fill((black))
                 pygame.display.update()
                 screen.blit(image, (x, y))
                 pygame.display.flip()
                elif event.key == ord ( "d" ) or event.key == pygame.K_RIGHT:
                    if (x < 1930):
                     x = x + 10;
                    screen.fill((black))
                    pygame.display.update()
                    screen.blit(image, (x, y))
                    pygame.display.flip()
                
     
    print("Quit")
    pygame.display.quit()
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
