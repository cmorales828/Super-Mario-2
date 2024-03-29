import sound_cache
import pygame
import math
from objects.parents.player_parent import Player
from objects.tileset import Tileset

# Mario Object
class Mario(Player):
    def __init__(self, x, y):
        super().__init__(x, y)

        # gravity base
        self.gravity_base = 0.4
        self.gravity_alt = 0.1

        self.gravity = self.gravity_base
        
        self.acc = 0.05
        self.accskid = 0.125
        self.deccel = 0.1
        self.deccskid = 0.05
        
        self.jumpstr = 3.85
        self.vel_x_min = 1.25
        self.vel_x_max = 2.5
        self.max_vel_x = self.vel_x_min

        self.image_index = 0
        self.jumping = 0
        self.skidding = False
        self.crouching = False
        self.dead = False
        # sprites
        self.small_mario = Tileset("player/small_mario.png", 16, 16)
        self.small_mario.offset = (0, 16)
        self.super_mario = Tileset("player/big_mario.png", 16, 32)
        self.life = 100
        self.iframes = 0
        #
        self.current_sprite = self.small_mario
        self.standard_rect = pygame.Rect(0, 0, 14, 30)
        self.crouch_rect = pygame.Rect(0, 0, 14, 14)

        self.jumped = False

    def wall_collide(self, gameobject):
        if not gameobject.is_phaseable:
            return super().wall_collide(gameobject)
        elif gameobject.is_harmful and not gameobject.dead \
        and self.rect.colliderect(gameobject.rect) \
        and self.rect.bottom > gameobject.rect.centery:
            self.damage()
        return False
    
    def damage(self):
        if not self.dead and self.iframes <= 0:
            self.life -= 1
            if self.life > 0:
                sound_cache.HURT.play()
                self.iframes = 120
            else:
                sound_cache.DIE.play()
                self.iframes = 30
                self.dead = True
                self.ground = False
                self.jumping = 0
                self.vel_y = -3.5
                self.vel_x = 0
                self.gravity = 0.1
        
    def ceiling_collide(self, gameobject):
        if not gameobject.is_phaseable \
        and not gameobject.is_block:
            return super().ceiling_collide(gameobject)
        elif gameobject.is_block and self.rect.colliderect(gameobject.rect) \
        and self.rect.top >= gameobject.rect.bottom - 4:
            if gameobject.bump:
                super().ceiling_collide(gameobject)
            else:
                self.bump_ceil(gameobject)
        return False
    
    def floor_collide(self, gameobject):
        if not gameobject.is_phaseable:
            return super().floor_collide(gameobject)
        # ENEMY COLLISION HANDLING HERE
        if self.rect.colliderect(gameobject.rect) and self.vel_y > 0 \
        and (self.rect.bottom >= gameobject.rect.top \
        and self.rect.bottom <= gameobject.rect.top + 4) and not gameobject.dead:
            self.vel_y = -4.1
            self.y -= 1
            self.jumping = True
            self.jumped = True
            self.variable_jumping()
            gameobject.kill()
        return False

    def bump_floor(self, floor):
        # if isinstance(floor, Enemy):
            # return
        return super().bump_floor(floor)
    
    def bump_ceil(self, ceiling):
        if ceiling.is_block and not ceiling.bump:
            ceiling.vel_y = -2
            ceiling.bump = True
            ceiling.physics_update()
            self.y += 1
        return super().bump_ceil(ceiling)

    def variable_jumping(self):
        if self.jumping >= 1 and not self.ground:
            if self.jumping == 1 and self.vel_y < -1:
                self.jumping = (not pygame.key.get_pressed()[pygame.K_SPACE]) + 1
                self.gravity = self.gravity_alt
            else:
                self.jumping = 2
                self.gravity = self.gravity_base
        else: 
            self.jumping = 0

    def physics_update(self):
        if not self.dead or (self.dead and self.iframes <= 0):
            return super().physics_update()

    def update(self, map, objects):
        # i frame decrease
        if self.iframes > 0:
            self.iframes -= 1

        if self.dead:
            return

        keys = pygame.key.get_pressed()

        # crouching 
        if self.ground and self.current_sprite != self.small_mario:
            if keys[pygame.K_s]:
                self.crouching = True
            else:
                self.crouching = False
        elif self.current_sprite == self.small_mario:
            self.crouching = False

        move = keys[pygame.K_d] - keys[pygame.K_a]
        sign_of = math.copysign(1, move)
        if abs(move) > 0 and ((not self.crouching) or (not self.ground)):
            if sign_of == math.copysign(1, self.vel_x):
                self.skidding = False
                self.vel_x += move * self.acc
                if self.ground:
                    self.dir = sign_of
            else:
                self.vel_x += move * self.accskid
                if (abs(self.vel_x) > self.vel_x_min):
                    self.skidding = True
        elif self.ground: # decceleration
            self.vel_x = max(0, abs(self.vel_x) - self.deccel) * math.copysign(1, self.vel_x)
            if self.vel_x < self.deccel and self.vel_x > -self.deccel:
                self.vel_x = 0
        
        if self.ground:
            self.max_vel_x = self.vel_x_min
            if keys[pygame.K_LSHIFT]:
                self.max_vel_x = self.vel_x_max
        
        # speed cap only in one direction as per suggestion of hollyer
        if math.copysign(1, self.vel_x) == self.dir:
            self.vel_x = max(-self.max_vel_x, min(self.vel_x, self.max_vel_x))

        # get the current sprite hitbox
        self.current_sprite = self.small_mario if self.life <= 1 else self.super_mario
        # if you want to add custom states you can cross check powerups with sprite being super mario here
        self.rect = self.standard_rect if ((not self.crouching) and (self.current_sprite != self.small_mario)) else self.crouch_rect
        self.offset_y = 8 if self.rect == self.standard_rect else 16

        super().update(map, objects)
        # print(self.rect)

        if self.ground:
            if not self.jumped \
            and keys[pygame.K_SPACE]:
                if self.life < 1:
                    sound_cache.JUMP.play()
                else:
                    sound_cache.JUMP_ALT.play()
                self.ground = False
                self.vel_y = -(self.jumpstr + (abs(self.vel_x) / 7.5))
                self.jumping = 1
                self.jumped = True
            elif self.jumped and not keys[pygame.K_SPACE]:
                self.jumped = False
        self.variable_jumping()

        # animation control
        if self.crouching or self.dead:
            self.image_index = 6
        else:
            if self.jumping == 0 or self.ground:
                if self.skidding and abs(self.vel_x) > 0.01:
                    self.image_index = 4
                else:
                    if abs(self.vel_x) > 0:
                        self.image_index += (0.065 + abs(self.vel_x) / 7.5) / 2
                        if self.image_index > 4:
                            self.image_index -= 3
                    else:
                        self.image_index = 0
            else:
                self.image_index = 5

    def render(self, surface, camera):
        super().render(surface, camera)
        if self.iframes % 2 == 0 or self.dead:
            self.current_sprite.draw_self(surface, self.image_index, ((self.x - self.size[0] / 2) - self.camera_x, (self.y - self.size[1] / 2) - self.camera_y), self.dir == -1)
        # pygame.draw.rect(surface, (255, 255, 255), self.rect)
    pass
