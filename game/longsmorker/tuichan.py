import pyxel

#シーン番号の定義
TITLE = 0
PLAY = 1
GAMEOVER= 2
CLEAR = 3

scene = TITLE
frame_tmr = 0
time= 0

clear_time = 0

#タバコの長さ
cigarette = 50



class App:

    def __init__(self):
        pyxel.init(150,78, title="long smorker", fps=25)
        pyxel.load("tuichan.pyxres")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        global scene, frame_tmr, time, cigarette, clear_time
        frame_tmr = frame_tmr + 1
        time = frame_tmr / 25

        if scene == TITLE:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                scene = PLAY
                frame_tmr = 0
                cigarette = 50

        elif scene == PLAY:
            cigarette = cigarette - 0.5

            if cigarette == 0:
                scene = GAMEOVER
            else:
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    clear_time = time
                    scene = CLEAR

        elif scene == GAMEOVER:

            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                scene = TITLE
        else:
            return
        
    def draw(self):
        pyxel.cls(11)
        pyxel.pal(11,6)

        if scene == TITLE:
            pyxel.blt(35,35, 0, 0,0, 8,8, scale=10)
            pyxel.blt(90,40, 0, 0,16, 40,8)
        elif scene == PLAY:
            pyxel.blt(35,35, 0, 8,0, 8,8, scale=10)
            pyxel.rect(29,49, cigarette,10, 7)
            pyxel.line(29 + cigarette, 49,  29 + cigarette,58, 8)
        elif scene == GAMEOVER:
            pyxel.blt(35,35, 0, 16,0, 8,8, scale=10)
            pyxel.text(90,40, "GAME OVER",1)
        elif scene == CLEAR:
            pyxel.text(50,50, str(clear_time), 1)
            
        
        pyxel.text(100,50, str(pyxel.mouse_x), 1)
        pyxel.text(100,60, str(pyxel.mouse_y), 1)

App()
