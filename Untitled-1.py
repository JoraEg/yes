from pygame import *







    class GameSprite(sprite.Sprite):
            #конструктор класса
        def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
            super().__init__()
            # каждый спрайт должен хранить свойство image - изображение
            self.image = transform.scale(image.load(player_image), (size_x, size_y))
            self.speed = player_speed
            # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

    class Player(GameSprite):
        def update_r(self):
            keys = key.get_pressed()
            if keys[K_w] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_s] and self.rect.x < win_width - 60:
                self.rect.x += self.speed
        def update_l(self):
            keys = key.get_pressed()
            if keys[K_UP] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_DOWN] and self.rect.x < win_width - 60:
                self.rect.x += self.speed

            




        win_width = 1250
        win_height = 800
        window = display.set_mode((win_width, win_height))
        display.set_caption('ЭПИЧНЫЙ СТРИМ СЕРЁГИ ПИРАТАВ   ')
        background = transform.scale(image.load(img_back), (win_width, win_height))






    display.update()
    clock.tick(FPS)






