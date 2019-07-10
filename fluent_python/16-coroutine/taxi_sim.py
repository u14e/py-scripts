# @Author: u14e
# @Time  : 2019/6/27 17:09
# @description:
import queue
import random
from collections import namedtuple

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

# time 字段是事件发生时的仿真时间
# proc 字段是出租车进程实例的编号
# action 字段是描述活动的字符串
Event = namedtuple('Event', ['time', 'proc', 'action'])

def taxi_process(ident, trips, start_time=0):
    """
    一辆出租车的运营过程。
    :param ident: 出租车编号
    :param trips: 行程数量
    :param start_time:
    :return:
    """
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')

class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            first_event = proc.send(None)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * '   ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))

def compute_duration(previous_action):
    """Compute action duration using exponential distribution"""
    if previous_action in ['leave garage', 'drop off passenger']:
        # new state is prowling
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # new state is trip
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1

def test_taxi_process():
    taxi = taxi_process(1, 2, 0)
    print(taxi.send(None))
    print(taxi.send(7))
    print(taxi.send(23))
    print(taxi.send(32))
    print(taxi.send(35))
    print(taxi.send(60))

def test_simulator(num_taxis, end_time):
    random.seed(89)
    taxis = {i: taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL)
             for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time)

if __name__ == '__main__':
    # test_taxi_process()
    test_simulator(3, 120)
