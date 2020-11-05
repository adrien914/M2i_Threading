from producer import Producer
from consummer import Consummer
from dispatcher import Dispatcher
import queue


main_queue = queue.Queue()
odd_queue = queue.Queue()
even_queue = queue.Queue()
producer = Producer(main_queue)
dispatcher = Dispatcher(main_queue, odd_queue, even_queue)
odd_consummer = Consummer(odd_queue)
even_consummer = Consummer(even_queue)

producer.start()
dispatcher.start()
odd_consummer.start()
#even_consummer.start()
input()
producer.stop()
odd_consummer.stop()
even_consummer.stop()
dispatcher.stop()
