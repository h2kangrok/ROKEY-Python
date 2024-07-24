import time
import datetime


def current_time():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_time


def sleep_for(seconds):
    time.sleep(seconds)


def time_elapsed(start_time):
    current_time = time.time()
    return current_time - start_time
