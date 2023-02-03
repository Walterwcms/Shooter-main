import pygame
from tiles import Tile
from apple import Apple
from settings import tile_size, screen_width, apple_size, enemi_size
from player import Player


class Level:
    def __init__(self,level_data,surface):

        #level setup
        self.display_surface = surface
        self.setup_leve(level_data)
        self.word_shift = 0

    def setup_leve(self,layout):
        self.tiles = pygame.sprite.Group()
        self.apple = pygame.sprite.GroupSingle()

        self.player = pygame.sprite.GroupSingle()
        self.enemi = pygame.sprite.GroupSingle()



        #------------------renderizar o ambiente-----------------
        for row_index,row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size


                if(cell == 'X'):
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)

                # ---------------Perssonagem do jogo--------------
                if (cell == 'P'):
                    player_sprice = Player((x, y))
                    self.player.add(player_sprice)
                # ------------------------------------------------


                #-----------------apple----------------------------
                if (cell == 'A'):
                    apple = Apple((x, y), apple_size)
                    self.apple.add(apple)
                #--------------------------------------------------


        #--------------------------------------------------------




    #--------------------------------------SCROOL SCREEN QUANDO O PLAYER MOVIMENTAR-------------------------
    def scrooll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if(player_x < (screen_width / 4) and direction_x < 0):
            self.word_shift = 8
            player.speed = 0
        elif (player_x > (screen_width -(screen_width / 4) ) and direction_x > 0):
            self.word_shift = -8
            player.speed = 0
        else:
            self.word_shift = 0
            player.speed = 8

    #----------------------------------------------------------------------------------------------------------




    #----------------------------colisao no chao-----------------------------------------------------------
    def horizontal_moviment_collision(self):
        player = self.player.sprite
        enemi = self.enemi.sprite

        player.rect.x += player.direction.x * player.speed #movimento horizontal


        #------------- procurar a colisa
        for sprite in self.tiles.sprites():
            if(sprite.rect.colliderect(player.rect)):

                if(player.direction.x < 0):
                    player.rect.left = sprite.rect.right
                if (player.direction.x > 0):
                    player.rect.right = sprite.rect.left



    def vertical_movimet_collision(self):
        player = self.player.sprite
        enemi = self.player.sprite

        enemi.apply_gravity()

        for sprite in self.tiles.sprites():
            if (sprite.rect.colliderect(player.rect)):
                if(player.direction.y > 0):
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground=True
                if(player.direction.y < 0):
                    player.direction.y = 0
                    player.rect.top = sprite.rect.bottom
                    player.on_ceiling = True


            if(player.on_ground and player.direction.y < 0 or player.direction.y > 1):
                player.on_ground = False

    #----------------------------------------------------------------------------------------------------------



    def run(self):
        #--------tiles
        self.tiles.update(self.word_shift)
        self.tiles.draw(self.display_surface)

        self.apple.update(self.word_shift)
        self.apple.draw(self.display_surface)

        self.scrooll_x()



        #---------player
        self.player.update()
        self.horizontal_moviment_collision()
        self.vertical_movimet_collision()
        self.player.draw(self.display_surface)





