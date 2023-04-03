import flow
import scheduler
from network import network

if __name__ == '__main__':
    # print(1)
    scheduler = scheduler.StaPriScheduler()
    network()
    scheduler.run()

