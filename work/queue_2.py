# -*- coding: utf-8 -*-
import threading, time, random, datetime, sys
import queue
# переменная для имитации разовой ошибки
err=False

class Worker(threading.Thread):
    """
    Класс потока который будет брать задачи из очереди и выполнять их до успешного
    окончания или до исчерпания лимита попыток
    """
    def __init__(self, queue, output):
        # Обязательно инициализируем супер класс (класс родитель)
        super(Worker,self).__init__()
        # Устанавливаем поток в роли демона, это необходимо что бы по окончании выполнения
        # метода run() поток корректно завершил работу,а не остался висеть в ожидании
        self.setDaemon(True)
        # экземпляр класса содержит в себе очередь что бы при выполнении потока иметь к ней доступ
        self.queue=queue
        self.output=output
    
    def run(self):
        """
        Основной код выполнения потока должен находиться здесь
        """
        while True:
            try:
                # переменная для иммитации единичной ошибки во время выполнения потока
                global err
                # фиксируем время начала работы потока
                start=datetime.datetime.now().strftime('%H:%M:%S')
                # запрашиваем из очереди объект
                target=self.queue.get(block=False)
                print('%s get target: %s'%(self.getName(), target))
                
                # эмулируем однократно возникающую ошибку
                if ((target==2) and (not err)):
                    err=True
                    raise Exception('test error')
                
                # делаем видимость занятости потока
                # путем усыпления его на случайную величину
                sleep_time=random.randint(0,10)
                time.sleep(sleep_time)
                print('%s %s target: %s sleep %ss'%(start, self.getName(), target, sleep_time))
                # сообщаем о том что задача для полученного объекта из очереди выполнена
                self.output.put(target, block=False)
                self.queue.task_done()
            # После того как очередь опустеет будет сгенерировано исключение
            except queue.Empty:
                sys.stderr.write('%s get Queue.EMPTY exception\r\n'%self.getName())
                break
            # если при выполнении потока будет сгенерировано исключение об ошибке,
            # то оно будет обработано ниже
            except Exception as e:
                self.queue.task_done()
                # выводим на экран имя потока и инфо об ошибке
                sys.stderr.write('%s get %s exception\r\n'%(self.getName(), e))
                # Предполагаем раз объект из очереди не был корреткно обработан,
                # то добавляем его в очередь
                self.queue.put(target, block=False)

class Test(object):
    def __init__(self, data, number_threads):
        # создаем экземпля класса очереди Queue
        self.queue=queue.Queue()
        self.output=queue.Queue()
        # заполняем очередь
        for item in data:
            self.queue.put(item)
        # определяем количество потоков которые будут обслуживать очередь
        self.NUMBER_THREADS=number_threads
        # список экземпляров класса потока, в последствии можно
        # обратиться к нему что бы получать сведения о состоянии потоков
        self.threads=[]
        
    def execute(self):
        # создаем экземпляра классов потоков и запускаем их
        for i in range(self.NUMBER_THREADS):
            self.threads.append(Worker(self.queue, self.output))
            self.threads[-1].start()
        
        # Блокируем выполнение кода до тех пор пока не будут выполнены все
        # элементы очереди. Это означает что сколкьо раз были добавлены элементы
        # очереди, то столько же раз должен быть вызван task_done().
        self.queue.join()
if __name__=="__main__":
    t=datetime.datetime.now()
    test=Test(range(20), 3)
    test.execute()
    print('the end in %s'%(datetime.datetime.now()-t))
    # вывод debug информации
    print(len(list(test.output.__dict__['queue'])))
    print(sorted(list(test.output.__dict__['queue'])))