import pygame

pygame.init()

width = 800
height = 600

pygame.display.set_caption("Space Invaders Clone")

pygame. display.update()

player_ship_img = pygame.image.load("media/Lightning.png")

player_ship_width = 60
player_ship_height = 40
player_ship_img = pygame.transform.scale(player_ship_img, (player_ship width, player_ship_height))

class PlayerShip:
    def __init__(self):
        self.img = player_ship_img
        self.width = player_ship_width
        self.height = player_ship_height
        # start ship at center
        self.x = (width - self.width) // 2
        # Position ship just above the bottom
        self.y = height - self.height - 10
        # Adjust movement speed
        self.speed = 5

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

running = True
while running:
    # Game loop
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_ship.x -= player_ship.speed
            elif event.key == pygame.K_RIGHT:
                player_ship.x += player_ship.speed

    player_ship = PlayerShip()
    #screen clear
    screen.fill((0, 0, 0))
    #draw objects
    player_ship.draw()
    # update display
    pygame.display.update()


















# Todo
#Create the Player's Ship: Implement the player's ship and allow it to move left and right using keyboard input. Ensure that the ship stays within the game window boundaries.

#Create the Enemy Invaders: Design the enemy invaders and arrange them in rows and columns. Make them move left and right across the screen, and also move down when they hit the edge of the screen.

#Implement Shooting: Allow the player's ship to shoot bullets when the player presses a designated key. Handle collisions between bullets and enemy invaders.

#Implement Game Over and Scoring: Implement the game over condition, where the game ends if the enemy invaders reach the bottom of the screen. Create a scoring system to keep track of the player's score.

#Add Sound Effects: Use sound effects to enhance the gaming experience. Include sounds for shooting, enemy explosions, and player's ship movement.

#Polish and Refine: Test your game thoroughly and make any necessary adjustments to improve gameplay and overall user experience.

#Optional Enhancements: Once you have a basic clone working, you can add more features and enhancements to make your game unique. For example, you can introduce power-ups, different enemy types, or different levels of difficulty.