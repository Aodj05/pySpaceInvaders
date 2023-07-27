import pygame
import random

pygame.init()

width = 800
height = 600


# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BULLET_COLOR = (255, 255, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders Clone")

clock = pygame.time.Clock()

pygame.display.update()

pygame.mixer.init()


player_ship_img = pygame.image.load("media/Lightning.png")

player_ship_width = 60
player_ship_height = 40
player_ship_img = pygame.transform.scale(player_ship_img, (player_ship_width, player_ship_height))

invader1_img = pygame.image.load("media/Dove.png")

invader1_width = 50
invader1_height = 40
invader1_img = pygame.transform.scale(invader1_img, (invader1_width, invader1_height))

explosion_sound = pygame.mixer.Sound("media/explosion.wav")
fastinvader1_sound = pygame.mixer.Sound("media/fastinvader1.wav")
fastinvader2_sound = pygame.mixer.Sound("media/fastinvader2.wav")
fastinvader3_sound = pygame.mixer.Sound("media/fastinvader3.wav")
fastinvader4_sound = pygame.mixer.Sound("media/fastinvader4.wav")
invaderkilled_sound = pygame.mixer.Sound("media/invaderkilled.wav")
shoot_sound = pygame.mixer.Sound("media/shoot.wav")
ufopitch_sound = pygame.mixer.Sound("media/ufo_lowpitch.wav")

shooting_condition = False
invader_destroyed = False
player_hit = False

#replace consitions to detect events
if shooting_condition:
    shoot_sound()

if invader_destroyed:
    invaderkilled_sound()

if player_hit:
    explosion_sound()

# half volume sound effects
shoot_sound.set_volume(0.5)
invaderkilled_sound.set_volume(0.5)
explosion_sound.set_volume(0.5)

class Invader1:
    def __init__(self, x, y):
        self.img = invader1_img
        self.width = invader1_width
        self.height = invader1_height
        self.x = x
        self.y = y
        # Adjust invader's movement speed
        self.speed = 2

    def draw(self) :
        screen.blit(self.img, (self.x, self.y))

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

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 3
        self.speed = 4

def destroy_invader(invader):
    global score
    score += 10

def display_score():
    font = pygame.font.Font(None, 42)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def check_game_over():
    global lives
    if lives <=0:
        return True
    return False

def display_game_over():
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("GAME OVER", True, RED)
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2))

def check_bullet_collision(bullets, invaders):
    for bullet in bullets:
        for invader in invaders:
            if bullet.y <= invader.y + invader1_height and invader.x <= bullet.x <= invader.x + invader1_width:
                # Bullet collided with an invader
                destroy_invader(invader)
                bullets.remove(bullet)
                break


score = 0

player_bullets = []
invader_bullets = []

invader_dir = 1
invader_speed = 2

invader_imgs = [pygame.image.load("media/Dove.png"), pygame.image.load("media/Dove.png")]
invader_animation_time = 500
current_animation_frame = 0
last_animation_time = pygame.time.get_ticks()

# Grid of the invaders
invader_rows = 5
invader_cols = 10

invaders = []
for row in range(invader_rows):
    for col in range(invader_cols):
        #spacing between invaders
        invader_x = col * (invader1_width + 10)
        invader_y = row * (invader1_height + 10)
        invaders.append(Invader1(invader_x, invader_y,))

score = 0
lives = 3
game_over = False

invader_bullet_interval = 2000  # 2000 milliseconds (2 seconds)
last_bullet_time = pygame.time.get_ticks()

def display_lives():
    font = pygame.font.Font(None, 42)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(lives_text, (10, 50))

player_ship = PlayerShip()

running = True
while running:
    for invader in invaders:
        invader.x += invader_speed * invader_dir

    # check window boundaries
    for invader in invaders:
        if invader.x <= 0 or invader.x + invader1_width >= width:
            invader_dir *= -1
            for inv in invaders:
                inv.y += 10


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
            if event.key == pygame.K_SPACE:
                shooting_condition = True
                player_bullets.append(Bullet(player_ship.x + player_ship.width // 2, player_ship.y))
        #filter off-screen bullets
    player_bullets = [bullet for bullet in player_bullets if bullet.y > 0]
    invader_bullets = [bullet for bullet in invader_bullets if bullet.y < height]

    for bullet in player_bullets:
        bullet.y -= bullet.speed

    for bullet in invader_bullets:
        bullet.y += bullet.speed


    #screen clear
    screen.fill((0, 0, 0))

    # draw invader objects
    for invader in invaders:
        invader.draw()
    
    current_time = pygame.time.get_ticks()
    if current_time - last_animation_time >= invader_animation_time:
        last_animation_time = current_time
        current_animation_frame = (current_animation_frame + 1) % len(invader_imgs)

    for invader in invaders:
        invader.img = invader_imgs[current_animation_frame]

    # Update and draw the player score
    display_score()

    

    #check for game over
    if check_game_over():
        game_over = True

    if game_over:
        display_game_over()
    else:
        display_lives()

player_ship = PlayerShip()

if current_time - last_bullet_time >= invader_bullet_interval:
    last_bullet_time = current_time
    random_invader = random.choice(invaders)
    invader_bullets.append(Bullet(random_invader.x + invader1_width // 2, random_invader.y + invader1_height))
    
    check_bullet_collision(player_bullets, invaders)
    check_bullet_collision(invader_bullets, [player_ship])  # Check collision with player ship


    #draw objects
    player_ship.draw()
    for bullet in player_bullets:
        pygame.draw.rect(screen, BULLET_COLOR, (bullet.x, bullet.y, bullet.width, bullet.height))

    for bullet in invader_bullets:
        pygame.draw.rect(screen, BULLET_COLOR, (bullet.x, bullet.y, bullet.width, bullet.height))
    # update display
    pygame.display.update()

    clock.tick(60)

pygame.mixer.quit()
pygame.quit()

















# Todo










#Polish and Refine: Test your game thoroughly and make any necessary adjustments to improve gameplay and overall user experience.

#Optional Enhancements: Once you have a basic clone working, you can add more features and enhancements to make your game unique. For example, you can introduce power-ups, different enemy types, or different levels of difficulty.