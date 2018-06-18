from adafruit_blinka import agnostic

if agnostic.microcontroller == "esp8266":
    from adafruit_blinka.microcontroller.esp8266.pin import *
elif agnostic.microcontroller == "stm32":
    from adafruit_blinka.microcontroller.stm32.pin import *
elif agnostic.microcontroller == "linux":
    if agnostic.board == "raspi_3" or agnostic.board == "raspi_2":
        print("import raspi23")
        from adafruit_blinka.microcontroller.raspi_23.pin import *
    else:
        raise NotImplementedError("Board not supported: ", agnostic.board)
else:
    raise NotImplementedError("Microcontroller not supported")
