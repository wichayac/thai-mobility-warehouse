import csv
import datetime
with open('sandbox/milestone_01/sample_probe.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    row_count = 0
    invalid_gps_records = 0
    unique_vehicles = set()
    total_speed = 0
    earliest_timestamp = None

    for row in reader:
        row_count += 1
        if len(row) != 9:
            print("Error: Row does not have 9 columns")
            continue
        VehicleID = row[0]
        gpsvalid = int(row[1])
        lat = float(row[2])
        lon = float(row[3])
        timestamp = datetime.datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
        speed = int(row[5])
        heading = int(row[6])
        for_hire_light = int(row[7])
        engine_acc = int(row[8])
        print(row)
        unique_vehicles.add(VehicleID)
        total_speed += speed
        if earliest_timestamp is None or timestamp < earliest_timestamp:
            earliest_timestamp = timestamp

        if gpsvalid == 0 or gpsvalid == 1:
            print("gpsvalid ok")
        else:
            invalid_gps_records += 1
            print("Error: gpsvalid is not 0 or 1")
        if -90 <= lat <= 90:
            print("lat ok")
        else:
            print("Error: lat is not between -90 and 90")
        if -180 <= lon <= 180:
            print("lon ok")
        else:
            print("Error: lon is not between -180 and 180")
        if 0 <= heading < 360:
            print("heading ok")
        else:
            print("Error: heading is not between 0 and 360")
        if for_hire_light == 0 or for_hire_light == 1:
            print("for_hire_light ok")
        else:
            print("Error: for_hire_light is not 0 or 1")
        if engine_acc == 0 or engine_acc == 1:
            print("engine_acc ok")
        else:
            print("Error: engine_acc is not 0 or 1")

print("Rows: ", row_count)
print("Unique vehicles: ", len(unique_vehicles))
print("Invalid gpsvalid records: ", invalid_gps_records)
print("Average speed: ", total_speed / row_count)
print("Earliest timestamp: ", earliest_timestamp)