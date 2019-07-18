import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position, images):
        super(AnimatedSprite, self).__init__()
        
        size = (32, 32)
        self.rect = pygame.Rect(position, size)
        #self.rect = (16,16)

        self.images = images 
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]
        self.index = 0
        self.image = images[self.index]
        self.velocity = pygame.math.Vector2(0,0)
        self.animation_time = 0.1
        self.current_time = 0
        self.animation_frames = 1
        self.current_frame = 0

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

