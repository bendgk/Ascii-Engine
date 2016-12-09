import time
import msvcrt as m
import os

class Input:
    def GetInput(self):
        return m.getch()

    def WaitFor(self, key):
        while m.getch() != key.lower():
            pass
        return True
