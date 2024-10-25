import pyxel

pyxel.init(160,128)
pyxel.load("shooting-game.pyxres")

x = 0
y = 100
def update():
    global x,y,dx
    if pyxel.btn(pyxel.KEY_LEFT):
        dx = -2
    elif pyxel.btn(pyxel.KEY_RIGHT):
        dx = 2
    else:
        dx = 0

    # 横方向の移動
    x = x + dx
    return

def draw():
    pyxel.cls(1)
    pyxel.blt( x,y, 0, 0,0, 16,16, 0)
    return

pyxel.run(update,draw)
