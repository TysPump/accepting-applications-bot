"""
Хендлер переработки dict в сообщение

"""

def generate_finish_req_message(data):

    empty = ""

    for step in data:
        empty = empty + f"{step[1]}\n"

    return empty