from datetime import datetime
import time
import signal
import logging

class GracefulKiller:
    def __init__(self):
        self.kill_now = False
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        logging.warning('gracefully exiting')
        self.kill_now = True
        raise KeyboardInterrupt

def start():
    g = GracefulKiller()
    logging.warning(f'start state : {g.kill_now}')
    i = 0
    while not g.kill_now:
        logging.warning(i)
        logging.warning(f'start : {datetime.now()}')
        time.sleep(3)
        logging.warning(f'end : {datetime.now()}')
        i += 1
        logging.warning(f'state now : {g.kill_now}')


if __name__ == '__main__':
    start()