import time
from plyer import notification


if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERTA!!!",
            message = "soy un hacker",
            timeout = 10
        )

        time.sleep(3600)