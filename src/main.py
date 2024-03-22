#Julia Strong
#To Do
#write intro paragraph for line 43
#implement player/user, npc, and monster stats
# implement observation where there's location and user has to find something specific such as traps - likely would take intelligence and/or wisdom into consideration
# final goal
# win/lose scenarios
#locations
#quests
from graphics import draw_image2
from graphics import draw_image3
from graphics import book_was_clicked
from graphics import corner_was_clicked
from graphics import startImage
from graphics import draw_image1
from graphics import bookImage
#from graphics import something_was_clicked
from graphics import testImage
from graphics import firstChoice
from Player import name
import time
import pygame

pygame.init()

display_width = 500
display_height = 500
display_time = 5000

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(
    "RPG Fantasy Game with Text-Based, Graphic, and Clicker Elements")

draw_image1(startImage, 1, 1, display_time)

print(
    "Welcome to the RPG Fantasy Based Game with Text Based, Clicker Game, and Graphics Aspects!"
)
name = input("What is your character's name?" + "\n")
print("Welcome," + "\n" + name + "!" + "\n Click on the book to begin!")
print("")
time.sleep(4)
running = True
start_time = pygame.time.get_ticks()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and book_was_clicked(200, 400, 400, 495):
        pygame.display.update()
        pygame.display.flip()
        print("temporary intro paragraph for information")
        print("click on the bottom right corner of the book to continue")
        if event.type == pygame.MOUSEBUTTONDOWN and corner_was_clicked(320, 450, 350, 475):
          pygame.display.update()
          pygame.display.flip()
          print("test")
          print(
              "Click on the crystal ball to hear from a townsperson for additional information. Click on the backpack to see your inventory. Click on the window to continue on your journey."
          )

#pygame.quit()
