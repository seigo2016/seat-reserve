#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import signal
import sys
import random


def handler(signum, frame):
    print('Signal handler called with signal ' + signum)
    GPIO.cleanup()
    sys.exit(0)


seat_number = list(range(1, 31))

GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN)
before = 0

while True:
    now = GPIO.input(9)
    if before == 0 and now == 1:
        number = random.choice(seat_number)
        if number <= 6:
            print("軍艦島座席番号 : " + str(number))
        elif 7 <= number <= 12:
            print("屋久島座席番号 : " + str(number))
        elif 13 <= number <= 18:
            print("小豆島座席番号 : " + str(number))
        elif 19 <= number <= 24:
            print("佐渡島座席番号 : " + str(number))
        elif 25 <= number <= 30:
            print("種子島座席番号 : " + str(number))
        time.sleep(0.1)
        seat_number.remove(number)
        if not seat_number:
            print("座席は全て埋まりました。空いているお席にどうぞ。")
            sys.exit()
    time.sleep(0.1)
    before = now
