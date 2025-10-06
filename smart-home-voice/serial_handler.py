# serial_handler.py
import serial
import time

def init_serial(port='COM6', baudrate=9600):
    """Initialize serial communication."""
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)
        print("✅ Serial connected on", port)
        return ser
    except Exception as e:
        print("⚠️ Serial not connected:", e)
        return None

def send_serial(ser, mode, value):
    """Send encoded data over serial."""
    if not ser:
        return
    try:
        if mode == "fan":
            ser.write(b'F' + bytes([value]))
        elif mode == "light":
            ser.write(b'L' + bytes([value]))
        elif mode == "servo":
            ser.write(b'S' + bytes([value]))
    except Exception as e:
        print("⚠️ Serial error:", e)
