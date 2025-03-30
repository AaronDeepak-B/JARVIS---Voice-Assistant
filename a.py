import speech_recognition as sr
import pyttsx3
import cv2
import numpy as np
import os
import webbrowser
import subprocess

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    try:
        with mic as source:
            print("Calibrating for ambient noise. Please wait...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="en-IN")
            print(f"You said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Speech service is unavailable.")
        speak("Speech service is currently unavailable.")
        return ""
    except Exception as e:
        print(f"Microphone error: {e}")
        speak("There was an error with the microphone.")
        return ""

def perform_web_search(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    speak(f"Searching for {query} on the web.")
    print(f"Opening browser to search for: {query}")
    webbrowser.open(search_url)

def open_application(app_name):
    speak(f"Opening {app_name}")
    try:
        if "command prompt" in app_name or "cmd" in app_name:
            subprocess.run("cmd")
        elif "notepad" in app_name:
            subprocess.run("notepad")
        elif "browser" in app_name or "chrome" in app_name:
            webbrowser.open("https://www.google.com")
        elif "vlc" in app_name:
            subprocess.run("vlc")
        elif "calculator" in app_name:
            subprocess.run("calculator")
        elif "task-manager" in app_name:
            subprocess.run("task-manager")
        else:
            speak("I couldn't find the application.")
    except Exception as e:
        speak(f"Error opening {app_name}")
        print(f"Error: {e}")

def load_yolo():
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    return net, classes, output_layers

def start_camera(object_detection=False, confidence_threshold=0.5):
    net, classes, output_layers = load_yolo() if object_detection else (None, None, None)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    print("Camera is on. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        if object_detection:
            height, width, _ = frame.shape
            blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)
            
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > confidence_threshold:
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        label = f"{classes[class_id]}: {confidence:.2f}"
                        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        cv2.imshow('JARVIS Vision', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    print("JARVIS is ready. You can talk to me freely, ask questions, or give commands.")
    speak("Hello, I am JARVIS. How can I assist you today?")
    while True:
        command = listen()
        if "exit" in command:
            speak("Goodbye!")
            break
        elif "camera" in command and "object" in command:
            speak("Starting object detection.")
            start_camera(object_detection=True)
        elif "camera" in command:
            speak("Activating camera.")
            start_camera()
        elif "search for" in command or "look up" in command:
            query = command.replace("search for", "").replace("look up", "").strip()
            perform_web_search(query)
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            open_application(app_name)
        else:
            print("Command not recognized. Please try again.")
            speak("I'm sorry, I couldn't process your request.")

if __name__ == "__main__":
    main()
