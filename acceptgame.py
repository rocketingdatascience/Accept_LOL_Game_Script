import pyautogui
import time

def find_accept_button():
    accept_button_location = None

    print('Looking for the button...')
    while accept_button_location is None:
        try:
            # look for the button on the screen
            accept_button_location = pyautogui.locateOnScreen(r'accept.png', confidence=0.7)
        except Exception as e:
            # prevent errors from stopping the program
            pass
        time.sleep(1)

    print("Button found!")
    return accept_button_location

def click_button(button_location):
    # click the button
    button_center = pyautogui.center(button_location)
    pyautogui.click(button_center)
    print("Button clicked!")

def main():
    while True:
        # keep looking for the button and click it
        accept_button_location = find_accept_button()
        click_button(accept_button_location)

if __name__ == "__main__":
    main()
