import _thread
import time

class Dispatcher:
    def __init__(self, queue, odd_queue, even_queue):
        self.queue = queue
        self.odd_queue = odd_queue
        self.even_queue = even_queue
        self.keep_going = True

    def start(self):
        _thread.start_new_thread(self.run, ())

    def stop(self):
        self.keep_going = False

    def run(self):
        while self.keep_going:
            if self.queue:
                message = self.queue.get()
                if message.number % 2:
                    self.odd_queue.put(message)
                else:
                    self.even_queue.put(message)
            time.sleep(0.00001)

