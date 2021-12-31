import random
import logging
import threading
import concurrent.futures
import time
import queue    

# Дополнительные объекты: 
# 1---threading.Semaphore Внутренний счетчик увеличивается 
# при вызове .release() и уменьшается при вызове .acquire(). 
# Следующее специальное свойство заключается в том, что если 
# поток вызывает .acquire(), когда счетчик равен нулю, этот поток
#  будет блокироваться, пока другой поток не вызовет .release() 
# и увеличит счетчик до единицы.

# 2---threading.Timer это способ запланировать функцию, 
# которая будет вызвана по истечении определенного времени. 
# Вы создаете таймер, передавая количество секунд ожидания и функцию для вызова:
# t = threading.Timer(30.0, my_function)
# Таймер запускается методом .start()
# Если вы хотите остановить уже запущенный таймер, 
# вы можете отменить его, вызвав .cancel()

# 2---threading.Barrier При создании Barrier вызывающая сторона должна 
# указать, сколько потоков будет синхронизироваться на нем. 
# Каждый поток вызывает .wait() в Barrier

def producer(pipeline, semaphore):
    """Pretend we're getting a message from the network."""
    semaphore.acquire()
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.put(message)
    
    logging.info("Producer reveived EXIT event. Exiting")
    semaphore.release()

def consumer(num, pipeline, semaphore):
    """ Pretend we're saving a number in the database. """
    semaphore.acquire()
    waiting_mess = True
    while not event.is_set() or not pipeline.empty():
        try:
            time.sleep(0.001)
            message = pipeline.get(block=False)
        except queue.Empty:
            continue
        logging.info(f'Consumer {num} storing message: {message} (queue size={pipeline.qsize()})')

    logging.info(f"Consumer {num} received EXIT event. Exiting")
    semaphore.release()
    # pipeline.task_done()


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)
    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    semaphore = threading.Semaphore(2)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, semaphore)   
        executor.submit(consumer, 1, pipeline, semaphore)
        executor.submit(consumer, 2, pipeline, semaphore)

        time.sleep(0.07)
        logging.info("Main: about to set event")
        event.set()
        print('Done')
        # time.sleep(2)
        # pipeline.put('end')
