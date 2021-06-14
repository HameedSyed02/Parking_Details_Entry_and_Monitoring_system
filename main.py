import cv2
import NoPDetection
import os
import csv
import datetime
import time
import pandas as pd
import numpy as np

def DataEntry(txt):
    Available = 10
    ts = time.time()
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')

    #file creation
    Entry_col_names = ['Number', 'Entry_Date', 'Entry_Time']
    Exit_col_names = ['Number', 'Exit_Date', 'Exit_Time']
    exists = os.path.isfile("ParkingData\EntryData\EntryData_" + date + ".csv")
    if exists:
        pass
    else:
        with open("ParkingData\EntryData\EntryData_" + date + ".csv", 'a+') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(Entry_col_names)
            csvfile.close()
        with open("ParkingData\ExitData\ExitData_" + date + ".csv", 'a+') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(Exit_col_names)
            csvfile.close()
    # File creation ended

    NP = str(txt)

    pd_Entry_data = pd.read_csv("ParkingData\EntryData\EntryData_" + date + ".csv")
    pd_Exit_data = pd.read_csv("ParkingData\ExitData\ExitData_" + date + ".csv")
    Entry_NP_values = np.array(pd_Entry_data['Number'])
    Exit_NP_values = np.array(pd_Exit_data['Number'])
    Entrylist = Entry_NP_values.tolist()
    Exitlist = Exit_NP_values.tolist()
    Entrycount = Entrylist.count(NP)
    Exitcount = Exitlist.count(NP)
    # print(Entrycount, Exitcount)
    A = len(Entry_NP_values)-len(Exit_NP_values)
    #print("Filled Parking slots = ", A)
    if Entrycount == Exitcount:
        data_values = [NP, date, timeStamp]
        with open("ParkingData\EntryData\EntryData_" + date + ".csv", 'a+') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data_values)
            print("Entry taken for CAR Number : " + NP)
            print("filled Parking slots present = ", A + 1)
            print("remaining slots : ", Available - A - 1)
            csvfile.close()
    elif Entrycount > Exitcount:
        data_values = [NP, date, timeStamp]
        with open("ParkingData\ExitData\ExitData_" + date + ".csv", 'a+') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data_values)
            print("Exit taken for CAR Number : " + NP)
            print("filled Parking slots present = ", A - 1)
            print("remaining slots : ", Available - A + 1)
            csvfile.close()
    else:
        pass





#img = cv2.imread("image3.jpg")
img = cv2.imread("image1.jpeg")
image = NoPDetection.NPDetection(img)

txt = NoPDetection.textReader(image)
# txt = ''
#print(txt)
DataEntry(txt)
# cv2.imshow("number plate", image)
# cv2.waitKey(0)