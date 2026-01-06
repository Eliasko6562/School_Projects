import pygame as pg

from systems.spawner import Spawner
from entities.player import Player

from settings import WIDTH, HEIGHT, FPS

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Game Arena')
        self.clock = pg.time.Clock()
        
        # ToDo: Inicializace skupiny objektu
        self.all_sprites = pg.sprite.Group()
        
        # ToDo: Vytvoreni objektu hrace
        self.player = Player(game=self, pos=(WIDTH / 2, HEIGHT / 2), size=(50, 50), color=(0, 255, 0))
        self.all_sprites.add(self.player)
        
        # ToDo: Inicializace systemu vytvareni nepratel
        self.enemies = pg.sprite.Group()
        self.spawner = Spawner(self)
        
        #ToDo: Inicializace skupiny projektilu
        self.bullets = pg.sprite.Group()
        
        # Stav hry
        self.running = True
        self.score = 0
        self.total_time = 0
        
        # Obrazky entit
        self.ship = pg.image.load("./images/ship.png")
        self.imagerect = self.ship.get_rect()
        
        self.meteorite = pg.image.load("./images/meteorite.png")
        self.meteoriterect = self.meteorite.get_rect()
        
        self.bullet = pg.image.load("./images/bullet2.png")
        self.bulletrect = self.bullet.get_rect()
        
    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000  # Delta time in seconds.
            self.handle_events()
            self.update(dt)
            self.draw()
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.shoot()

    def update(self, dt):
        self.all_sprites.update(dt)
        self.spawner.update(dt, self.total_time)
        self.total_time += dt
        for bullet in self.bullets:
            hits = pg.sprite.spritecollide(bullet, self.enemies, True)
            if hits:
                bullet.kill()
                self.score += len(hits)
                
        if pg.sprite.spritecollide(self.player, self.enemies, dokill=False):
            self.player.kill()
            self.running = False

    def draw(self):
        self.screen.fill((30, 30, 30))  # Clear screen with dark gray
        self.all_sprites.draw(self.screen)
        self.imagerect.center = self.player.rect.center
        self.screen.blit(self.ship, self.imagerect)
        for enemy in self.enemies:
            self.meteoriterect.center = enemy.rect.center
            self.screen.blit(self.meteorite, self.meteoriterect)
        for bullet in self.bullets:
            self.bulletrect.center = bullet.rect.center
            self.screen.blit(self.bullet, self.bulletrect)
        self.score_board()
        pg.display.flip()
        
    def score_board(self):
        font = pg.font.SysFont('Arial', 30)
        text = font.render(f'Kills: {self.score}', True, (255,255,255))
        self.screen.blit(text, (50, 50))
        text = font.render(f'Time: {self.total_time:.1f}', True, (255,255,255))
        self.screen.blit(text, (45, 85))
