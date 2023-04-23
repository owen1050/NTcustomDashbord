from networktables import NetworkTables
import time

NetworkTables.initialize(server="localhost")
sd = NetworkTables.getTable("SmartDashboard")

sd.putNumber("TestNumber", -1)
time.sleep(1)




#https://github.com/robotpy/pynetworktables/blob/main/samples/global_listener.py