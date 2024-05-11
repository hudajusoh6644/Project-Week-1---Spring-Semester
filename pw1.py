# project week 1 - group 14
#this code only have the movement of the car
#always used as troubleshooting code to make sure the motors are working fine 

import RPi.GPIO as GPIO

import time

 

#pin numbers BASED ON THE board not GPIO!!

ENA_PIN = 22

ENB_PIN = 18

IN1 = 15

IN2 = 13

IN3 = 11

IN4 = 7

 

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

 

GPIO.setup(ENA_PIN, GPIO.OUT)

GPIO.setup(ENB_PIN, GPIO.OUT)

GPIO.setup(IN1, GPIO.OUT)

GPIO.setup(IN2, GPIO.OUT)

GPIO.setup(IN3, GPIO.OUT)

GPIO.setup(IN4, GPIO.OUT)

 

#  Function to move the robot forward

def forward():

    GPIO.output(IN1, GPIO.HIGH)

    GPIO.output(IN2, GPIO.LOW)

    GPIO.output(IN3, GPIO.HIGH)

    GPIO.output(IN4, GPIO.LOW)

 

# Function to move the robot backward

def backward():

    GPIO.output(IN1, GPIO.LOW)

    GPIO.output(IN2, GPIO.HIGH)

    GPIO.output(IN3, GPIO.LOW)

    GPIO.output(IN4, GPIO.HIGH)

 

# Function to turn the robot left

def left():

    GPIO.output(IN1, GPIO.LOW)

    GPIO.output(IN2, GPIO.HIGH)

    GPIO.output(IN3, GPIO.HIGH)

    GPIO.output(IN4, GPIO.LOW)

 

# Function to turn the robot right

def right():

    GPIO.output(IN1, GPIO.HIGH)

    GPIO.output(IN2, GPIO.LOW)

    GPIO.output(IN3, GPIO.LOW)

    GPIO.output(IN4, GPIO.HIGH)

 

# Stop the robot

def stop():

    GPIO.output(IN1, GPIO.LOW)

    GPIO.output(IN2, GPIO.LOW)

    GPIO.output(IN3, GPIO.LOW)

    GPIO.output(IN4, GPIO.LOW)

 

try:

    # Enable Motors

    GPIO.output(ENA_PIN, GPIO.HIGH)

    GPIO.output(ENB_PIN, GPIO.HIGH)

 

    # Move forward for 2 seconds

    forward()

    time.sleep(2)

 

    # Move backward for 2 seconds

    #backward()

    #time.sleep(2)

 

    # Turn left for 2 second

    #left()

    #time.sleep(2)

 

    # Turn right for 2 second

    #right()

    #time.sleep(2)

 

    # Stop the robot

    #stop()

 

finally:

    # Disable Motors and clean up GPIO settings

    GPIO.output(ENA_PIN, GPIO.LOW)

    GPIO.output(ENB_PIN, GPIO.LOW)

    GPIO.cleanup()
