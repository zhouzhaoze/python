from os import system
import threading

interval = 3600;

class auto_locker:
    def __init__(self, interval):
        self.interval = interval
    def lock(self):
        system('rundll32.exe user32.dll, LockWorkStation')
        #print('hello world')
        self.t = threading.Timer(self.interval, self.lock)
        self.t.start()
    def start(self):
        self.t = threading.Timer(self.interval, self.lock)
        self.t.start()

def main():
    al = auto_locker(interval)
    al.start()

if __name__ == '__main__':
    main()
