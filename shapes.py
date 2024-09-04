import pgzrun
HEIGHT=499
WIDTH=499

def draw():
    screen.fill("blue")
    W=WIDTH
    H=HEIGHT-100
    for i in range(40):
        R1R=Rect((0,0,),(W,H))
        R1R.center = WIDTH/2, HEIGHT/2
        screen.draw.rect(R1R,(0,0,0))
        W-=5
        H+=5

pgzrun.go()