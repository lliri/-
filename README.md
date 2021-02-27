lst = [[1,1,1,1,1,2,2],
       [1,1,1,1,2,0,2],
       [1,2,1,2,0,2,1],
       [2,3,2,0,2,1,1],
       [1,2,0,2,1,1,1],
       [2,3,2,3,2,1,1],
       [1,2,1,2,1,1,1]]
def setup():
    size(400,400)
def draw():
    for indexy in range(len(lst)):
        for indexx in range(len(lst[indexy])):
            if lst[indexy][indexx] == 1:
                fill('#139B08')
            if lst[indexy][indexx] == 2:
                fill('#000000')
            if lst[indexy][indexx] == 3:
                fill('#B96E0B')
            elif lst[indexy][indexx] == 0:
                fill('#0AA0CB')
            square(indexx*50,indexy*50,50)
            if mousePressed and mouseButton == LEFT:
                if mouseX > indexx*50 and mouseX<indexx*50 + 50 and mouseY > indexy*50 and mouseY<indexy*50 + 50:
                    lst[indexy][indexx] = fill(random(0,255),random(0,255),random(0,255))
