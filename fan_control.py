def fan_control():
    import subprocess
    import time
    import RPi.GPIO as GPIO
    import json
    import curses

    def update_line(stdscr, text):
        stdscr.addstr(0, 0, text)
        stdscr.refresh()

    stdscr = curses.initscr()
    curses.noecho()  # Disable echoing of input characters
    curses.cbreak()
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
        on_temp = data['fanControl']['onTemp'] # default 65
        off_temp = data['fanControl']['offTemp'] # default 55
        gpio = data['fanControl']['gpio'] # default 17
        enable = data['fanControl']['enable']
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # enabling the motor/enable pins
    GPIO.setup(gpio, GPIO.OUT)
    GPIO.setup(enable, GPIO.OUT)

    # Create a PWM object for the enable pin
    pwm = GPIO.PWM(enable, 100)
    pwm.start(100)
    fan_on = False
    try: 
        while True:
            temp = subprocess.check_output("vcgencmd measure_temp", shell=True).decode('utf-8')
            temp_value = float(temp[5:9])
            
            if temp_value > on_temp:
                fan_on = True
            elif temp_value < off_temp:
                fan_on = False
            
            if fan_on:
                GPIO.output(gpio, GPIO.HIGH)
                update_line(stdscr, f"Fan on : {temp_value}")
            else:
                GPIO.output(gpio, GPIO.LOW)
                update_line(stdscr, f"Fan off: {temp_value}")

            time.sleep(1)
    except KeyboardInterrupt:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        print("Program stopped via keyboard interrupt")
    finally:
        # resetting echo
        curses.echo()
        curses.nocbreak()
        curses.endwin()
	
if __name__ == "__main__":
    fan_control()
