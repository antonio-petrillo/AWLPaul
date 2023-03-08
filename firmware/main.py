print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.debug_enabled = False

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP4, board.GP5, board.GP6, False),)

keyboard.col_pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP26,
)

keyboard.row_pins = (
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

TRASP   = KC.TRNS
FNLYR   = KC.MO(1)
METALYR = KC.MO(2)
_NONE_  = KC.NO

keyboard.keymap = [
    [
        KC.ESC   , KC.N1   , KC.N2   , KC.N3   , KC.N4   , KC.N5   , KC.N6   , KC.N7   , KC.N8   , KC.N9   , KC.N0   , KC.MINS  , KC.EQL   , KC.BSPC  , _NONE_  , KC.DEL  ,
        KC.TAB   , KC.Q    , KC.W    , KC.E    , KC.R    , KC.T    , KC.Y    , KC.U    , KC.I    , KC.O    , KC.P    , KC.LBRC  , KC.RBRC  , KC.BSLS  , _NONE_  , KC.PGUP ,
        KC.LCTL  , KC.A    , KC.S    , KC.D    , KC.F    , KC.G    , KC.H    , KC.J    , KC.K    , KC.L    , KC.SCLN , KC.QUOT  , _NONE_   , KC.ENT   , _NONE_  , KC.PGDN ,
        KC.LSFT  , KC.Z    , KC.X    , KC.C    , KC.V    , _NONE_  , KC.GRV  , KC.N    , KC.M    , KC.COMM , KC.DOT  , KC.SLSH  , KC.RSFT  , _NONE_   , KC.UP   , _NONE_  ,
        KC.HYPR  , KC.LALT , KC.LGUI , _NONE_  , KC.SPC  , _NONE_  , KC.B  , FNLYR   , _NONE_  , KC.RALT , _NONE_  , METALYR  , KC.RCTL  , KC.LEFT  , KC.DOWN , KC.RGHT ,
    ],
    [
        KC.ESC   , KC.F1   , KC.F2   , KC.F3   , KC.F4   , KC.F5   , KC.F6   , KC.F7   , KC.F8   , KC.F9   , KC.F10  , KC.F11   , KC.F12   , TRASP    , _NONE_  , TRASP   ,
        KC.TAB   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP    , TRASP    , TRASP    , _NONE_  , TRASP   ,
        KC.LCTRL , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , KC.LEFT , KC.DOWN , KC.UP   , KC.RGHT , TRASP   , TRASP    , TRASP    , TRASP    , _NONE_  , TRASP   ,
        KC.LSFT  , TRASP   , TRASP   , TRASP   , TRASP   , _NONE_  , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP    , TRASP    , _NONE_   , TRASP   , _NONE_  ,
        KC.HYPR  , TRASP   , TRASP   , _NONE_  , TRASP   , _NONE_  , TRASP   , TRASP   , _NONE_  , TRASP   , _NONE_  , TRASP    , TRASP    , TRASP    , TRASP   , TRASP   ,
    ],
    [
        KC.ESC   , KC.F13  , KC.F14  , KC.F15  , KC.F16  , KC.F17  , KC.F18  , KC.F19  , KC.F20  , KC.F21  , KC.F22  , KC.F23   , KC.F24   , TRASP    , _NONE_   , TRASP  ,
        KC.TAB   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP    , TRASP    , TRASP    , _NONE_   , TRASP   ,
        KC.LCTRL , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , KC.LEFT , KC.DOWN , KC.UP   , KC.RGHT , TRASP   , TRASP    , TRASP    , TRASP    , _NONE_   , TRASP   ,
        KC.LSFT  , TRASP   , TRASP   , TRASP   , TRASP   , _NONE_  , TRASP   , TRASP   , TRASP   , TRASP   , TRASP   , TRASP    , TRASP    , _NONE_   , TRASP    , _NONE_  ,
        KC.HYPR  , TRASP   , TRASP   , _NONE_  , TRASP   , _NONE_  , TRASP   , TRASP   , _NONE_  , TRASP   , _NONE_  , TRASP    , TRASP    , TRASP    , TRASP    , TRASP   ,
    ]
]

encoder_handler.map = (
    ((KC.VOLU, KC.VOLD, KC.MUTE),),
    ((KC.BRIU, KC.BRID, KC.PSCR),),
)
keyboard.modules.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()
