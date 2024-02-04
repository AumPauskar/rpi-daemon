def fan_on():
    import time
    import RPi.GPIO as GPIO

    gpio = 17
    enable = 27
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # enabling the motor/enable pins
    GPIO.setup(gpio, GPIO.OUT)
    GPIO.setup(enable, GPIO.OUT)

    # Create a PWM object for the enable pin
    pwm = GPIO.PWM(enable, 100)
    pwm.start(100)
    fan_on = False
    counter = 60
    try: 
        while counter:
            GPIO.output(gpio, GPIO.HIGH)
            print(f"Fan on")
            counter -= 1
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program stopped via keyboard interrupt")
        GPIO.output(gpio, GPIO.LOW)
    finally:
        # resetting echo
        GPIO.output(gpio, GPIO.LOW)
	
if __name__ == "__main__":
    fan_on()
