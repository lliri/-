  
c=0


            


class chelovek:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.img = loadImage("3.jpg")
    def cheldraw(self):
        image(self.img ,self.x,self.y,50,50)
    def randomPos(self):
        self.x=random(50,750)
        self.y=random(50,550)
class cpritz:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.img = loadImage('sp.png')
    def drsp(self):
        image(self.img,mouseX - 60,mouseY - 45,160,280)
        #loadImage('sp.png')

def setup():
    global chel,cp
    fill(0)
    chel=chelovek(200,200)
    cp=cpritz(300,300)
    size(800,600)
def draw():

    background(255)
    cp.drsp()
    global c
    text(c,50,50)
    chel.cheldraw()
    if mousePressed:
        if mouseX>=chel.x and mouseX<=chel.x+50 and mouseY>=chel.y and mouseY<=chel.y+50:
            chel.randomPos()
            c+=1
