import pyautogui
import time

def type_code_automator(code_text):
    if not code_text:
        return
    
    # Wait 5 seconds so you can click the input box in your target editor
    print("Preparing to type... switch to your target window now!")
    #time.sleep()
    
    # Type the code with the requested interval
    # interval=0.025 mimics fast human typing
    pyautogui.write(code_text, interval=0.005)
    
    print("Typing completed.")