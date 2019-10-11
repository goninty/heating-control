import RPi.GPIO as GPIO
import time

def turn_servo(desired):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)

    p = GPIO.PWM(7, 50)
    p.start(7.5)

    if desired == "on":
        p.ChangeDutyCycle(12.5) #turn on heating
        time.sleep(0.04)
        
    elif desired == "off":
        p.ChangeDutyCycle(7.5) #turn off heating
        time.sleep(1)
        
    p.stop()
    GPIO.cleanup()