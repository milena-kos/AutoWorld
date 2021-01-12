from pynput.keyboard import Key, Controller as KeyboardController
from time import sleep
import simpleaudio as sa
keyboard = KeyboardController()
f = open('country.txt', 'r')
sleep(3)
filename = 'cooldown.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
sleep(2.8)
for line in f:
    keyboard.type(line)
play_obj.wait_done()