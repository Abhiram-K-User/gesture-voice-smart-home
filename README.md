# 🖐️ Gesture + Voice Controlled Smart Home System

A Python-based **smart home control interface** that uses **hand gestures** and **voice commands** to control electrical devices (like a fan, light, and servo-operated door) via **Arduino**.

---

## 🚀 Features

- ✋ **Gesture Recognition:**  
  Uses MediaPipe to detect hand gestures and map the number of raised fingers to fan/light intensity.

- 🎙️ **Voice Control:**  
  Uses the Vosk offline speech recognition model to detect commands such as:
  - “Neelam fan” → Switch to fan mode  
  - “Neelam light” → Switch to light mode  
  - “Neelam door” → Switch to door/servo mode  

- 🔌 **Arduino Serial Communication:**  
  Sends control signals over serial to an Arduino that adjusts:
  - Fan speed (PWM)
  - Light brightness
  - Door servo angle

- 🪟 **Secure Login Interface:**  
  Basic Tkinter GUI login before system activation.

---

## 🧠 System Architecture

[ Hand Gesture (OpenCV + MediaPipe) ]
│
▼
[ Mode Logic + Serial ]
│
▼
[ Arduino Controls Fan / Light / Door Servo ]
▲
│
[ Voice Commands (Vosk Model + sounddevice) ]


---

## 🛠️ Installation

1. Clone this repository:

   git clone https://github.com/<your-username>/gesture-voice-smart-home.git
   cd gesture-voice-smart-home
Install dependencies:

bash

pip install -r requirements.txt
Download the Vosk model and place it in a folder named model/
You can get it from: Vosk Models

Connect your Arduino to the COM port (COM6 by default).
Adjust the port in serial_handler.py if needed.
