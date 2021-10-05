import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)

def format_data(data):
    # 0,+8.5400E+02
    d = data.split(',')[1].split('E')
    # 0   +8.5400E   +02
    first = float(d[0])
    second = float(d[1])
    result = first * 10 ** second
    # 5400 * 10 ** 02
    print(result)
    return result

def process_request():
    ser.write(b'PRX\x0D\x0A')
    ser.readline()
    ser.write(b'\x05')
    data = ser.readline()
    if data:
        data = data.decode().strip()
        print(data)
        format_data(data)

if __name__ == '__main__':
    try:
        while True:
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        ser.close()
