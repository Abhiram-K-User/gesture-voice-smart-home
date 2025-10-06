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

