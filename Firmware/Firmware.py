import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap


keyboard  = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.col_pins = (board.D4, board.D5, board.D8, board.D9)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [
    [
        KC.N1,      KC.N2,      KC.N3,      KC.N4,       # Row 0
        KC.N5,      KC.N6,      KC.N7,      KC.N8,       # Row 1
        KC.N9,      KC.N0,      KC.DELETE,  KC.ENTER,    # Row 2
        KC.A,       KC.B,       KC.MPRV,    KC.MNXT,     # Row 3
    ]
]


if __name__ == '__name__':
        keyboard.go()