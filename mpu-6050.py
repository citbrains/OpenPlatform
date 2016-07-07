# -*- coding: utf-8 -*-
#!/usr/bin/python

# import module
import smbus		# use I2C
import math		# mathmatics
from time import sleep	# time module

#
# define
#
# slave address
DEV_ADDR = 0x68		# device address
# register address
ACCEL_XOUT = 0x3b	#
ACCEL_YOUT = 0x3d
ACCEL_ZOUT = 0x3f
TEMP_OUT = 0x41
GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47
PWR_MGMT_1 = 0x6b	# PWR_MGMT_1
PWR_MGMT_2 = 0x6c	# PWR_MGMT_2

bus = smbus.SMBus(1)
bus.write_byte_data(DEV_ADDR, PWR_MGMT_1, 0)

#
# Sub function
#
# 1byte read
def read_byte(adr):
    return bus.read_byte_data(DEV_ADDR, adr)
# 2byte read
def read_word(adr):
    high = bus.read_byte_data(DEV_ADDR, adr)
    low = bus.read_byte_data(DEV_ADDR, adr+1)
    val = (high << 8) + low
    return val
# Sensor data read
def read_word_sensor(adr):
    val = read_word(adr)
    if (val >= 0x8000):
    # minus
        return -((65535 - val) + 1)
    else:
    # plus
        return val

#
# 角速度
#
# get gyro data
def get_gyro_data_lsb():
    x = read_word_sensor(GYRO_XOUT)
    y = read_word_sensor(GYRO_YOUT)
    z = read_word_sensor(GYRO_ZOUT)
    # 角速度表示
    print 'gyro_x(raw): %d' % x,
    print 'gyro_y(raw): %d' % y,
    print 'gyro_z(raw): %d' % z,
    return [x, y, z]

#
# 加速度
#
# get accel data
def get_accel_data_lsb():
    x = read_word_sensor(ACCEL_XOUT)
    y = read_word_sensor(ACCEL_YOUT)
    z = read_word_sensor(ACCEL_ZOUT)
    # 加速度表示
    print 'accel_x(raw): %d' % x,
    print 'accel_y(raw): %d' % y,
    print 'accel_z(raw): %d' % z,
    return [x, y, z]

#
# Main function
#
while 1:
    # 角速度
    gyro_x,gyro_y,gyro_z = get_gyro_data_lsb()
    # 加速度
    accel_x,accel_y,accel_z = get_accel_data_lsb()

    print

    sleep(0.5)
