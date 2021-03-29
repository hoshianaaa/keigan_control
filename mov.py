# -*- coding: utf-8 -*-
from pykeigan import blecontroller
from pykeigan import utils
from concurrent.futures import ThreadPoolExecutor
import time 
import sys

def get_motor_informations():
    global pos
    global init_pos
    while True:
        if dev:

            m = dev.read_motor_measurement()
            p = m.pop("position")
            t = m.pop("torque")

        pos = utils.rad2deg(p)
        time.sleep(0.1)

def rad2deg(rad):
    return utils.rad2deg(rad)

def deg2rad(deg):
    return utils.deg2rad(deg)

def init_pos():
    dev.move_to_pos(0)
    time.sleep(7)
    dev.stop_motor()

def mov( deg, error=1):

    target_pos = deg
    dev.move_to_pos(deg2rad(deg))

    while(1):
        if abs(target_pos - pos) < error:
            dev.stop_motor()
            break

sn = "e7:e6:c6:91:82:75"

pos = 0
dev = blecontroller.BLEController(sn)
executor = ThreadPoolExecutor(max_workers=2)
res = executor.submit(get_motor_informations)
dev.enable_action()
dev.set_speed(0.5)
dev.set_acc(0.5)
dev.set_max_torque(0.1)
dev.set_led(1, 0, 200, 0)

deg_list = [-90,-60,-30,0,30,60,90]

print("mov 0 deg")
mov(0)

for i in deg_list:
    print("mov",i,"deg")
    mov(i)
