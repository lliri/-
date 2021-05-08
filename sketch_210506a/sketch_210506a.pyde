class player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.img=loadImage("player.png")
    def play(self):
        image(self.img,mouseX-125,mouseY-150,300,300)
class Vrag:
    def __init__(self):
        
        r = floor (random (1,5))
        x=0
        y=0
        if (r== 1):
            y = 0
            x = random(0,800)
        if (r == 2):
            y = 800
            x = random(0,800)
        if (r== 3):
            y = random(0,800)
            x = 0
        if (r == 4):
            y = random(0,800)
            x = 800
            
        
        self.x=x
        self.y=y
        self.dx=(x-400)/100
        self.dy=(y-400)/100
        self.img=loadImage("Vrag.png")
    def drvr(self):
        image(self.img,self.x,self.y,150,150)
    def move(self):
        self.x -= self.dx
        self.y -= self.dy
        #if x == 
        
def setup():
    global pl,vr
    #vr = Vrag()
    pl = player(200,200)
    size(800,800)
def draw():
    global x,y,dx,dy
    background(255)
    pl.play()
    #vr.drvr()
    #vr.move()
