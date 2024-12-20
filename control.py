import os
import signal
import subprocess

def start_keylogger():
    process = subprocess.Popen(["python", "main.py"])
    with open("log.txt", "w") as pid_file:
        pid_file.write(str(process.pid))
    print("Keylogger started with PID:", process.pid)

def stop_keylogger():
    try:
        with open("log.txt", "r") as pid_file:
            pid = int(pid_file.read())
        os.kill(pid, signal.SIGTERM)
        os.remove("log.txt")
        print("Keylogger stopped.")
    except FileNotFoundError:
        print("Keylogger is not running.")
    except ProcessLookupError:
        print("Process not found.")

if __name__ == "__main__":
    action = input("Enter 'start' to start the keylogger or 'stop' to stop it: ").strip().lower()
    if action == "start":
        start_keylogger()
    elif action == "stop":
        stop_keylogger()
    else:
        print("Invalid action.")