from adafruit_blinka import Enum, agnostic
from adafruit_blinka.agnostic import board as boardId

class Pin(Enum):
    def __init__(self, id):
        """Identifier for pin, referencing platform-specific pin id"""
        self.id = id

    def __repr__(self):
        import board
        for key in dir(board):
            if getattr(board, key) is self:
                return "board.{}".format(key)
        import microcontroller.pin as pin
        for key in dir(pin):
            if getattr(pin, key) is self:
                return "microcontroller.pin.{}".format(key)
        return repr(self)


if agnostic.microcontroller == "esp8266":
    from adafruit_blinka.microcontroller.esp8266 import *
elif agnostic.microcontroller == "stm32":
    from adafruit_blinka.microcontroller.stm32 import *
elif agnostic.microcontroller == "linux":
    if boardId == "raspi_3" or boardId == "raspi_2":
        from adafruit_blinka.microcontroller.raspi_23 import *
    else:
        raise NotImplementedError("Board not supported: ", boardId)
else:
    raise NotImplementedError("Microcontroller not supported: ", agnostic.microcontroller)
