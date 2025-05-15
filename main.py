import time
import RPi.GPIO as GPIO

# GPIO setup
def setup_gpio():
	GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
	GPIO.setwarnings(False)

# Cleanup GPIO
def cleanup_gpio():
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup_gpio()
		print("GPIO setup complete. Running main loop...")
	except KeyboardInterrupt:
		print("Exiting program.")
	finally:
		cleanup_gpio()
		print("GPIO cleaned up.")