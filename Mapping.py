import pygame
from test import *
from subprocess import call

def write_to_file():
    text_file = open("Mapper.ino", "w")
    lines = leonardo.split("\n")
    for i in lines:
        if i in points:
            index = points.index(i)
            index_2 = lines.index(i)
            lines[index_2] = string[index]
        if i == "[11]":
            index_2 = lines.index(i)
            lines[index_2] = "100"
    print('\n'.join(lines))
    text_file.write('\n'.join(lines))
    text_file.close()

def processkeys():
    for i in keys:
        # A-Z, a-z
        if (i >= 65 and i <= 90) or (i >= 97 and i <= 122):
            string.append("Keyboard.press('"+pygame.key.name(i)+"');")
        else:
            # map the other keys in the keyboard
            string.append("Keyboard.press("+mapp.get(i)+");")

# wait for the user to press a key and return the keycode
def wait_for_key():
    e = pygame.event.wait()
    while e.type != pygame.KEYDOWN:
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            return pygame.K_ESCAPE
    return e.key

# show the pygame window
pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Key Mapping")
font = pygame.font.Font(None, 36)
keys = []
string = []

# set image coordinates
x = 0
y = 0
s = ["left_top", "up", "down", "left", "right", "start", "right_top", "W", "A", "S", "D"]
i = 0
# loop around until the user presses escape or Q
looping = True
while looping:
    img_logo = pygame.image.load(s[i]+".jpg")
    # fill the screen in white
    screen.fill((255, 255, 255))
    i += 1
    # blit copies an image onto the screen
    screen.blit(img_logo, (-10, -100))
    text = font.render("Press key to Map controller", True, (0, 0, 0))
    screen.blit(text, (0, 0))
    pygame.display.flip()
    # wait for a key to be pressed
    key = wait_for_key()
    keys.append(key)

    # stop looping if the user presses Q or escape
    if key == pygame.K_ESCAPE or i == 11:
        screen.fill((255, 255, 255))
        text = font.render("Press Enter to set keys to controller", True, (0, 0, 0))
        screen.blit(text, (0, 0))
        pygame.display.flip()
        key = wait_for_key()
        if(key == 13):
            looping = False
        else:
            continue
    #print(key)
    #print(pygame.key.name(key))
    # move the image
    #elif key == pygame.K_UP:
    #    y -= 10
    #elif key == pygame.K_DOWN:
    #    y += 10
processkeys()
write_to_file()
pygame.quit()
