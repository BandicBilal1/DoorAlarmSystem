import serial
from datetime import datetime
from db_connection import DatabaseConnection



def main():
    arduino = serial.Serial(port="COM4", baudrate=9600, timeout=.1)
    db = DatabaseConnection()
    previous_signal = ""
    while True:
        signal = arduino.read().decode("utf-8")
        arduino.reset_input_buffer()
        if signal != "" and signal != previous_signal:
            db.save(datetime.utcnow().isoformat())
        previous_signal = signal


if __name__ == "__main__":
    main()