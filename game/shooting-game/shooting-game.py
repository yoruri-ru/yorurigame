import pyxel

class App:
    def __init__(self):
        pyxel.init(100, 100)

        # リソースファイルの読み込み
        pyxel.load("shooting-game.pyxres")
        
    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

        # イメージの描画：(x, y, img, u, v, w, h, [colkey])
        # xy:コピー先の座標、img:イメージバンクの番号
        # uv:コピー元の座標、wh:コピー範囲、colkey:透明色
        pyxel.blt(0, 0, 0, 0, 0, 16, 16, 0)

App().run()
