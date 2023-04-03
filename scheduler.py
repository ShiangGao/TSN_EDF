# 静态优先级调度器类
import time

from flow import random_get_TT


class StaPriScheduler:

    # 初始化流的队列
    def __init__(self):
        self.streams = []
        self.currentTime = 0
        self.TTFlow, self.hp = random_get_TT(3)
    # # 添加流实例到堆中
    # def add_stream(self, stream):
    #     self.streams.append(stream)

    def get_next_stream(self):
        ready_Stream = []
        for stream in self.TTFlow:
            if self.currentTime % stream.period == 0:
                stream.ready = True
            if stream.ready:
                ready_Stream.append(stream)
        if not ready_Stream:
            pass
        else:
            ready_Stream.sort(key=lambda x: (x.next_deadline, x.priority))
            return ready_Stream[0]
        return None

    # 运行流
    def run(self):
        while self.currentTime <= 2 * self.hp:
            stream = self.get_next_stream()
            if not stream:
                self.currentTime += 1
                time.sleep(0.1)
                continue
            print(f"random flow id:{stream.name} period:{stream.period} priority:{stream.priority} slot:{stream.slot}")
            start_time = self.currentTime
            end_time = start_time + stream.slot
            print(f"{stream.name} scheduled from {start_time} to {end_time}")
            time.sleep(0.1)
            stream.start_time = stream.next_deadline
            stream.next_deadline += stream.period
            stream.ready = False  # 将流变为挂起态
            self.currentTime = end_time
