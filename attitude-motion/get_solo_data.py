from dronekit import connect
import sys
import time

class Solo():
    """docstring for ."""
    def __init__(self, virtual=False):
        self.vehicle = None
        self.connected = False

    def connect(self):
        # Connect to UDP endpoint (and wait for default attributes to accumulate)
        target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
        print('Connecting to ' + target + '...')
        self.vehicle = connect(target, wait_ready=True)
        self.connected = True
        if not self.vehicle:
            print('bad.')


    def get_state(self):
        if not self.connected:
            print('vehicle not connected. Call .connect to connect.')
            return

        pos = self.vehicle.location.global_frame
        imu = self.vehicle.attitude

        return map(str, (pos.lat, pos.lon, imu.pitch, imu.roll))

def main():
    vehicle = Solo()
    vehicle.connect()

    out = 'latitutde, longitude, pitch, roll\n'

    try:
        while True:
            state = ','.join(vehicle.get_state())
            print(state)
            out += state + '\n'
            time.sleep(0.05)
    except KeyboardInterrupt:
        with open('solo_data4.csv', 'w') as f:
            f.write(out)

    print("Done.")


if __name__ == "__main__":
    main()
