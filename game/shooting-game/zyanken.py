import pyxel

class App:
    
    def __init__(self):
        pyxel.init(240, 160, title="Pyxel Shooter r")
        pyxel.load("zyanken.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        return

    def draw(self):
        pyxel.cls(0)
        return

App()
