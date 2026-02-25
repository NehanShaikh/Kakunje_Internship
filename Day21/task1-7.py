# Custom Game Window
import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Intern Game Window")

screen.fill((100, 150, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()


# Shape Playground
import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shape Playground")

white = (255, 255, 255)
screen.fill(white)

pygame.draw.rect(screen, (0, 0, 255), (100, 100, 200, 100))
pygame.draw.circle(screen, (255, 0, 0), (500, 200), 70)
pygame.draw.rect(screen, (0, 255, 0), (300, 350, 100, 100))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

# Detect Multiple Keys
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Moving Backward")
            if event.key == pygame.K_RIGHT:
                print("Moving Forward")
            if event.key == pygame.K_UP:
                print("Jump")
            if event.key == pygame.K_DOWN:
                print("Crouch")

pygame.quit()

# Sound Player with Text
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sound Player")

gray = (150, 150, 150)
screen.fill(gray)

font = pygame.font.SysFont(None, 50)
text = font.render("Playing...", True, (0, 0, 0))
screen.blit(text, (200, 180))

pygame.mixer.music.load("game_over.wav")
pygame.mixer.music.play()

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


# Display Custom Text
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
screen.fill((0, 0, 0))

font = pygame.font.SysFont(None, 40)

text1 = font.render("Nehan Shaikh", True, (0, 255, 0))
text2 = font.render("AI & ML Engineering", True, (0, 255, 0))

screen.blit(text1, (200, 250))
screen.blit(text2, (200, 300))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


# Multi Audio Player
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Multi Sound Player")

white = (255, 255, 255)
screen.fill(white)

pygame.draw.circle(screen, (255, 0, 0), (300, 200), 60)

sound1 = pygame.mixer.Sound("subway_surfers.mp3")
sound1.play(5)

pygame.mixer.music.load("glass_breaking.mp3")
pygame.mixer.music.play(-1)

game_over = pygame.mixer.Sound("game_over.wav")
game_over.play()

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


# Simple Mini Game Example
import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mini Game")

white = (255, 255, 255)
blue = (0, 0, 255)

x = 100
y = 250
speed = 5

font = pygame.font.SysFont(None, 40)

running = True
while running:
    screen.fill(white)

    text = font.render("Use Arrow Keys", True, (0, 0, 0))
    screen.blit(text, (300, 50))

    pygame.draw.rect(screen, blue, (x, y, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    pygame.display.update()

pygame.quit()
