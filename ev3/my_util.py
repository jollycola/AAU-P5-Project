''' Utility functions '''
from threading import Thread

from pybricks import ev3brick as brick


def play_sound_in_background(sound, volume: int = 100):
    ''' Play sound in background thread '''
    Thread(target=brick.sound.file, args=(sound, volume)).start()
