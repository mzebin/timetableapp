from datetime import datetime


def get_today():
    today = datetime.now()
    return today.strftime("%A").upper()


def is_current_time_between(start_time, end_time):
    current_time = datetime.now().time()

    start_time_obj = datetime.strptime(start_time, "%H:%M").time()
    end_time_obj = datetime.strptime(end_time, "%H:%M").time()

    if start_time_obj <= current_time < end_time_obj:
        return True
    else:
        return False
