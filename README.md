# 🤖 JARVIS - Voice Controlled Personal Assistant 🗣️

This project is a voice-controlled personal assistant named JARVIS, built using Python. It allows users to automate various tasks on their Windows PC through voice commands. 💻

## ✨ Features

* **Voice Control 🎤:** Uses speech recognition to understand user commands.
* **Web Search 🌐:** Performs web searches using Google.
* **Application Launching 🚀:** Opens specified applications.
* **Screenshot Capture 📸:** Takes and saves screenshots.
* **Screen Recording 🎬:** Records the screen and saves it as an AVI file.
* **Object Detection 👁️:** Uses YOLOv3 to detect objects from webcam input.
* **Graphical User Interface (GUI) 🖼️:** Provides a user-friendly interface using Tkinter.
* **Stop Functionality 🛑:** Has a stop button to terminate the application.

## 🛠️ Technologies Used

* **Python 🐍:** The primary programming language.
* **speech_recognition 🗣️➡️📝:** For speech-to-text conversion.
* **pyttsx3 📝➡️🗣️:** For text-to-speech conversion.
* **opencv-python 📷:** For image processing and object detection.
* **numpy 🔢:** For numerical computations.
* **pyautogui 🖱️⌨️:** For automating mouse and keyboard actions.
* **tkinter 🖼️:** For the GUI.
* **PyInstaller 📦:** For creating the executable.
* **YOLOv3 🎯:** For object detection.

## ⚙️ Prerequisites

Before running the application, ensure you have the following installed:

* Python 3.x 🐍
* The required Python libraries (install using `pip install -r requirements.txt`).

## 📦 Installation

1.  **Clone the Repository 📥:**

    ```bash
    git clone [repository URL]
    cd JARVIS
    ```

2.  **Install Dependencies ⬇️:**

    ```bash
    pip install speech_recognition pyttsx3 opencv-python numpy pyautogui tkinter
    ```

3.  **Download YOLOv3 Files 📥:**

    * Download `yolov3.weights`, `yolov3.cfg`, and `coco.names` and place them in the `D:\j\` directory. 📂

4.  **Create Executable (Optional) 🚀:**

    * If you want to create a standalone executable, use PyInstaller.
    * Navigate to the project directory in your terminal.
    * Run the following command:

        ```bash
        pyinstaller --onefile --windowed --add-data "D:\j\yolov3.weights;." --add-data "D:\j\yolov3.cfg;." --add-data "D:\j\coco.names;." b.py
        ```

    * The executable will be created in the `dist` folder. 📁

## 🚀 Usage

1.  **Run the Application ▶️:**

    * If you created an executable, double-click `b.exe` from the `dist` folder.
    * Otherwise, run `b.py` using Python:

        ```bash
        python b.py
        ```

2.  **Use the GUI 🖱️:**

    * Click the "Start JARVIS" button to begin voice control. 🔊
    * Say "Hey Jarvis" to activate the assistant, followed by your command. 🗣️
    * Click the "Stop JARVIS" button to terminate the application. 🛑

## ⚠️ Important Notes

* The application relies on the YOLO files being in the `D:\j\` directory. 📂
* If you move the executable or run it on another computer, ensure the YOLO files are also in `D:\j\`. 📂
* The application requires microphone access. 🎤

## 🤝 Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request. 🛠️
