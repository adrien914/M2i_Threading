import sys, time, _thread


class Consummer:
    def __init__(self, queue):
        self.queue = queue
        self.keep_going = True

    def start(self):
        _thread.start_new_thread(self.run, ())

    def stop(self):
        self.keep_going = False

    def run(self):
        while self.keep_going:
            if self.queue:
                print(self.queue.get().content())
            time.sleep(0.00001)

