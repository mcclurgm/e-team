import sys
import csv
from geopy import distance

# this needs to account for orientation of the drone
# if I'm going to test with this data. Its x and mine don't align.


class data_meters():

    def __init__(self):
        self.degree_data = []
        self.meter_data = []

        with open(sys.argv[1], "r") as solo_data:
            data_reader = csv.reader(solo_data, delimiter=",")
            next(data_reader)
            refresh = next(data_reader)
            print(refresh)
            
            lat_base = float(refresh[0])
            long_base = float(refresh[1])
            alt_base = float(refresh[2])
            pitch_base = float(refresh[3])
            roll_base = float(refresh[4])
            yaw_base = float(refresh[5])
            time_base = float(refresh[6])
            for refresh in data_reader:
                lat = float(refresh[0]) - lat_base
                long = float(refresh[1]) - long_base
                alt = float(refresh[2]) - alt_base
                pitch = float(refresh[3]) - pitch_base
                roll = float(refresh[4]) - roll_base
                yaw = float(refresh[5]) - yaw_base
                time = float(refresh[6]) - time_base

                print([lat, long, alt, pitch, roll, yaw, time])

                self.degree_data.append([lat, long, alt, pitch, roll, yaw, time])

        # print self.degree_data
        # Note: distance calculator has error of +/- 0.5%
        for row in self.degree_data:
            lat = (0, row[0])
            long = (0, row[1])
            print("lat {0} long {1}".format(lat, long))
            lat_meters = distance.distance((0,0), (lat,0)).meters
            long_meters = distance.distance((0,0), (0,long)).meters
            # print(row[3])
            # print([lat_meters, long_meters, row[2], row[3]])
            if len(self.meter_data) > 0:
                pass
                # print(row[2] - self.meter_data[-1][2])
            self.meter_data.append([lat_meters, long_meters, row[2], row[3]])

        # print self.meter_data

print(sys.argv)
thing = data_meters()
