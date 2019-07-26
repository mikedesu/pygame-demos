import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position, images):
        super(AnimatedSprite, self).__init__()
        
        size = (32, 32)

        # experimenting with adding multiple animations
        self.current_animation = 0
        self.total_animations = 5
        self.rect = pygame.Rect(position, size)
        self.animations = images
        self.images = self.animations[self.current_animation] 
        self.images_right = self.animations[self.current_animation]
        self.images_left = [pygame.transform.flip(image, True, False) for image in self.animations[self.current_animation]]
        self.index = 0
        self.image = self.animations[self.current_animation][self.index]
        self.velocity = pygame.math.Vector2(0,0)
        self.animation_time = 0.1
        self.current_time = 0
        self.animation_frames = 4
        self.current_frame = 0

    def set_current_animation(self):
        # 0 = default
        # 1 = boosters on up
        # 2 = boosters on down
        # 3 = boosters left and up
        # 4 = boosters left and down
        self.index = -1
        if self.velocity.y == 0:
            self.index = 0
        elif self.velocity.x == 0 and self.velocity.y > 0:
            self.index = 1
        elif self.velocity.x == 0 and self.velocity.y < 0:
            self.index = 2
        elif self.velocity.y > 0:
            self.index = 4
        elif self.velocity.y < 0:
            self.index = 3
        else:
            self.index = 0

        if self.index >= 0 and self.index < self.total_animations:
            self.current_animation = self.index
            self.images = self.animations[self.current_animation] 
            self.images_right = self.animations[self.current_animation]
            self.images_left = [pygame.transform.flip(image, True, False) for image in self.animations[self.current_animation]]
        else:
            print(f"Error: set_current_animation() index {index} out of range")


    def update_time_dependent(self, dt):
        if self.velocity.x > 0:
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left 
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = 0
            self.image = self.images[self.index]
        self.rect.move_ip(*self.velocity)

    def update_frame_dependent(self):
        if self.velocity.x > 0:
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left 
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index+1)%len(self.images)
            self.image = self.images[self.index]
        self.rect.move_ip(*self.velocity)

    def update(self, dt):
        #self.update_time_dependent(dt)
        self.update_frame_dependent()

