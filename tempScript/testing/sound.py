# https://stackoverflow.com/questions/16573051/sound-alarm-when-code-finishes

import winsound
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)