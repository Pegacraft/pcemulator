current: int = 0


def set_counter(value: int):
    global current
    current = value


def increment(value: int):
    global current
    current += value


def get_current():
    global current
    return current
