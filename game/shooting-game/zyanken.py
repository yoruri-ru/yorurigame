import pyxel

com_hand = 0
player_hand = 0
state = 0
result = ""

TITLE = 0
PLAY = 1
END = 2
scene = TITLE
class App:
    
    def __init__(self):
        pyxel.init(80, 64, title="zyanken", fps=25)
        pyxel.load("zyanken.pyxres")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def check():
        ret =False
        x = pyxel.mouse_x
        y = pyxel.mouse_y
        if 16 <= x and x < 64 and 44 <= y and y < 60:
            ret = True
        return ret

    def update(self):
        global com_hand, player_hand, state, result
        if state == 0:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and App.check():
                player_hand = int(pyxel.mouse_x / 16) -1
                com_hand = pyxel.rndi(0,2)
                state = 1
            else:
                com_hand = int(pyxel.frame_count /5) % 3
        elif state == 1:
            if com_hand == player_hand:
                result = "DRAW"
            elif com_hand == 0:
                if player_hand == 1:
                    result = "LOSE"
                else:
                    result = "WIN"
            elif com_hand == 1:
                if player_hand == 2:
                    result = "LOSE"
                else:
                    result = "WIN"
            elif com_hand == 2:
                if player_hand == 0:
                    result = "LOSE"
                else:
                    result = "WIN"

            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                state = 0
        
    def draw(self):
        pyxel.cls(0)

        #COM
        pyxel.text(4,3, "COM",7)
        pyxel.blt(32,3, 0, com_hand * 16,0, -16,16,0)

        #PLAYER
        pyxel.text(4,44, "YOU",7)
        if state == 0:
            pyxel.pal(11, 0)
            pyxel.blt(16,44, 0, 0,0, 16,16, 0)
            pyxel.blt(32,44, 0, 16,0, 16,16, 0)
            pyxel.blt(48,44, 0, 32,0, 16,16, 0)
        else:
            pyxel.blt(32,44, 0, player_hand * 16,0, 16,16, 0)
            pyxel.text(34,28, result, 7)

App()
