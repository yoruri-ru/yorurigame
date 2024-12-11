import pyxel

class App:
    
    def __init__(self):
        pyxel.init(80, 64, title="Pyxel Shooter r")
        pyxel.load("zyanken.pyxres")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        return

    def draw(self):
        pyxel.cls(0)

        #COM
        pyxel.text(4,10, "COM",7)
        pyxel.blt(32,10, 0, 0,0, 16,16,0)

        #PLAYER
        pyxel.text(4,32, "YOU",7)
        pyxel.blt(16,32, 0,  0,0, 16,16, 0)
        pyxel.blt(32,32, 0, 16,0, 16,16, 0)
        pyxel.blt(48,32, 0, 32,0, 16,16, 0)
        
        return

App()
