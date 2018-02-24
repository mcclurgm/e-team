import csv
from geopy import distance

# this needs to account for orientation of the drone
# if I'm going to test with this data. Its x and mine don't align.
class data_meters():
    def __init__():
        self.degree_data = []
        self.meter_data = []

        with open("solo_data.csv", "rb") as solo_data:
            data_reader = csv.reader(solo_data, delimiter=",")
            data_reader.next()
            refresh = data_reader.next()

            lat_base = float(refresh[0])
            long_base = float(refresh[1])
            pitch_base = float(refresh[2])
            roll_base = float(refresh[3])
            print [lat_base, long_base, pitch_base, roll_base]
            for refresh in data_reader:
                lat = float(refresh[0]) - lat_base
                long = float(refresh[1]) - long_base
                pitch = float(refresh[1]) - pitch_base
                roll = float(refresh[2]) - roll_base

                self.degree_data.append([lat, long, pitch, roll])

        # print self.degree_data

        for row in self.degree_data:
            lat = (0, row[0])
            long = (0, row[1])
            lat_meters = distance.vincenty(0, lat).meters
            long_meters = distance.vincenty(0, long).meters
            # print [lat_meters, long_meters]
            self.meter_data.append[lat_meters, long_meters, row[2], row[3]]

        # print self.meter_data