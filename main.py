# Author: Poseidon-Fan

import pygame
from pygame.locals import *
import sys
import random
pygame.init()


# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_IMG.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.speed = 10

    def draw(self):
        SCREEN.blit(self.image, self.rect)


# 第一种敌机
class Enemy1(pygame.sprite.Sprite):
    def __init__(self, enhance):
        super().__init__()
        self.image = ENEMY1_IMG
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        if enhance == 0:
            self.health_points = 700
            self.speed = 1
        else:
            self.health_points = 1000
            self.speed = 2
        self.score = 500

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        global running, score
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)
        if self.health_points <= 0:
            enemies.remove(self)
            bomb_sound.play()
            score += self.score
        if pygame.sprite.collide_mask(self, PLAYER):
            running = 0


# 第二种敌机
class Enemy2(pygame.sprite.Sprite):
    def __init__(self, enhance):
        super().__init__()
        self.image = ENEMY2_IMG
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        if enhance == 0:
            self.speed = 3
            self.health_points = 100
        else:
            self.speed = 5
            self.health_points = 150
        self.score = 100

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        global running, score
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)
        if self.health_points <= 0:
            enemies.remove(self)
            bomb_sound.play()
            score += self.score
        if pygame.sprite.collide_mask(self, PLAYER):
            running = 0


# 第三种敌机
class Enemy3(pygame.sprite.Sprite):
    def __init__(self, enhance):
        super().__init__()
        self.image = ENEMY3_IMG
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        if enhance == 0:
            self.speed = 25
            self.health_points = 50
        else:
            self.speed = 30
            self.health_points = 100
        self.score = 200

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        global running, score
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)
        if self.health_points <= 0:
            enemies.remove(self)
            bomb_sound.play()
            score += self.score
        if pygame.sprite.collide_mask(self, PLAYER):
            running = 0


# 第四种敌机
class Enemy4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ENEMY4_IMG
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.speed = 0.5
        self.health_points = 1500

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        global running
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height:
            enemies.remove(self)
        if self.health_points <= 0:
            enemies.remove(self)
            bomb_sound.play()
        if pygame.sprite.collide_mask(self, PLAYER):
            running = 0

    def shoot(self):
        bullet = EnemyBullet()
        bullet.rect.midtop = self.rect.midbottom
        enemy_bullets.add(bullet)


# 终极模式中第四种敌机的子弹
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ENEMY_BULLET_IMG
        self.rect = self.image.get_rect()
        self.speed = 10

    def update(self):
        global running
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            enemy_bullets.remove(self)
        if pygame.sprite.collide_mask(self, PLAYER):
            running = 0

    def draw(self):
        SCREEN.blit(self.image, self.rect)


# 第一种子弹
class Bullet1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = BULLET1_IMG
        self.rect = self.image.get_rect()
        self.rect.center = PLAYER.rect.midtop
        self.damage_points = 10
        self.speed = 50

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.top <= 0:
            bullets.remove(self)
        collision = pygame.sprite.spritecollide(self, enemies, False, pygame.sprite.collide_mask)
        if len(collision):
            collision[0].health_points -= self.damage_points
            bullets.remove(self)


# 第二种子弹
class Bullet2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = BULLET2_IMG
        self.rect = self.image.get_rect()
        self.rect.center = PLAYER.rect.midtop
        self.damage_points = 15
        self.speed = 60

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.top <= 0:
            bullets.remove(self)
        collision = pygame.sprite.spritecollide(self, enemies, False, pygame.sprite.collide_mask)
        if len(collision):
            collision[0].health_points -= self.damage_points
            bullets.remove(self)


# 第三种子弹
class Bullet3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = BULLET3_IMG
        self.rect = self.image.get_rect()
        self.rect.center = PLAYER.rect.midtop
        self.damage_points = 25
        self.speed = 75

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.top <= 0:
            bullets.remove(self)
        collision = pygame.sprite.spritecollide(self, enemies, False, pygame.sprite.collide_mask)
        if len(collision):
            collision[0].health_points -= self.damage_points
            bullets.remove(self)


# 补给子弹——右
class Bullet4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = BULLET_SUPPLY_IMG
        self.rect = self.image.get_rect()
        self.rect.center = PLAYER.rect.midtop
        self.rect.x += self.rect.width / 2
        self.rect.x -= 10
        self.damage_points = 30
        self.speed = 70

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.top <= 0:
            bullets.remove(self)
        collision = pygame.sprite.spritecollide(self, enemies, False, pygame.sprite.collide_mask)
        if len(collision):
            collision[0].health_points -= self.damage_points
            bullets.remove(self)


# 补给子弹——左
class Bullet5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = BULLET_SUPPLY_IMG
        self.rect = self.image.get_rect()
        self.rect.center = PLAYER.rect.midtop
        self.rect.x -= self.rect.width / 2
        self.rect.x += 10
        self.damage_points = 30
        self.speed = 70

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.top <= 0:
            bullets.remove(self)
        collision = pygame.sprite.spritecollide(self, enemies, False, pygame.sprite.collide_mask)
        if len(collision):
            collision[0].health_points -= self.damage_points
            bullets.remove(self)


# 补给类
class Supply(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = SUPPLY_IMG
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.speed = 25

    def update(self):
        self.rect.y += self.speed
        if pygame.sprite.collide_rect(self, PLAYER):
            supplies.remove(self)
            pygame.time.set_timer(FIRE_B4, 100, 20)
            pygame.time.set_timer(FIRE_B5, 100, 20)

    def draw(self):
        SCREEN.blit(self.image, self.rect)


# 常量设置
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 800
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 80
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ICON = pygame.image.load('icon.jpg')
pygame.display.set_icon(ICON)
pygame.display.set_caption('飞机大战')
pygame.mixer.music.load('bg.wav')
pygame.mixer.music.play(-1)
bomb_sound = pygame.mixer.Sound('exp.wav')
BG = pygame.transform.scale(pygame.image.load('bg.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))
BG_FINAL = pygame.transform.scale(pygame.image.load('bg_final.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 30
PLAYER_IMG = pygame.transform.scale(pygame.image.load('plane.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER = Player()
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)
BOMB_FONT = pygame.font.Font('freesansbold.ttf', 32)
GAME_OVER_FONT = pygame.font.Font('freesansbold.ttf', 64)

# 加载图像
ENEMY1_IMG = pygame.image.load('enemy1.png').convert_alpha()
ENEMY2_IMG = pygame.image.load('enemy2.png').convert_alpha()
ENEMY3_IMG = pygame.image.load('enemy3.png').convert_alpha()
ENEMY4_IMG = pygame.image.load('enemy4.png').convert_alpha()
ENEMY_BULLET_IMG = pygame.image.load('enemy4_bullet.png').convert_alpha()
BULLET1_IMG = pygame.image.load('bullet1.png').convert_alpha()
BULLET2_IMG = pygame.image.load('bullet2.png').convert_alpha()
BULLET3_IMG = pygame.image.load('bullet3.png').convert_alpha()
BULLET_SUPPLY_IMG = pygame.image.load('bullet4.png').convert_alpha()
SUPPLY_IMG = pygame.image.load('supply.png').convert_alpha()

# 自定义事件
FIRE_B1 = USEREVENT + 1
FIRE_B2 = USEREVENT + 2
FIRE_B3 = USEREVENT + 3
FIRE_B4 = USEREVENT + 4
FIRE_B5 = USEREVENT + 5
ADD_ENEMIES_L1 = USEREVENT + 6
ADD_ENEMIES_L2 = USEREVENT + 7
ADD_ENEMIES_L3 = USEREVENT + 8
LEVEL_UP = USEREVENT + 9
BOMB = USEREVENT + 10
SUPPLY = USEREVENT + 11
FINAL_ADD_ENEMY = USEREVENT + 12
FINAL_FIRE = USEREVENT + 13
ENEMY_FIRE = USEREVENT + 14

# 初始化游戏循环钟
pygame.time.set_timer(LEVEL_UP, 1000)
pygame.time.set_timer(ADD_ENEMIES_L1, 2000)
pygame.time.set_timer(BOMB, 40000)
pygame.time.set_timer(SUPPLY, 10000)
pygame.time.set_timer(FIRE_B1, 200)

# 精灵组容容器
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
supplies = pygame.sprite.Group()


# 显示分数
def show_score():
    text = f'Score: {score}'
    score_render = SCORE_FONT.render(text, True, (255, 255, 255))
    SCREEN.blit(score_render, (10, 10))


# 显示补给数
def show_bomb(bomb_num):
    text = f'bomb:{bomb_num}'
    bomb_render = BOMB_FONT.render(text, True, (255, 255, 255))
    rect = bomb_render.get_rect()
    rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)
    SCREEN.blit(bomb_render, rect)


# 常规时间内死亡，显示得分
def show_over(score):
    text1 = 'GAME OVER'
    text2 = f'YOUR SCORE: {score}'
    over_render1 = GAME_OVER_FONT.render(text1, True, (255, 0, 0))
    over_render2 = GAME_OVER_FONT.render(text2, True, (255, 0, 0))
    rect1 = over_render1.get_rect()
    rect2 = over_render2.get_rect()
    rect1.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    rect2.midtop = rect1.midbottom
    SCREEN.blit(over_render1, rect1)
    SCREEN.blit(over_render2, rect2)


# 添加敌人，分为不同级别
def add_enemies(level, enhance):
    if level == 1:
        enemies.add(Enemy2(enhance))

    elif level == 2:
        rand = random.randint(1, 100)
        if rand < 50:
            enemies.add(Enemy3(enhance))
        else:
            enemies.add(Enemy2(enhance))
    elif level == 3:
        rand = random.randint(1, 100)
        if rand <= 7:
            enemies.add(Enemy1(enhance))
        elif rand <= 55:
            enemies.add(Enemy2(enhance))
        else:
            enemies.add(Enemy3(enhance))
    elif level == 4:  # 终极模式
        if random.randint(1, 100) >= 70:
            enemies.add(Enemy4())
        for i in range(1, 3):
            enemies.add(Enemy3(1))
        rand = random.randint(1, 100)
        if rand <= 15:
            enemies.add(Enemy4())
        elif rand <= 40:
            enemies.add(Enemy1(1))
        elif rand <= 70:
            enemies.add(Enemy2(1))
        else:
            enemies.add(Enemy3(1))


# 显示警告画面
def show_warning():
    warning_img = pygame.image.load('warning.png')
    warning_rect = warning_img.get_rect()
    warning_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    time = 90
    while time:
        time -= 1
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[K_a]:
            PLAYER.rect.x -= PLAYER.speed
            if PLAYER.rect.x < 0:
                PLAYER.rect.x = 0
        if pressed[K_d]:
            PLAYER.rect.x += PLAYER.speed
            if PLAYER.rect.x + PLAYER.rect.width > SCREEN_WIDTH:
                PLAYER.rect.x = SCREEN_WIDTH - PLAYER.rect.width
        if pressed[K_w]:
            PLAYER.rect.y -= PLAYER.speed
            if PLAYER.rect.y < 0:
                PLAYER.rect.y = 0
        if pressed[K_s]:
            PLAYER.rect.y += PLAYER.speed
            if PLAYER.rect.y + PLAYER.rect.height > SCREEN_HEIGHT:
                PLAYER.rect.y = SCREEN_HEIGHT - PLAYER.rect.height
        SCREEN.blit(BG_FINAL, (0, 0))
        SCREEN.blit(warning_img, warning_rect)
        PLAYER.draw()
        pygame.display.update()


# 终极模式
def final():
    global running

    # 显示警告动画
    show_warning()

    running = 1
    PLAYER.speed = 20  # 增加玩家移动速度

    # 设定循环钟
    pygame.time.set_timer(FINAL_ADD_ENEMY, 4000)
    pygame.time.set_timer(FINAL_FIRE, 150)
    pygame.time.set_timer(ENEMY_FIRE, 4000)

    # 主循环
    while running:
        CLOCK.tick(30)
        SCREEN.blit(BG_FINAL, (0, 0))

        # 事件处理——退出与自定义
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == FINAL_ADD_ENEMY:
                add_enemies(4, 1)
            elif event.type == FINAL_FIRE:
                bullets.add(Bullet3())
                bullets.add(Bullet4())
                bullets.add(Bullet5())
            elif event.type == ENEMY_FIRE:
                for enemy in enemies:
                    if type(enemy) == Enemy4:
                        enemy.shoot()

        # 处理键盘事件，玩家移动
        pressed = pygame.key.get_pressed()
        if pressed[K_a]:
            PLAYER.rect.x -= PLAYER.speed
            if PLAYER.rect.x < 0:
                PLAYER.rect.x = 0
        if pressed[K_d]:
            PLAYER.rect.x += PLAYER.speed
            if PLAYER.rect.x + PLAYER.rect.width > SCREEN_WIDTH:
                PLAYER.rect.x = SCREEN_WIDTH - PLAYER.rect.width
        if pressed[K_w]:
            PLAYER.rect.y -= PLAYER.speed
            if PLAYER.rect.y < 0:
                PLAYER.rect.y = 0
        if pressed[K_s]:
            PLAYER.rect.y += PLAYER.speed
            if PLAYER.rect.y + PLAYER.rect.height > SCREEN_HEIGHT:
                PLAYER.rect.y = SCREEN_HEIGHT - PLAYER.rect.height

        # 画面更新与显示
        PLAYER.draw()
        bullets.update()
        enemies.update()
        enemy_bullets.update()
        bullets.draw(SCREEN)
        enemies.draw(SCREEN)
        supplies.draw(SCREEN)
        enemy_bullets.draw(SCREEN)
        pygame.display.update()


# 全局变量设置
score = 0
running = 1


# 普通模式主函数
def main():
    global running
    to_final = 0  # 判断是否达到分数要求，通向终极关
    enhance = 0  # 判断敌机是否增强
    level_flag = 0  # 记录游戏难度，相当于计时器，每10s +1
    bomb_num = 1  # 炸弹数
    fire_level = 1  # 玩家开火级别

    # 初始化两个敌机
    enemies.add(Enemy2(0))
    enemies.add(Enemy2(0))

    # 游戏主循环
    while running:
        CLOCK.tick(FPS)
        SCREEN.blit(BG, (0, 0))

        # 处理各种自定义事件
        for event in pygame.event.get():
            # 退出事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 开火
            elif event.type == FIRE_B1:
                bullets.add(Bullet1())
            elif event.type == FIRE_B2:
                bullets.add(Bullet2())
            elif event.type == FIRE_B3:
                bullets.add(Bullet3())
            elif event.type == FIRE_B4:
                bullets.add(Bullet4())
            elif event.type == FIRE_B5:
                bullets.add(Bullet5())

            # 每十秒，记录一下，判断敌机是否升级，难度是否增加
            elif event.type == LEVEL_UP:
                level_flag += 1
                if level_flag == 15:
                    pygame.time.set_timer(ADD_ENEMIES_L1, 0)
                    pygame.time.set_timer(ADD_ENEMIES_L2, 1500)
                if level_flag == 40:
                    pygame.time.set_timer(ADD_ENEMIES_L2, 0)
                    pygame.time.set_timer(ADD_ENEMIES_L3, 1000)
                if level_flag == 100:
                    enhance = 1

            # 增加敌人
            elif event.type == ADD_ENEMIES_L1:
                add_enemies(1, enhance)
            elif event.type == ADD_ENEMIES_L2:
                add_enemies(2, enhance)
            elif event.type == ADD_ENEMIES_L3:
                add_enemies(3, enhance)

            elif event.type == BOMB:
                if bomb_num < 3:
                    bomb_num += 1

            # 玩家释放炸弹，清空屏幕上的敌人
            elif event.type == KEYDOWN and event.key == K_SPACE and bomb_num > 0:
                bomb_num -= 1
                enemies.empty()
                bomb_sound.play(2)

            # 掉落补给
            elif event.type == SUPPLY:
                supplies.add(Supply())

        # 处理键盘事件——玩家移动
        pressed = pygame.key.get_pressed()
        if pressed[K_a]:
            PLAYER.rect.x -= PLAYER.speed
            if PLAYER.rect.x < 0:
                PLAYER.rect.x = 0
        if pressed[K_d]:
            PLAYER.rect.x += PLAYER.speed
            if PLAYER.rect.x + PLAYER.rect.width > SCREEN_WIDTH:
                PLAYER.rect.x = SCREEN_WIDTH - PLAYER.rect.width
        if pressed[K_w]:
            PLAYER.rect.y -= PLAYER.speed
            if PLAYER.rect.y < 0:
                PLAYER.rect.y = 0
        if pressed[K_s]:
            PLAYER.rect.y += PLAYER.speed
            if PLAYER.rect.y + PLAYER.rect.height > SCREEN_HEIGHT:
                PLAYER.rect.y = SCREEN_HEIGHT - PLAYER.rect.height

        # 更新与显示屏幕
        show_score()
        show_bomb(bomb_num)
        PLAYER.draw()
        bullets.update()
        enemies.update()
        supplies.update()
        bullets.draw(SCREEN)
        enemies.draw(SCREEN)
        supplies.draw(SCREEN)

        # 通过分数判断是否给玩家升级
        if score >= 1200 and fire_level == 1:
            fire_level = 2
            pygame.time.set_timer(FIRE_B1, 0)
            pygame.time.set_timer(FIRE_B2, 150)

        if score >= 5000 and fire_level == 2:
            fire_level = 3
            pygame.time.set_timer(FIRE_B2, 0)
            pygame.time.set_timer(FIRE_B3, 125)

        if score >= 10000:
            running = 0
            to_final = 1

        pygame.display.update()

    # 普通模式结束（先关闭所有事件，再判断是否进入终极模式）
    pygame.time.set_timer(FIRE_B1, 0)
    pygame.time.set_timer(FIRE_B2, 0)
    pygame.time.set_timer(FIRE_B3, 0)
    pygame.time.set_timer(FIRE_B4, 0)
    pygame.time.set_timer(FIRE_B5, 0)
    pygame.time.set_timer(LEVEL_UP, 0)
    pygame.time.set_timer(ADD_ENEMIES_L1, 0)
    pygame.time.set_timer(ADD_ENEMIES_L2, 0)
    pygame.time.set_timer(ADD_ENEMIES_L3, 0)
    pygame.time.set_timer(BOMB, 0)
    pygame.time.set_timer(SUPPLY, 0)
    enemies.empty()
    bullets.empty()
    supplies.empty()
    pygame.event.clear()

    # 判断是否进入终极模式
    if not to_final:
        while 1:
            SCREEN.blit(BG, (0, 0))
            show_over(score)  # 显示结束动画
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
    else:
        final()  # 进入终极模式


if __name__ == '__main__':
    main()







