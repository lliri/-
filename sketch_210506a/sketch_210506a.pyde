class player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.w=150
        self.h=150
        self.img=loadImage("player.png")
    def play(self):
        if mousePressed and mouseButton == RIGHT:
            fill(255,0,0)
            rect(self.x,self.y,300,300)
        image(self.img,mouseX-75,mouseY-75,self.w,self.h)
class Vrag:
    def __init__(self):
        
        r = floor (random (1,5))
        self.x=0
        self.y=0
        if (r== 1):
            self.y = 0
            self.x = random(0,800)
        if (r == 2):
            self.y = 800
            self.x = random(0,800)
        if (r== 3):
            self.y = random(0,800)
            self.x = 0
        if (r == 4):
            self.y = random(0,800)
            self.x = 800
        

        self.dx=(self.x-400)/100
        self.dy=(self.y-400)/100
        
        self.img=loadImage("Vrag.png")
    def drvr(self):
        if mousePressed and mouseButton==RIGHT:
            fill(255,0,0)
            rect(self.x,self.y,150,150)
        image(self.img,self.x,self.y,150,150)
        
    def move(self):
        self.x -=self.dx
        self.y -=self.dy
        
        if self.y >= 850 or self.y<= -50 or self.x >= 850 or self.x <= -50 :
            r=random(1,5)
            if (r== 1):
                self.y = 0
                self.x = random(0,800)
            if (r == 2):
                self.y = 800
                self.x = random(0,800)
            if (r== 3):
                self.y = random(0,800)
                self.x = 0
            if (r == 4):
                self.y = random(0,800)
                self.x = 800
            self.dx=(self.x-mouseX)/100
            self.dy=(self.y-mouseY)/100
    
def init():
    global pl,vrags
    vrags = []
    
    for i in range(8):
        vrags.append(Vrag())
    pl = player(mouseX-150,mouseY-150)
         
state  = 0



def collideRects(x,y,w,h , x1,y1,w1,h1):
    
    def collide(x,y,w,h  , x1, y1):
        return x1>=x and x1 <= x+w and y1 >= y and y1 <= y+h
    return collide(x,y,w,h , x1,y1) or collide(x,y,w,h , x1+w1,y1) or collide(x,y,w,h , x1,y1+h1) or collide(x,y,w,h , x1+w1,y1+h1)
    
state  = 0
def setup():
    global vdsa
    pl = player(mouseX-150,mouseY-150)
    vdsa=loadImage("start.png")
    init()
    size(800,800)
    frameRate(1000)
def draw():
    pl = player(mouseX-150,mouseY-150)
    textSize(50)
    global x,y,dx,dy,vdsa,state
    
    if (state == 1):
        background(255)
        pl.play()
        
        for vr in vrags:
            vr.drvr()
            vr.move() 
            if ( collideRects( vr.x,vr.y,150,150  , mouseX-75,mouseY-75,pl.w,pl.h)) :
                state = 0
            
            
            
    elif (state == 0 ):
        background(255,0,0)
        text("start game",300,400)

        
    
def mouseClicked():
    global state
    if state == 0:
        state = 1
        init()
