import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animations_speed = 0.15

        # print(str(self.animations['idle']))
        # self.image = self.animations['idle'][self.frame_index]
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        # Player moviment
        self.speed = 8
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = 0.8
        self.jump_speed = -16
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False


    def import_character_assets(self):
        character_path = '../graf/character/'
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fail':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1



        else:
            self.direction.x = 0

        if(keys[pygame.K_SPACE] and self.on_ground):
            self.jump()

    def apply_gravity(self):
        self.direction.y  += self.gravity
        self.rect.y += self.direction.y


    def jump(self):
        self.direction.y = self.jump_speed

    def get_status(self):
        if(self.direction.y < 0):
            self.status = 'salto'
        if(self.direction.y > 1):
            self.status = 'caio'
        else:
            if (self.direction.x != 0):
                self.status = 'run'
            else:
                self.status = 'idle'



    def update(self):
        self.get_input()
        self.get_status()
        # self.animate()
