import pygame, numpy, random, sys


# Class for location of icons
class IconLocation(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, icon):
        super().__init__()
        self.image = pygame.image.load("Assets/beer_mini.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def set_image(self, image):
        self.image = image

# Class for spin animation
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.spin_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load("Assets/blank_mini.png"))
        self.sprites.append(pygame.image.load("Assets/beer_mini.png"))
        self.sprites.append(pygame.image.load("Assets/vodka_mini.png"))
        self.sprites.append(pygame.image.load("Assets/peppermint_mini.png"))
        self.sprites.append(pygame.image.load("Assets/tequila_mini.png"))
        self.sprites.append(pygame.image.load("Assets/jagermeister_mini.png"))
        self.sprites.append(pygame.image.load("Assets/group_mini.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect = [pos_x,pos_y]

    def spin(self):
        self.spin_animation = True

    def update(self,speed):
        if self.spin_animation == True:
            self.current_sprite += speed
            if int (self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0 
                self.spin_animation = False

        self.image = self.sprites[int(self.current_sprite)]

def start():
    global total_coins
    # Generate three random icon
    rand_icons = numpy.random.choice(icons, 3, p=icons_proba)
    # Draw the random icons on the correct location
    loc_left.set_image(icon_dict[rand_icons[0]])
    loc_middle.set_image(icon_dict[rand_icons[1]])
    loc_right.set_image(icon_dict[rand_icons[2]])

    # Reward if there are three ientical icons
    if rand_icons[0] == rand_icons[1] == rand_icons[2]:
        # Get reward from a dict
        coins = icon_reward_dict[rand_icons[0]]
        total_coins += coins

# Setup the window
pygame.init()
clock = pygame.time.Clock()
width = 1000
height = 667
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drink Machine v1.0")
logo = pygame.image.load('Assets/group.png')
pygame.display.set_icon(logo)


# Load background image
background = pygame.image.load('Assets/bg.png')
police_total_coins = pygame.font.SysFont("Impact", 50)
police_menu = pygame.font.SysFont("Impact", 25)

# Load location icons
# No equation to do location 
height_location = height / 2 - 135
Location = pygame.sprite.Group()
loc_left = IconLocation(200, height_location, "Bier")
loc_middle = IconLocation(415, height_location, "Vodka")
loc_right = IconLocation(630, height_location, "Pfeffi")

# Group location
Location.add(loc_left)
Location.add(loc_middle)
Location.add(loc_right)

# Location of icons menu
Location_menu = pygame.sprite.Group()
first_loc = IconLocation(20, 400, "Bier")
second_loc = IconLocation(20, 500, "Vodka")
third_loc = IconLocation(320, 400, "Pfeffi")
fourth_loc = IconLocation(320, 500, "Tequila")
fifth_loc = IconLocation(615, 400, "Jäger")
sixth_loc = IconLocation(615, 500, "Gruppe")

# icons 
Bier = pygame.image.load("Assets/beer_win_mini.png")
Vodka = pygame.image.load("Assets/vodka_win_mini.png")
Pfeffi = pygame.image.load("Assets/peppermint_win_mini.png")
Tequila = pygame.image.load("Assets/tequila_win_mini.png")
Jäger = pygame.image.load("Assets/jagermeister_win_mini.png")
Gruppe = pygame.image.load("Assets/group_win_mini.png")
Blank = pygame.image.load("Assets/blank_mini.png")

    # Group location_menu
    #Location_menu.add(first_loc)
    #Location_menu.add(second_loc)
    #Location_menu.add(third_loc)
    #Location_menu.add(fourth_loc)
    #Location_menu.add(fifth_loc)
    #Location_menu.add(sixth_loc)

# Coins of the player
total_coins = 500

# Stock the social media icons in list
icons = ["Bier", "Vodka", "Pfeffi", "Tequila", "Jäger", "Gruppe"]
# Probability of evry icon to appear
icons_proba = [0.5, 0.05, 0.30, 0.05, 0.05, 0.05]

# Stock on dict every icon with that reward
icon_reward_dict = {
    "Bier": 25,
    "Vodka": 20,
    "Pfeffi": 15,
    "Tequila": 35,
    "Gruppe": 5,
    "Jäger": 200    
}

# Stock every icon associate to a image
icon_dict = {
    "Bier": pygame.image.load("Assets/beer_mini.png"),
    "Vodka": pygame.image.load("Assets/vodka_mini.png"),
    "Pfeffi": pygame.image.load("Assets/peppermint_mini.png"),
    "Tequila": pygame.image.load("Assets/tequila_mini.png"),
    "Jäger": pygame.image.load("Assets/jagermeister_mini.png"),
    "Gruppe": pygame.image.load("Assets/group_mini.png")
}

# Create sprites and groups
moving_sprites = pygame.sprite.Group()
player1 = Player(200,height_location)
player2 = Player(415, height_location)
player3 = Player(630, height_location)
moving_sprites.add(player1)
moving_sprites.add(player2)
moving_sprites.add(player3)

# Main loop
run = True
while run:
    # Draw the bg image
    screen.blit(background, (0, 0))
    # Draw icon image
    Location.draw(screen)
    # Display of win icons
    screen.blit(Bier, (190, 470))
    screen.blit(Vodka, (190, 570))
    screen.blit(Pfeffi, (405, 470))
    screen.blit(Tequila, (405, 570))
    screen.blit(Jäger, (625, 470))
    screen.blit(Gruppe, (625, 570))
    # Print the coins of the player
    text = police_total_coins.render("Total "+str(total_coins)+"$", True, (255, 215, 0))
    screen.blit(text, (400, 25))
    # Print menu reward for each icon
    be_menu = police_menu.render("=   +25$", True, (255, 255, 255))
    screen.blit(be_menu, (295, 480))
    vo_menu = police_menu.render("=  +20$", True, (255, 255, 255))
    screen.blit(vo_menu, (295, 575))
    pf_menu = police_menu.render("=  +15$", True, (255, 255, 255))
    screen.blit(pf_menu, (510, 480))
    te_menu = police_menu.render("=  +35$", True, (255, 255, 255))
    screen.blit(te_menu, (510, 575))
    ja_menu = police_menu.render("=  +200$", True, (255, 255, 255))
    screen.blit(ja_menu, (735, 480))
    gr_menu = police_menu.render("=  +5$", True, (255, 255, 255,))
    screen.blit(gr_menu, (735, 575))




    # Draw icon image of the menu
    Location_menu.draw(screen)
    # Update screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
        # Chek if key is pressed
        if event.type == pygame.KEYDOWN:
            player1.spin()
            player2.spin()
            player3.spin()
            # 1 click = 1 try ====> -15$
            if total_coins >= 15:
                total_coins -= 15
                start()

    # Drawing
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    pygame.display.flip()
    clock.tick(20)