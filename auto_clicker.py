import pyautogui
import time


def auto_click(num_clicks, delay):
    init_delay = 10
    print(f"Auto clicker will start {init_delay}s. Move the mouse!")
    time.sleep(init_delay)

    pyautogui.click(clicks=num_clicks, interval=0.00001)


if __name__ == "__main__":
    num_clicks = 1000
    delay = 1

    auto_click(num_clicks, delay)
