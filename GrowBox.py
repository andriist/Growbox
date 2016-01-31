# Maintenance of insolation level at home made grove box. 

import time
import RPI.GPIO as GPIO

PHOTO_SENSOR_PIN = 22 
MOTOR_PIN_OPEN = 12 # jaloise operation motor`s GPIO pin
MOTOR_PIN_CLOSE = 16 # jaloise operation motor`s GPIO pin
PHOTO_MAX = 50000  # max allowable level of illumination
PHOTO_MIN = 40000  # min allowable level of illumination

GPIO.setmode(GPIO.BOARD)

# Get data from photo sensor
def getPhotoSensorData():
	data = 0;
	GPIO.setup(PHOTO_SENSOR_PIN, GPIO.OUT)
	GPIO.output(PHOTO_SENSOR_PIN, LOW)
	time.sleep(0.1)
	
	GPIO.setup(pin, GPIO.IN)
	while(GPIO.input(PHOTO_SENSOR_PIN) == GPIO.LOW):
		data += 1 # 
	return data
	
# Run the motor	
def startMotor(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, HIGH)

# Stop the motor	
def stopMotor(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, LOW)
			
while 1:
	photoData = getPhotoSensorData():
	if photoData > PHOTO_MAX:
		while (photoData > PHOTO_MAX):
			startMotor(MOTOR_PIN_CLOSE)
		stopMotor(MOTOR_PIN_CLOSE)
	else:
		while (photoData < PHOTO_MIN):
			startMotor(MOTOR_PIN_OPEN)
		stopMotor(MOTOR_PIN_OPEN)
