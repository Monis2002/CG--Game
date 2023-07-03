
import pygame
from sys import exit
from random import randint,choice
"""
I have done this by two diff Method
1)Original code is by:- Class Method
2)Comments are :- Functional Method

This is the Reason for code to be so long

"""

pygame.init()
screen=pygame.display.set_mode((800,400))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk1 = pygame.image.load("Image/player_walk_1.png").convert_alpha()
        player_walk2 = pygame.image.load("Image/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load("Image/jump.png").convert_alpha()

        self.image=self.player_walk[self.player_index]
        self.rect=self.image.get_rect(midbottom=(80,280))
        self.gravity=0
        self.jump_sound=pygame.mixer.Sound("audio/audio_jump.mp3")


    def input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom>=280:
            self.gravity=-20
            self.jump_sound.play()
            self.jump_sound.set_volume(0.5)

    def animation(self):
        if self.rect.bottom<280:
            self.image=self.player_jump
        else:
            self.player_index+=0.1
            if self.player_index>=len(self.player_walk):
                self.player_index=0
            self.image=self.player_walk[int(self.player_index)]


    def gravity_player(self):
        self.gravity+=1
        self.rect.y+=self.gravity
        if self.rect.bottom>=280:
            self.rect.bottom=280

    def update(self):
        self.input()
        self.gravity_player()
        self.animation()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type=="fly":
            fly_frame_1 = pygame.image.load("Image/Fly1.png")
            fly_frame_2 = pygame.image.load("Image/Fly2.png")
            self.frame = [fly_frame_1, fly_frame_2]
            self.y_pos=140
        else:
            snail_frame_1 = pygame.image.load("Image/snail1.png")
            snail_frame_2 = pygame.image.load("Image/snail2.png")
            self.frame = [snail_frame_1, snail_frame_2]
            self.y_pos=280

        self.frame_index=0
        self.image=self.frame[self.frame_index]
        self.rect=self.image.get_rect(midbottom=((randint(900,1100)),self.y_pos))

    def animation_state(self):
        self.frame_index+=0.1
        if self.frame_index>=len(self.frame):
            self.frame_index=0
        self.image=self.frame[int(self.frame_index)]

    def update(self):
        t = int(pygame.time.get_ticks() * 10 ** (-3)) - int(s_time)
        self.animation_state()
        if t<randint(10,20):
            self.rect.x-=6
        elif t<randint(20,30):
            self.rect.x-=10
        elif t<randint(30,50):
            self.rect.x-=15
        else:
            self.rect.x-=22

        self.destroy()

    def destroy(self):
        if self.rect.x<=-100:
            self.kill()



def display_score():

    curent_time=int(pygame.time.get_ticks()*10**(-3))-int(s_time)
    score_surf=text_font.render(f'Score: {curent_time}',False,(64,64,64))
    score_rect=score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    return curent_time

def obstacle_movement(obstacle_list):
    t=int(pygame.time.get_ticks()*10**(-3))-int(s_time)

    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if t<randint(10,20):
                obstacle_rect.x-=5
            elif t<randint(20,30):
                obstacle_rect.x-=9
            elif t<randint(30,40):
                obstacle_rect.x-=14
            else:
                obstacle_rect.x-=22
            if obstacle_rect.bottom==280:
                screen.blit(snail_surf,obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)


        obstacle_list=[i for i in obstacle_list if i.x>-100]
        return obstacle_list
    else:
        return []

def colision(player,obstacle):
    if obstacle:
        for obstacle_rect in obstacle:
            if player.colliderect(obstacle_rect):
                return False
    return True

def collison_sprit():
    if pygame.sprite.spritecollide(player.sprite,obstacle_class,False):
        obstacle_class.empty()
        return False
    else:
        return True

def player_animination():
    global player_surf,player_index
    if player_rect.bottom<280:
        player_surf=player_jump
    else:
        player_index+=0.1
        if player_index>=len(player_walk):
            player_index=0
        player_surf=player_walk[int(player_index)]


player=pygame.sprite.GroupSingle()
player.add(Player())

obstacle_class=pygame.sprite.Group()

pygame.display.set_caption("Monis's Game")
clock=pygame.time.Clock()
text_font=pygame.font.Font("Font/Pixeltype.ttf",50)
game_active=False

sky=pygame.image.load("Image/Sky1.png")
ground=pygame.image.load("Image/ground1.png")

#score_surf=text_font.render("Score",False,(64,64,64))
#score_rect=score_surf.get_rect(center=(400,50))

#Snail
snail_frame_1=pygame.image.load("Image/snail1.png")
snail_frame_2=pygame.image.load("Image/snail2.png")
snail_frame=[snail_frame_1,snail_frame_2]
snail_frame_index=0
snail_surf=snail_frame[snail_frame_index]

#Fly
fly_frame_1=pygame.image.load("Image/Fly1.png")
fly_frame_2=pygame.image.load("Image/Fly2.png")
fly_frame=[fly_frame_1,fly_frame_2]
fly_frame_index=0
fly_surf=fly_frame[fly_frame_index]

obstacle_list=[]



player_walk1=pygame.image.load("Image/player_walk_1.png").convert_alpha()
player_walk2=pygame.image.load("Image/player_walk_2.png").convert_alpha()
player_walk=[player_walk1,player_walk2]
player_index=0
player_jump=pygame.image.load("Image/jump.png").convert_alpha()

player_surf=player_walk[player_index]
player_rect=player_surf.get_rect(midbottom=(80,280))
player_gravity=0

#Intro Screen
player_stand=pygame.image.load("Image/player_stand.png")
player_stand=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand.get_rect(center=(400,200))
player_name=text_font.render("Monis",False,(111,196,169))
player_name_rect=player_name.get_rect(center=(400,95))
space_start=text_font.render("Press Space to Run",False,(111,196,169))
space_start_rect=space_start.get_rect(center=(400,340))
s_time=0
score=0

#Timer
obstacle_timer=pygame.USEREVENT+1
pygame.time.set_timer(obstacle_timer,1500)

snail_timer=pygame.USEREVENT +2
pygame.time.set_timer(snail_timer,500)

fly_timer=pygame.USEREVENT+ 3
pygame.time.set_timer(fly_timer,200)

#Sound
bg_sound=pygame.mixer.Sound("audio/music.wav")
bg_sound.play(loops=-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity=-20

            if event.type==pygame.KEYDOWN:
                if player_rect.bottom==280:
                    if event.key==pygame.K_SPACE:
                        player_gravity=-20



        else:

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_active=True
                    s_time=pygame.time.get_ticks()*10**(-3)

        if game_active:
            if event.type==obstacle_timer:

                obstacle_class.add(Obstacle(choice(["fly","snail","snail"])))
                #if randint(0,2):
                 #   obstacle_list.append(snail_surf.get_rect(bottomright=((randint(900,1100)),280)))
                #else:
                 #   obstacle_list.append(fly_surf.get_rect(bottomright=((randint(900,1100)),190)))
            if event.type==snail_timer:
                if snail_frame_index==0:
                    snail_frame_index=1
                else:
                    snail_frame_index=0
                snail_surf=snail_frame[snail_frame_index]

            if event.type==fly_timer:
                if fly_frame_index==0:
                    fly_frame_index=1
                else:
                    fly_frame_index=0
                fly_surf=fly_frame[fly_frame_index]


    if game_active:
        screen.blit(sky,(0,0))
        screen.blit(ground,(0,280))

        score=display_score()

       # pygame.draw.rect(screen,"#c0e8ec",score_rect)
        #pygame.draw.rect(screen,"#c0e8ec",score_rect,10)
        #screen.blit(score_surf, score_rect)

       #Snail:-
        #snail_rect.x-=5
        #if score>8: snail_rect.x-=8

        #if snail_rect.right<0: snail_rect.left=800
        #screen.blit(snai1_surf,snail_rect)

        #Player:-
        #player_gravity+=1
        #player_rect.y+=player_gravity

        #if player_rect.bottom>=280:
         #   player_rect.bottom=280

        #if player_rect.top<0:
         #   player_rect.top=0

        #player_animination()
        #screen.blit(player_surf,player_rect)

        #By using Class
        player.draw(screen)
        player.update()

        obstacle_class.draw(screen)
        obstacle_class.update()



        #Obstacle Movement
        obstacle_movement(obstacle_list)

        #Collison:-
        game_active=collison_sprit()
        #game_active=colision(player_rect,obstacle_list)



    else:
        obstacle_list.clear()
        player_rect.midbottom=(80,280)
        player_gravity=0

        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(player_name,player_name_rect)
        score_massage=text_font.render(f"Your score: {score}",False,(111,196,169))
        score_massage_rect=score_massage.get_rect(center=(400,340))
        if score==0:
            screen.blit(space_start,space_start_rect)
        else:
            screen.blit(score_massage,score_massage_rect)


    pygame.display.update()
    clock.tick(60)