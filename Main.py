import turtle
import math
from consts import *
import random

window = turtle.Screen()
window.setup(SCREEN_WIDTH +220 ,SCREEN_HEIGHT +20)
window.title("Space Arena by Henrique!")
window.bgcolor("black")
window.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 2
        self.state = "splash"

    def start(self):
        self.state = "playing"

    def start_level(self):
        sprites.clear()

        #misseis inimigos
        for enemy_missile in enemy_missiles:
            sprites.append(enemy_missile)

        sprites.append(player)
        for missile in missiles:
            sprites.append(missile)

        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-1,1)
            dy = random.randint(-1,-1)
            sprites.append(Powerup(x,y,"circle","blue"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-1,1)
            dy = random.randint(-1,-1)
            sprites.append(Enemy(x,y,"square","red"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

    def mapa(self, pen, x_offset, y_offset):
        pen.color("white")
        pen.width(3)
        pen.penup()

        left = -self.width/2.0 - x_offset
        right = self.width/2.0 - x_offset
        top = self.height/2.0 - y_offset
        bottom = -self.height/2.0 -y_offset

        pen.goto(left,top)
        pen.pendown()
        pen.goto(right,top)
        pen.goto(right,bottom)
        pen.goto(left,bottom)
        pen.goto(left,top)
        pen.penup()

    def render_info(self,pen,score, active_enemies=0):
        pen.color("#222255")
        pen.penup()
        pen.goto(400,0)
        pen.shape("square")
        pen.setheading(90)
        pen.shapesize(10,32,None)
        pen.stamp()

        pen.color("white")
        pen.width(3)
        pen.goto(300,400)
        pen.pendown()
        pen.goto(300,-400)

        pen.penup()
        pen.color("white")
        character_pen.scale = 1.0
        character_pen.draw_string(pen,"SPACE ARENA", 400, 270)
        character_pen.draw_string(pen,"SCORE: {}".format(score), 400, 240)
        character_pen.draw_string(pen,"ENEMIES {}".format(active_enemies), 400, 210)
        character_pen.draw_string(pen,"LIVES: {}".format(player.lives), 400, 180)
        character_pen.draw_string(pen,"LEVEL: {}".format(game.level), 400, 150)


class CharacterPen():
    def __init__(self,color="white", scale = 1.0):
        self.color = color
        self.scale = scale
        self.characters = {}
        self.characters["1"] = ((-5,10),(0,10),(0,-10),(-5,-10),(5,-10))
        self.characters["2"] = ((-5, 10),(5, 10),(5, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["3"] = ((-5, 10),(5, 10),(5, 0), (0, 0), (5, 0), (5,-10), (-5, -10))
        self.characters["4"] = ((-5, 10), (-5, 0), (5, 0), (2,0), (2, 5), (2, -10))
        self.characters["5"] = ((5, 10), (-5, 10), (-5, 0), (5,0), (5,-10), (-5, -10))
        self.characters["6"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0))
        self.characters["7"] = ((-5, 10), (5, 10), (0, -10))
        self.characters["8"] = ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0))
        self.characters["9"] = ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0))
        self.characters["0"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))

        self.characters["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
        self.characters["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5,0), (5, -10), (-5, -10))
        self.characters["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
        self.characters["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
        self.characters["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
        self.characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
        self.characters["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
        self.characters["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))   
        self.characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
        self.characters["L"] = ((-5, 10), (-5, -10), (5, -10))
        self.characters["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
        self.characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
        self.characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
        self.characters["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
        self.characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
        self.characters["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
        self.characters["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10)) 
        self.characters["V"] = ((-5, 10), (0, -10), (5, 10)) 
        self.characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10)) 
        self.characters["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))   
        self.characters["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))   
        self.characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0,0), (0, -10))   
        self.characters["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))   
        
        self.characters["-"] = ((-3, 0), (3, 0))

    def draw_string(self,pen,str,x,y):
        pen.width(2)
        pen.color(self.color)

        x -= 15 * self.scale * ((len(str) -1)/2)
        for character in str:
            self.draw_character(pen,character,x,y)
            x += 15 * self.scale


    def draw_character(self,pen, character, x,y):
        scale = self.scale
        if character in "abcdfghijklmnopqrstuvwyxz":
            self.scale *= 0.8
        
        character = character.upper()

        if character in self.characters:
            pen.penup()
            xy = self.characters[character][0]
            pen.goto(x + xy[0] * scale, y + xy[1] *scale)
            pen.pendown()
            for i in range(1,len(self.characters[character])):
                xy = self.characters[character][i]
                pen.goto(x + xy[0] * scale, y + xy[1] *scale)
            pen.penup()


character_pen = CharacterPen("red", 3.0)
character_pen.draw_string(pen,"SPACE ARENA", 0, 160)
character_pen.scale = 1.0
character_pen.draw_string(pen, "BY HENRIQUE", 0 ,100)
pen.color("white")
pen.shape("triangle")
pen.goto(-150,20)
pen.stamp()
character_pen.draw_string(pen, "SPACESHIP", -150 ,-10)

pen.shape("square")
pen.goto(0,20)
pen.stamp()
character_pen.draw_string(pen, "ENEMY", 0, -10)


pen.shape("circle")
pen.color("blue")
pen.goto(100,20)
pen.stamp()
character_pen.draw_string(pen, "POWERUP", 100, -10)


character_pen.draw_string(pen, "UP ARROW",-100 ,-60 )
character_pen.draw_string(pen, "ACCELARATE", 100 ,-60 )
character_pen.draw_string(pen, "LEFT ARROW",-100 ,-100 )
character_pen.draw_string(pen, "ROTATE LEFT",100 ,-100 )
character_pen.draw_string(pen, "RIGHT ARROW",-100 ,-140 )
character_pen.draw_string(pen, "ROTATE RIGHT", 100,-140 )
character_pen.draw_string(pen, "SPACE", -100,-180 )
character_pen.draw_string(pen, "FIRE", 100,-180 )

character_pen.scale = 1.0
character_pen.draw_string(pen, "PRESS S TO START", 0,-240 )

window.tracer(0)

class Sprite():
    def __init__(self, x ,y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0
        self.thrust = 0.0
        self.accelaration = 0.003
        self.health = 20
        self.maxhealth = 20
        self.width = 20
        self.height = 20
        self.state = "active"
        self.radar = 200
        self.max_dx = 3
        self.max_dy = 3

    def colision(self,other):
        if self.x < other.x + other.width and\
            self.x + self.width > other.x and\
            self.y - other.y + other.height and\
            self.y + self.height > other.y:
            return True
        else:
            return False

    def bounce(self,other):
        temp_dx = self.dx
        temp_dy = self.dy

        self.dx = other.dx
        self.dy = other.dy

        other.dx = temp_dx
        other.dy = temp_dy

    def update(self):
        
        self.heading += self.da
        self.heading %= 360

        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust

        self.x += self.dx
        self.y += self.dy

        self.border_check()

    def border_check(self):
        if self.x > game.width/2.0 -10:
            self.x = game.width/2.0 - 10
            self.dx *= -1

        elif self.x < -game.width/2.0 +10:
            self.x = -game.width/2.0 + 10
            self.dx *= -1
        
        if self.y > game.height/2.0 -10:
            self.y = game.height/2.0 - 10
            self.dy *= -1

        elif self.y < -game.height/2.0 +10:
            self.y = -game.height/2.0 + 10
            self.dy *= -1

        

    def render(self,pen, x_offset, y_offset):
        if self.state == "active":
                
            pen.goto(self.x - x_offset,self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()


            self.health_meter(pen, x_offset, y_offset)

    #health meter
    def health_meter(self, pen, x_offset,y_offset):
        pen.goto(self.x - x_offset - 10, self.y - y_offset + 20)
        pen.width(3)
        pen.pendown()
        pen.setheading(0)
    
        if self.health/self.maxhealth <0.3:
            pen.color("red")
        elif self.health/self.maxhealth <0.7:
            pen.color("yellow")
        else:
            pen.color("green")

        pen.fd(20 * (self.health/self.maxhealth))
        if self.health != self.maxhealth:
            pen.color("grey")
            pen.fd(20 * ((self.maxhealth-self.health)/self.maxhealth))

        pen.penup()

    
game = Game(700,500)

class Enemy(Sprite):
    def __init__(self, x, y , shape, color):
        Sprite.__init__(self,400,300,shape,color)
        self.maxhealth = 20
        self.health = self.maxhealth
        self.type = random.choice(["hunter", "mine", "surveillance"])

        if self.type == "hunter":
            self.color = "red"
            self.shape = "square"

        elif self.type == "mine":
                self.color = "orange"
                self.shape = "square"

        elif self.type == "surveillance":
            self.color = "green"
            self.shape = "square"

    def update(self):
        if self.state == "active":

            self.heading += self.da
            self.heading %= 360

            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

            self.x += self.dx
            self.y += self.dy

            self.border_check()

            if self.health <= 0:
                self.reset()
            
            if self.type == "hunter":
                if self.x < player.x:
                    self.dx += 0.05
                else:
                    self.dx -= 0.05
                if self.y < player.y:
                    self.dy += 0.05
                else:
                    self.dy -= 0.05

            elif self.type == "mine":
                self.dx = 0
                self.dy = 0
            elif self.type == "surveillance":
                if self.x < player.x:
                   self.dx -= 0.05
                else:
                    self.dx += 0.05
                if self.y < player.y:
                    self.dy -= 0.05
                else:
                    self.dy += 0.05

            #definir velocidade máxima
            if self.dx > self.max_dx:
                self.dx = self.max_dx
            elif self.dx < -self.max_dx:
                self.dx = -self.max_dx
            
            if self.dy > self.max_dy:
                self.dy = self.max_dy
            elif self.dy < -self.max_dy:
                self.dy = -self.max_dy

    
    def reset(self):
        self.state = "inactive"
    

class Powerup(Sprite):
    def __init__(self, x, y , shape, color):
        Sprite.__init__(self,0,0,shape,color)

class Player(Sprite):
    def __init__(self, x, y , shape, color):
        Sprite.__init__(self,0,0,shape,color)
        self.lives = 3
        self.score = 0
        self.heading = 90
        self.da = 0

    def rotateleft(self):
        self.da = 0.5

    def rotateright(self):
        self.da = -0.5

    def stop(self):
        self.da = 0

    def accelarate(self):
        self.thrust += self.accelaration

    def decelarate(self):
        self.thrust = 0.0

    def fire(self):
        num_of_missiles = 0

        for missile in missiles:
            if missile.state == "ready":
                num_of_missiles += 1


        for missile in missiles:
            if num_of_missiles == 1 and missile.state == "ready":             
                missile.fire(self.x,self.y, self.heading, self.dx,self.dy)
                break
            if num_of_missiles == 2:             
                directions = [-5,5]
                for missile in missiles:
                    if missile.state == "ready":
                        missile.fire(self.x,self.y, self.heading + directions.pop(), self.dx,self.dy)
            if num_of_missiles == 3:
                directions = [0,-10,10]
                for missile in missiles:
                    if missile.state == "ready":
                        missile.fire(self.x,self.y, self.heading + directions.pop(), self.dx,self.dy)
                    

    def render(self,pen, x_offset, y_offset):
        pen.shapesize(0.5,1.0,None)
        pen.goto(self.x - x_offset,self.y - y_offset)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()
        pen.shapesize(1.0,1.0,None)

        self.health_meter(pen, x_offset, y_offset)

    def update(self):
        if self.state == "active":

            self.heading += self.da
            self.heading %= 360

            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

            self.x += self.dx
            self.y += self.dy

            self.border_check()

            if self.health <= 0:
                self.reset()
    
    def reset(self):
        self.x = 0
        self.y = 0
        self.health = self.maxhealth
        self.heading = 90
        self.dx = 0
        self.dy = 0
        self.lives -= 1

class Missile(Sprite):
    def __init__(self, x, y , shape, color):
        Sprite.__init__(self,0,0,shape,color)
        self.state = "ready"
        self.thrust = 5.0
        self.maxfuel = 300
        self.fuel = self.maxfuel
        self.height = 4
        self.width = 4
    
    def fire(self,x,y,heading,dx,dy):
        if self.state == "ready":
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy

            self.dx += math.cos(math.radians(self.heading)) * self.thrust /2
            self.dy += math.sin(math.radians(self.heading)) * self.thrust /2


    def render(self,pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(0.1,0.1,None)
            pen.goto(self.x - x_offset,self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()
            pen.shapesize(1.0,1.0,None)

    def update(self):
        if self.state == "active":
            self.fuel -= self.thrust
            if self.fuel <=0:
                self.reset()
            self.heading += self.da
            self.heading %= 360

            self.x += self.dx
            self.y += self.dy

            self.border_check()

    def reset(self):
        self.fuel = self.maxfuel
        self.dx = 0
        self.dy = 0
        self.state = "ready"

class EnemyMissile(Sprite):
    def __init__(self, x, y , shape, color):
        Sprite.__init__(self,0,0,shape,color)
        self.state = "ready"
        self.thrust = 5.0
        self.maxfuel = 300
        self.fuel = self.maxfuel
        self.height = 4
        self.width = 4
    
    def fire(self,x,y,heading,dx,dy):
        if self.state == "ready":
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy

            self.dx += math.cos(math.radians(self.heading)) * self.thrust /2
            self.dy += math.sin(math.radians(self.heading)) * self.thrust /2


    def render(self,pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(0.1,0.1,None)
            pen.goto(self.x - x_offset,self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()
            pen.shapesize(1.0,1.0,None)

    def update(self):
        if self.state == "active":
            self.fuel -= self.thrust
            if self.fuel <=0:
                self.reset()
            self.heading += self.da
            self.heading %= 360

            self.x += self.dx
            self.y += self.dy

            self.border_check()

    def reset(self):
        self.fuel = self.maxfuel
        self.dx = 0
        self.dy = 0
        self.state = "ready"

#camara que segue o jogador
class Camera():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def update(self,x,y):
        self.x = x
        self.y = y

class Radar():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def render(self,pen,sprites):
        pen.color("white")
        pen.setheading(90)
        pen.goto(self.x + self.width/2.0, self.y)
        pen.pendown()
        pen.circle(self.width/2.0)
        pen.penup()

        for sprite in sprites:
            if sprite.state == "active":
                radar_x = self.x + (sprite.x - player.x) *(self.width/game.width)
                radar_y = self.y + (sprite.y - player.y) *(self.height/game.height)
                pen.goto(radar_x,radar_y)
                pen.color(sprite.color)
                pen.shape(sprite.shape)
                pen.setheading(sprite.heading)
                pen.shapesize(0.1,0.1,None)

                distance = ((player.x-sprite.x)**2 + (player.y-sprite.y)**2)**0.5
                if distance< player.radar:
                    pen.stamp()

radar = Radar(400,-200,200,200)


#criar o jogador
player = Player(0,0,"triangle", "white")
player.dx = 0.2
player.dy = -0.1

#criar a camara
camera = Camera(player.x,player.y)

missiles = []
for _ in range(3):
    missiles.append(Missile(0,100, "circle", "yellow"))

enemy_missiles = []

for _ in range(1):
    enemy_missiles.append(EnemyMissile(0,100, "circle", "red"))


sprites = []



game.start_level()


#key bindings

window.listen()
window.onkeypress(player.rotateleft, "Left")
window.onkeypress(player.rotateright, "Right")
window.onkeyrelease(player.stop, "Left")
window.onkeyrelease(player.stop, "Right")
window.onkeypress(player.fire, "space")

window.onkeypress(player.accelarate, "Up")
window.onkeyrelease(player.decelarate, "Up")
window.onkeypress(game.start, "s")
window.onkeypress(game.start, "S")

while running:

    if game.state == "splash":
        window.update()
    elif game.state == "playing":
        pen.clear()

        #atualizar os bonecos
        for sprite in sprites:
            sprite.update()

        #disparar misseis inimigos
        for enemy_missile in enemy_missiles:
            if enemy_missile.state == "ready":
                enemies = []

                for sprite in sprites:
                    if isinstance(sprite,Enemy):
                        enemies.append(sprite)

                enemy = random.choice(enemies)
                heading = math.atan2(player.y - enemy.y, player.x - enemy.x)
                heading = heading * (180/3.14159)
                enemy_missile.fire(enemy.x,enemy.y,heading, enemy.dx,enemy.dy)


        for sprite in sprites:
            if isinstance(sprite,Enemy) and sprite.state == "active":
                if player.colision(sprite):
                    sprite.health -= 5
                    player.health -= 5
                    player.bounce(sprite)
                for missile in missiles:
                    if missile.state == "active" and missile.colision(sprite):
                        sprite.health -= 10
                        missile.reset()

            if isinstance(sprite,Powerup):
                if player.colision(sprite):
                    sprite.x = 100
                    sprite.y = 100
                for missile in missiles:
                    if missile.state == "active" and missile.colision(sprite):
                        sprite.x = 100
                        sprite.y = 100
                        missile.reset()

            if isinstance(sprite,EnemyMissile):
                if sprite.state == "active" and sprite.colision(player):
                    sprite.reset()
                    player.health -= 5

        #desenhar os bonecos
        for sprite in sprites:
            sprite.render(pen,camera.x+100, camera.y)

        game.mapa(pen, camera.x+100,camera.y)

        #end_of_level = True
        #for sprite in sprites:
        #   if isinstance(sprites,Enemy) and sprite.state == "active":
        #        end_of_level = False
        #if end_of_level:
        #    game.level += 1
        #    game.start_level()

        camera.update(player.x,player.y)
        game.render_info(pen,0,0)
        radar.render(pen,sprites)



        window.update()



