#!/usr/bin/python

from pyarlo import PyArlo
from influxdb import InfluxDBClient

def main():
	# INFLUXDB CONNECTION INFO
	host = "192.168.1.67"
	port = 8086
	user = "user"
	password = "password" 
	dbname = "readings"
	
	# CREATE CLIENT OBJECT
	client = InfluxDBClient(host, port, user, password, dbname)
	
	# ARLO CONNECTION INFO
	arlo  = PyArlo('user@fake.com', 'password')
	
	collectData(client,arlo)

def collectData(client,arlo):
	cams = arlo.cameras

	# COLLECT & UPLOAD DATA
	for cam in cams:
		model_id = cam.model_id
		serial_number = cam.serial_number
		battery_level = cam.battery_level
		signal_strength = cam.signal_strength
		measurement = "jupitor-" + model_id + "-" + serial_number
		
		data = [
		{
		  "measurement": measurement,
			  "fields": {
				  "battery_level" : battery_level ,
				  "signal_strength" : signal_strength
			  }
		  } 
		]
	
		client.write_points(data)

if __name__ == "__main__":
	main()
