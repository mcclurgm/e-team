from simplified1_no_drag import Localizer
from csv_parse import data_meters

drone_data = data_meters()
drone_meters = data_meters.meter_data
localizer = Localizer()

# gps updates every 1/20 s
time_step = 1/20

vx = 0
vy = 0
x = 0
y = 0

for refresh in drone_meters:
    # gps_x = 
    pass