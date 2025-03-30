import speech_recognition as sr
import pyttsx3
import cv2
import numpy as np
import webbrowser
import subprocess
import os
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox
import threading
import sys
import tempfile
import shutil

# Initialize resources globally for efficiency
engine = pyttsx3.init()
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Load YOLO model once
def load_yolo():
    yolo_weights_path = "D:/j/yolov3.weights"
    yolo_cfg_path = "D:/j/yolov3.cfg"
    coco_names_path = "D:/j/coco.names"

    net = cv2.dnn.readNet(yolo_weights_path, yolo_cfg_path)
    with open(coco_names_path, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    return net, classes, output_layers

yolo_net, yolo_classes, yolo_output_layers = load_yolo()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with mic as source:
            print("Calibrating for ambient noise. Please wait...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for 'Hey Jarvis'...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="en-IN").lower()
            if "hey jarvis" in command:
                print("Wake word detected. Listening for your command...")
                speak("I'm listening.")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio, language="en-IN").lower()
                print(f"You said: {command}")
                return command
            else:
                print("Wake word not detected. Waiting...")
                return ""
    except (sr.UnknownValueError, sr.RequestError):
        print("Sorry, I didn't understand that.")
        return ""
    except Exception as e:
        print(f"Microphone error: {e}")
        return ""

def perform_web_search(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    speak(f"Searching for {query} on the web.")
    webbrowser.open(search_url)

def take_screenshot():
    screenshot = pyautogui.screenshot()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    screenshot.save(filename)
    speak("Screenshot taken and saved.")
    messagebox.showinfo("Screenshot", f"Screenshot saved as {filename}")

def start_screen_recording():
    speak("Starting screen recording. Press Q to stop.")
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_filename = f"screen_recording_{timestamp}.avi"
    out = cv2.VideoWriter(output_filename, fourcc, 20.0, screen_size)

    while True:
        frame = np.array(pyautogui.screenshot())
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow('Recording Screen', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    out.release()
    cv2.destroyAllWindows()
    speak(f"Screen recording saved as {output_filename}")

def open_application(app_name):
    speak(f"Opening {app_name}")
    app_name = app_name.strip().lower()
    try:
        if "excel" in app_name:
            subprocess.Popen(['start', 'excel'], shell=True)
        elif "powerpoint" in app_name:
            subprocess.Popen(['start', 'powerpnt'], shell=True)
        elif "power bi" in app_name:
            subprocess.Popen(['start', 'C:\\Program Files\\Microsoft Power BI Desktop\\bin\\PBIDesktop.exe'], shell=True)
        elif "notepad" in app_name:
            subprocess.Popen(['start', 'notepad'], shell=True)
        elif "calculator" in app_name:
            subprocess.Popen(['start', 'calc'], shell=True)
        elif "command prompt" in app_name or "cmd" in app_name:
            subprocess.Popen(['start', 'cmd'], shell=True)
        elif "browser" in app_name or "chrome" in app_name:
            webbrowser.open("https://www.google.com")
        elif "on screen keyboard" in app_name or "keyboard" in app_name:
            subprocess.Popen(['start', 'osk'], shell=True)
        elif "task manager" in app_name:
            subprocess.Popen(['start', 'taskmgr'], shell=True)
        else:
            subprocess.Popen(['start', app_name], shell=True)
    except Exception as e:
        speak(f"Error opening {app_name}. Please check if it is installed.")
        messagebox.showerror("Error", f"Failed to open {app_name}. {e}")

jarvis_running = True # Global variable to control the loop

def run_jarvis():
    global jarvis_running
    print("JARVIS is ready. Say 'Hey Jarvis' to give a command.")
    speak("Hello, I am JARVIS. Say 'Hey Jarvis' when you need assistance.")
    while jarvis_running:
        command = listen()
        if not command:
            continue
        elif "exit" in command:
            speak("Goodbye!")
            jarvis_running = False
            break
        elif "take a screenshot" in command:
            take_screenshot()
        elif "start screen recording" in command:
            start_screen_recording()
        elif "search for" in command or "look up" in command:
            query = command.replace("search for", "").replace("look up", "").strip()
            perform_web_search(query)
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            open_application(app_name)
        else:
            print("Command not recognized. Please try again.")
            speak("I'm sorry, I couldn't process your request.")

def stop_jarvis():
    global jarvis_running
    jarvis_running = False
    speak("Stopping JARVIS.")

def start_gui():
    root = tk.Tk()
    root.title("JARVIS - Voice Assistant")
    root.geometry("400x200")
    tk.Label(root, text="Click below to start JARVIS").pack(pady=20)
    tk.Button(root, text="Start JARVIS", command=lambda: threading.Thread(target=run_jarvis).start()).pack(pady=10)
    tk.Button(root, text="Stop JARVIS", command=stop_jarvis).pack(pady=10) # Added Stop Button
    root.mainloop()

# Function to bundle resources
def bundle_resources():
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    data_files = [
        ("yolov3.weights", "D:/j/yolov3.weights"),
        ("yolov3.cfg", "D:/j/yolov3.cfg"),
        ("coco.names", "D:/j/coco.names")
    ]
    temp_dir = tempfile.mkdtemp()
    for dest_file, src_file in data_files:
        shutil.copy(src_file, os.path.join(temp_dir, dest_file))
    os.chdir(temp_dir) # change the working directory to the temp dir
    start_gui()
    os.chdir(base_path) # change back to original dir after app closes
    shutil.rmtree(temp_dir) # delete the temp directory

if __name__ == "__main__":
    bundle_resources()