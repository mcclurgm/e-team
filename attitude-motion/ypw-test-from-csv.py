from simplified1_no_drag import Localizer
from csv_parse import data_meters

drone_data = data_meters()
drone_meters = drone_data.meter_data
localizer = Localizer()

# gps updates every 1/20 s
time_step = 0.05

count = 0
for refresh in drone_meters:
    print time_step
    # gps_x = 
    localizer.update(refresh[2], refresh[3], time_step)
    print "round: pitch: " + str(refresh[2]) + " roll: " + str(refresh[3])
    print "       x: " + str(localizer.x) + " y: " + str(localizer.y)
    print "       n: " + str(refresh[1]) + " e: " + str(refresh[0])
    print "       vx: " + str(localizer.vx) + " vy: " + str(localizer.vy)
    count += 1
    if count == 10:
        break