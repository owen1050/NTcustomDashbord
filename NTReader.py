from networktables import NetworkTables
import time

NetworkTables.initialize(server="localhost")
sd = NetworkTables.getTable("SmartDashboard")

def valueChanged(key, value, isNew):
    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))


NetworkTables.addEntryListener(valueChanged)
sd.putNumber("TestNumber", 1)

while True:
    time.sleep(1)



#https://github.com/robotpy/pynetworktables/blob/main/samples/global_listener.py