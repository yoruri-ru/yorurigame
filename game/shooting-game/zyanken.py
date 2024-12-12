import pyxel
import random

COM_HAND = 0
PLAYER_HAND = 0

class App:
    
    def __init__(self):
        pyxel.init(80, 64, title="zyanken", fps=25)
        pyxel.load("zyanken.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        global COM_HAND, PLAYER_HAND
        if pyxel.btn(pyxel.KEY_S):
            PLAYER_HAND = 0
        if pyxel.btn(pyxel.KEY_A):
            PLAYER_HAND = 1
        if pyxel.btn(pyxel.KEY_D):
            PLAYER_HAND = 2
        if pyxel.btnp(pyxel.KEY_SPACE):
            COM_HAND = random.randint(0,2)
        
        return
        
    def draw(self):
        pyxel.cls(0)

        #COM
        pyxel.text(4,10, "COM",7)
        pyxel.blt(32,10, 0, COM_HAND * 16,0, 16,16,0)

        #PLAYER
        pyxel.text(4,32, "YOU",7)
        pyxel.blt(32,32, 0,  PLAYER_HAND * 16,0, 16,16, 0)
        
        return

App()
