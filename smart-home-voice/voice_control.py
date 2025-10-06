# voice_control.py
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import numpy as np
import json
import os
import threading

def start_voice_listener(callback, model_path="model/"):
    """Starts a background voice recognition thread."""
    if not os.path.exists(model_path):
        print("❌ Vosk model not found at:", model_path)
        return

    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    def listener():
        def audio_callback(indata, frames, time, status):
            audio_data = (indata * 32767).astype(np.int16).tobytes()
            if recognizer.AcceptWaveform(audio_data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").strip().lower()
                if text:
                    callback(text)

        with sd.InputStream(
            samplerate=16000, channels=1, dtype='float32',
            blocksize=8000, callback=audio_callback
        ):
            while True:
                pass

    threading.Thread(target=listener, daemon=True).start()
