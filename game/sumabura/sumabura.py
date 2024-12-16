import pyxel

class App:

    def __init__(self):
        pyxel.init(80, 64, title="スマブラ", fps="32")
        pyxel.load("sumabura.pyxres")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        return

    def draw(self):
        pyxel.cls(0)

        pyxel.blt(32,32, 0, 16,0, 32,16, 0)


App()