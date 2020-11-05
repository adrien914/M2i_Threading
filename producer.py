import time, _thread
from Message import Message


class Producer:

    def __init__(self, queue):
        self.queue = queue
        self.keep_going = True

    def start(self):
        _thread.start_new_thread(self.run, ())

    def stop(self):
        self.keep_going = False

    def run(self):
        i = 0
        while self.keep_going:
            message = Message(i)
            self.queue.put(message)
            i += 1
            time.sleep(0.000001)
