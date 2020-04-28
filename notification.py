import time


def notification(start_time, time_checker):
    if time.time() - start_time > 15:
        if time_checker == 3:
            print("more than 15 seconds elapsed")
        return 4

    elif time.time() - start_time > 10:
        if time_checker == 2:
            print("more than 10 seconds elapsed")
        return 3

    elif time.time() - start_time > 7:
        if time_checker == 1:
            print("more than 7 seconds elapsed")
        return 2

    elif time.time() - start_time > 2:
        if time_checker == 0:
            print("more than 2 seconds elapsed")
        return 1

    return 0
