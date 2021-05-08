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
    pl = player(200,200)
         
state  = 0
def setup():
    global vdsa
    vdsa=loadImage("start.png")
    init()
    size(800,800)
    frameRate(1000)
def draw():
    global x,y,dx,dy,vdsa
    
    if (state == 1):
        background(255)
        pl.play()
        
        for vr in vrags:
            vr.drvr()
            vr.move()
    elif (state == 0 ):
        background(255,0,0)
        image(vdsa, 400,400,500,500)
        
    
def mouseClicked():
    global state
    if state == 0:
        state = 1
        init()
