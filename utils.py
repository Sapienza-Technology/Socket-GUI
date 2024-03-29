import json
import logging
import sys
import threading

APP_NAME = "Tech Team Rover"
PORT = 12345
ROVER_UUID = "4b7caa5d-2634-44f3-ad62-5ffb1e08d73f"


def init_logger():
    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setFormatter(logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s"))
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)


def check_load_json(data):
    if data.startswith("<") and data.endswith(">"):
        logging.info("Received test message: " + data)
        return None
    lb = data.count("{")
    rb = data.count("}")
    if lb != rb or lb == 0 or data[0] != "{" or data[len(data) - 1] != "}":
        logging.warning("Corrupted Json")
        return None
    count = 0
    for i in range(len(data)):
        if data[i] == "{":
            count += 1
        elif data[i] == "}":
            count -= 1
        if count == 0 and (i + 1) != len(data) and i != 0:
            logging.warning("Corrupted Json")
            return None
    return json.loads(data)


class RoverNotConnectedError(Exception):
    pass


class RoverInvalidOperation(Exception):
    pass


def InterruptableEvent():
    e = threading.Event()

    def patched_wait():
        while not e.is_set():
            e._wait(3)

    e._wait = e.wait
    e.wait = patched_wait
    return e
