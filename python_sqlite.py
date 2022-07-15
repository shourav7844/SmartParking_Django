import serial
import sqlite3
import time
import numpy
import itertools
# establish connection to sqlite
try:
    dbConn = sqlite3.connect('db.sqlite')
# open a cursor to the database
    cursor = dbConn.cursor()
    print('success')
except:
    print('failed')
device = 'COM3' #this will have to be changed to the serial port you are using
try:
    print ("Trying...",device) 
    arduino = serial.Serial(device, 9600)
    # arduino = serial.Serial(port='COM9', baudrate=115200, timeout=.1)
except: 
    print ("Failed to connect on",device)

data_xxx ='XXX'
while True:
    time.sleep(1)
    try:
        # Getting the data from rfid to arduino, then arduino to laptop via COM3
        data_raw=arduino.readline()
        print('raw data:', data_raw)


        try:

            cursor = dbConn.cursor()

            # Fetching the info of the slot
            slot_status = cursor.execute("""SELECT veh_number FROM vehicleStatus WHERE slot = 'Slot 1'""")            
            slot1 = cursor.fetchall()
            slot1_previous_condition = list(itertools.chain(*slot1))
            print('slot condition:',slot1_previous_condition[0])

            # Getting trimmed data
            data1 = numpy.char.lstrip(str(data_raw), chars="b'")
            data = numpy.char.rstrip(str(data1), chars=" \r\n'")
            print(data)

            slot_vehicle_number_raw = cursor.execute("""SELECT veh_number FROM vehicle_rfid WHERE rfid_no = (?)""", (str(data),))            
            slot1_vehicle_number = cursor.fetchall()
            new_data_for_slot = list(itertools.chain(*slot1_vehicle_number))

            print('slot vehicle number:',new_data_for_slot[0])

            if slot1_previous_condition[0] == new_data_for_slot[0]:
                    cursor.execute("""UPDATE vehicleStatus SET veh_number = (?),status = False WHERE slot = 'Slot 1'""", (str(data_xxx),))
                    print('inserted ', data_xxx)
                    dbConn.commit()
            else:
                    cursor.execute("""UPDATE vehicleStatus SET veh_number = (?), status = True WHERE slot = 'Slot 1'""", (str(new_data_for_slot[0]),))
                    print('inserted ', new_data_for_slot[0])
                    dbConn.commit()

            print('insertion success')
            dbConn.commit()
            cursor.close()
        except:
            print('failed to insert')
    except:
        print('processing')
        
