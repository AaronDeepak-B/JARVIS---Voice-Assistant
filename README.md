# 🤖 JARVIS - Voice Assistant

JARVIS is a Python-based AI voice assistant that performs various tasks using voice commands. It can open applications, search the web, take screenshots, and record your screen.

## ✨ Features
- 🗣️ **Voice Commands**: Perform tasks using simple voice commands.
- 🖥️ **Application Control**: Open installed applications using voice.
- 🌐 **Web Search**: Perform Google searches with your voice.
- 📸 **Screenshot**: Capture your screen using a voice command.
- 🎥 **Screen Recording**: Record your screen and save it as a video.

## 🛠️ Requirements
- 🐍 Python 3.8 or higher
- 💻 Virtual Environment (optional but recommended)

### 📦 Install Dependencies
Run the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

### 📚 Packages Used
- `speech_recognition` for voice input
- `pyttsx3` for text-to-speech
- `cv2` and `numpy` for screen recording
- `pyautogui` for screenshots
- `subprocess` for application control
- `webbrowser` for web search

## 🚀 Usage
1. Clone this repository:
```bash
git clone https://github.com/your-username/JARVIS.git
cd JARVIS
```

2. Run the Python script:
```bash
python a.py
```

3. You can say commands like:
- 📝 "Open Notepad"
- 🔎 "Search for Iron Man"
- 📸 "Take a screenshot"
- 🎥 "Start recording"
- ⏹️ "Stop recording"
- 🚪 "Exit"

## 🛎️ Troubleshooting
- 🎙️ Ensure your microphone is enabled and permissions are granted.
- 📦 Install `ffmpeg` if screen recording doesn't work.
- ✅ Verify application names are correct when opening apps.

## 🤝 Contributing
Feel free to submit pull requests for new features or bug fixes.
