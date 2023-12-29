import random
import pygame
from  sys import exit
from random import randint, choice

class Panda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        panda_walk_1 = pygame.image.load('Panda Trail/graphics/Walk_1.png').convert_alpha()
        panda_walk_2 = pygame.image.load('Panda Trail/graphics/Walk_2.png').convert_alpha()
        self.panda_walk = [panda_walk_1, panda_walk_2]
        self.panda_walk_index = 0
        
        panda_jump_1 = pygame.image.load('Panda Trail/graphics/Jumping_1.png').convert_alpha()
        panda_jump_2 = pygame.image.load('Panda Trail/graphics/Jumping_2.png').convert_alpha()
        panda_jump_3 = pygame.image.load('Panda Trail/graphics/Jumping_3.png').convert_alpha()
        self.panda_jump = [panda_jump_1, panda_jump_2, panda_jump_3, panda_jump_2]
        self.panda_jump_index = 0
        
        panda_roll_1 = pygame.image.load('Panda Trail/graphics/Roll_1.png').convert_alpha()
        panda_roll_1 = pygame.transform.rotozoom(panda_roll_1, 0, 1.5)
        panda_roll_2 = pygame.image.load('Panda Trail/graphics/Roll_2.png').convert_alpha()
        panda_roll_2 = pygame.transform.rotozoom(panda_roll_2, 0, 1.5)
        panda_roll_3 = pygame.image.load('Panda Trail/graphics/Roll_3.png').convert_alpha()
        panda_roll_3 = pygame.transform.rotozoom(panda_roll_3, 0, 1.5)
        panda_roll_4 = pygame.image.load('Panda Trail/graphics/Roll_3.png').convert_alpha()
        panda_roll_4 = pygame.transform.rotozoom(panda_roll_4, -25, 1.5)
        panda_roll_5 = pygame.image.load('Panda Trail/graphics/Roll_3.png').convert_alpha()
        panda_roll_5 = pygame.transform.rotozoom(panda_roll_5, -75, 1.5)
        panda_roll_6 = pygame.image.load('Panda Trail/graphics/Roll_3.png').convert_alpha()
        panda_roll_6 = pygame.transform.rotozoom(panda_roll_6, -125, 1.5)
        panda_roll_7 = pygame.image.load('Panda Trail/graphics/Roll_3.png').convert_alpha()
        panda_roll_7 = pygame.transform.rotozoom(panda_roll_7, -175, 1.5)
        panda_roll_8 = pygame.image.load('Panda Trail/graphics/Roll_3.png').convert_alpha()
        panda_roll_8 = pygame.transform.rotozoom(panda_roll_8, -225, 1.5)
        panda_roll_9 = pygame.image.load('Panda Trail/graphics/Roll_3.png').convert_alpha()
        panda_roll_9 = pygame.transform.rotozoom(panda_roll_9, -275, 1.5)
        panda_roll_10 = pygame.image.load('Panda Trail/graphics/Roll_3.png').convert_alpha()
        panda_roll_10 = pygame.transform.rotozoom(panda_roll_10, -315, 1.5)
        self.panda_roll = [panda_roll_1, panda_roll_2, panda_roll_3, panda_roll_4, panda_roll_5, panda_roll_6, panda_roll_7, panda_roll_8, panda_roll_9, panda_roll_10, panda_roll_2, panda_roll_1]
        self.panda_roll_index = 0
        
        self.image = self.panda_walk[self.panda_walk_index]
        self.rect = self.image.get_rect(midbottom = (200,328))
        self.gravity = 0
        
        self.jump_sound = pygame.mixer.Sound('Panda Trail/audio/jump.mp3')
    
    def panda_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.bottom >= 328:
            self.gravity = -18
            self.jump_sound.play()
            
    def apply_gravity(self):
        keys = pygame.key.get_pressed()
        self.gravity += 0.7
        self.rect.y += self.gravity
        if self.rect.bottom >= 328 and not keys[pygame.K_DOWN]:
            self.rect.bottom = 328
        if keys[pygame.K_DOWN]:
            self.gravity = 0
            self.rect.bottom = 340
            
    def animation_state(self):
        keys = pygame.key.get_pressed()
        if self.rect.bottom < 328:
            self.panda_jump_index += 0.09
            if self.panda_jump_index >= len(self.panda_jump):
                self.panda_jump_index = 0
            if keys[pygame.K_UP]:
                self.panda_jump_index = 0
            self.image = self.panda_jump[int(self.panda_jump_index)]
            
        elif self.rect.bottom > 328:
            self.panda_roll_index += 0.1
            if self.panda_roll_index >= len(self.panda_roll):
                self.panda_roll_index = 0
            if not keys[pygame.K_DOWN]:
                self.panda_roll_index = 0
            self.image = self.panda_roll[int(self.panda_roll_index)]
            
        else:
            self.panda_walk_index += 0.1
            if self.panda_walk_index >= len(self.panda_walk):
                self.panda_walk_index = 0
            self.image = self.panda_walk[int(self.panda_walk_index)]
    
    def update(self):
        self.panda_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'butterfly':
            butterfly_1 = pygame.image.load('Panda Trail/graphics/Butterfly_1.png').convert_alpha()
            butterfly_2 = pygame.image.load('Panda Trail/graphics/Butterfly_2.png').convert_alpha()
            self.frames = [butterfly_1, butterfly_2]
            y_pos = 240
        else:
            bamboo = pygame.image.load('Panda Trail/graphics/bamboo.png').convert_alpha()
            bamboo = pygame.transform.rotozoom(bamboo, 0, 1.5)
            self.frames = [bamboo]
            y_pos = 328
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(850, 950), y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
        
def display_score():
    cTime = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = inline_font.render(f'Score: {cTime}', False, "White")
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return cTime

def collision_sprite():
    if pygame.sprite.spritecollide(panda.sprite, obstacle_group, False): #panda is a class
        obstacle_group.empty()
        lose_music.play(loops = 0)
        return False
    else:
        return True


pygame.init() #initializing pygame
screen = pygame.display.set_mode((800, 400))
game_active = False
clock = pygame.time.Clock()
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('Panda Trail/audio/october-rose.mp3')
bg_music.play(loops = -1) #loops forever
lose_music = pygame.mixer.Sound('Panda Trail/audio/game_over.mp3')

panda = pygame.sprite.GroupSingle()
panda.add(Panda())

obstacle_group = pygame.sprite.Group()

pygame.display.set_caption('Panda Trail')
font = pygame.font.Font('Panda Trail/fonts/karma/Karma Future.otf', 50)
inline_font = pygame.font.Font('Panda Trail/fonts/karma/Karma Suture.otf', 40)
instruction_font = pygame.font.Font('Panda Trail/fonts/karma/Karma Suture.otf', 30)

backdrop = pygame.image.load('Panda Trail/graphics/backdrop.png').convert_alpha()
ground = pygame.image.load('Panda Trail/graphics/ground.png').convert_alpha()
ground_width = ground.get_width()
tiles = 2
scroll = 0

face_surf = pygame.image.load('Panda Trail/graphics/face.png').convert_alpha()
face_surf = pygame.transform.rotozoom(face_surf, 0, 2) #gets new surface
face_rect = face_surf.get_rect(center = (400, 195))

#Writing
game_name = font.render('Panda Trail', False, "Black")
game_name_rect = game_name.get_rect(center = (400, 70))

game_instruc1 = instruction_font.render('Press space to continue', False, "Black")
game_instruc2 = instruction_font.render('Press the up arrow to jump', False, "Black")
game_instruc3 = instruction_font.render('Hold the down arrow to roll', False, "Black")
game_instruc_rect1 = game_instruc1.get_rect(center = (400, 290))
game_instruc_rect2 = game_instruc2.get_rect(center = (400, 330))
game_instruc_rect3 = game_instruc3.get_rect(center = (400, 370))

#Timer
obstacle_timer = pygame.USEREVENT + 1 #pygame might already have certain events so it avoids conflicts
pygame.time.set_timer(obstacle_timer, 1800) #triggers event

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit() #fully closes all code
    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)   
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['butterfly', 'bamboo', 'bamboo'])))

    if game_active:
        pygame.mixer.unpause()
        screen.blit(backdrop, (0, 0))
        
        for i in range(0, tiles):
            screen.blit(ground, (i*ground_width + scroll, 20))
        
        # scrolling ground
        scroll -= 6
        if scroll < -ground_width:
            scroll = 0
        
        pygame.draw.line(screen, 'Black', (264, 48), (533, 48), 68)
        score = display_score()
        
        panda.draw(screen)
        panda.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        game_active = collision_sprite()
     
    else:
        screen.fill((54, 143, 79))
        screen.blit(face_surf, face_rect)
        panda_gravity = 0
        
        score_message = inline_font.render(f'Your score: {score}', False, "Black")
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_name, game_name_rect)
        
        if score == 0:
            screen.blit(game_instruc1, game_instruc_rect1)
            screen.blit(game_instruc2, game_instruc_rect2)
            screen.blit(game_instruc3, game_instruc_rect3)
        else:
            screen.blit(score_message, score_message_rect)
            
    pygame.display.update()
    clock.tick(60) #caps it at 60 fps
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
