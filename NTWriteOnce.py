from networktables import NetworkTables
import time

NetworkTables.initialize(server="localhost")
sd = NetworkTables.getTable("SmartDashboard")
i = 0
while True:
	i = i + 1
	sd.putNumber("TestNumber", i)
	time.sleep(0.1)





#https://github.com/robotpy/pynetworktables/blob/main/samples/global_listener.py