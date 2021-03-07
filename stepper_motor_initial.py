#!/usr/bin/env python3

import time
import board
import digitalio

enable_pin = digitalio.DigitalInOut(board.D18)
A1pin = digitalio.DigitalInOut(board.D4)
A2pin = digitalio.DigitalInOut(board.D17)
B1pin = digitalio.DigitalInOut(board.D23)
B2pin = digitalio.DigitalInOut(board.D24)

enable_pin.direction = digitalio.Direction.OUTPUT
A1pin.direction = digitalio.Direction.OUTPUT
A2pin.direction = digitalio.Direction.OUTPUT
B1pin.direction = digitalio.Direction.OUTPUT
B2pin.direction = digitalio.Direction.OUTPUT

enable_pin.value = True


def forward(delay, steps):
    i = 0
    while i in range(0, steps):
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        i += 1


def backwards(delay, steps):
    i = 0
    while i in range(0, steps):
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        i += 1


def setStep(w1, w2, w3, w4):
    A1pin.value = w1
    A2pin.value = w2
    B1pin.value = w3
    B2pin.value = w4


while True:
    user_delay = input("Delay between steps (milliseconds)?")
    user_steps = input("How many steps forward? ")
    forward(int(user_delay) / 1000.0, int(user_steps))
    user_steps = input("How many steps backwards? ")
    backwards(int(user_delay) / 1000.0, int(user_steps))
