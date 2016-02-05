# Maintenance of climat conditions at home made grove box. 

import time
import pigpio 
import RPI.GPIO as GPIO
import DHT22
from time import sleep

PHOTO_SENSOR_PIN = 22	    # Pghotoresistor 
HUMIDITY_TEMP_PIN = 27	    # DHT22 humidity-temerature sensor
MOTOR_PIN_OPEN = 12         # jaloise operation motor`s GPIO pin
MOTOR_PIN_CLOSE = 16        # jaloise operation motor`s GPIO pinFAN_PIN = 16                
IRL_PIN = 16                # pin to turn on infrared lamp
WATER_PUMP_PIN = 16         # pin to send signal to a water pump

PHOTO_MAX = 50000           # max allowable level of illumination
PHOTO_MIN = 40000     
TEMP_MAX = 25               #allowable level of temperature
TEMP_MIN = 22
HUMIDITY_MAX = 80           #allowable level of humidity
HUMIDITY_MIN = 70
        
GPIO.setmode(GPIO.BOARD)

#---------------------Class Photo Sensor------------------------
class PhotoSensor:
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

#--------------------Class Temperature and Humidity sensor------
class HumidityTemperatureSensor:
    pi = gpio.pi()
    DHT22 = DHT22.sensor(pi, HUMIDITY_TEMP_PIN)
    DHT22.triger()

    def getHumidity:
        HT22.triger()
        humidity = '%.2f' % (DHT22.hymidity())
        return humidity 
    
    def readDHT22():
        DHT22.triger()
        temperature = '%.2f' % (DHT22.temperature())
        return temperature

#-------------------Class Motor--------------------------------
class Motor
    # Run the motor
    def startMotor(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, HIGH)

    # Stop the motor	
    def stopMotor(pin):
    	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, LOW)

#-------------------Class Water Pomp----------------------------
class WaterPomp:
    def startMotor(pin):
        GPIO.output(pin, True)
        
    def stopMotor(pin):
        GPIO.output(pin, False)

#-----------------Class Infrared Lamp---------------------------
class InfraredLamp:
    def turnOn(pin):
        GPIO.output(pin, True)
        
    def turnOff(pin):
        GPIO.output(pin, False)

#------------------Class Control System---------------------------
class ControlSystem:
    photoSensor = PhotoSensor()
    humidityTempSensor = HumidityTemperatureSensot()
    jaloiseMotor = Motor()
    waterPompMotor = WaterPomp()
    fanMotor = Motor()
    infraredLamp = InfraredLamp()

    def startInsolationControl:
        while True:
		photoData = photoSensor.getPhotoSensorData()
		if photoData > PHOTO_MAX:
                    jaloiseMotor.startMotor(MOTOR_PIN_CLOSE)
		    while (photoData > PHOTO_MAX):
			photoData = photoSensor.getPhotoSensorData()	
		    jaloiseMotor.stopMotor(MOTOR_PIN_CLOSE)
		else if photoData < PHOTO_MIN:
                    jaloiseMotor.startMotor(MOTOR_PIN_OPEN)
		    while (photoData < PHOTO_MIN):
			photoData = photoSensor.getPhotoSensorData()
		    jaloiseMotor.stopMotor(MOTOR_PIN_OPEN)

    def startTemperatureControl:
        while True:
            temperature = humidityTempSensor.getTemperature()
            if temperature < TEMP_MIN:
                infraredLamp.turnOn(IRL_PIN)
                while (temperature < TEMP_MIN):
                    temperature = humidityTempSensor.getTemperature()
                infraredLamp.turnOff(IRL_PIN)
            else if temperature > TEMP_MAX:
                fanMotor.startMotor()
                while (temperature > TEMP_MAX):
                    temperature = humidityTempSensor.getTemperature()
                fanMotor.stopMotor()
                

    def startHumidityControl:
        while True:
            humidity = humidityTempSensor.getHumidity()
            if humidity < HUMIDITY_MIN:
                waterPumpMotor.startMotor(WATER_PUMP_PIN)
                while (humidity < HUMIDITY_MIN):
                    humidity = humidityTempSensor.getHumidity()
                waterPumpMotor.stopMotor(WATER_PUMP_MOTOR)
            else if humidity > HUMIDITY_MAX:
                fanMotor.startMotor(FAN_PIN)
                while (humidity > HUMIDITY_MAX):
                    humidity = humidityTempSensor.getHumidity()
                fanMotor.stopMotor(FAN_PIN)
                    
                    	
def main():
    controlSystem = ControlSystem()
    controlSystem.srartInsolationControl()
    controlSystem.startTemperatureControl()
    controlSystem.startHumidityControl()
	

if __name__ == '__main__': 
    main()


