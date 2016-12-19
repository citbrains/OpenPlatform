import serial
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, True)
time.sleep(0.05)
ser = serial.Serial('/dev/ttyAMA0', 115200)
angle=16000
#angle=32000
ID=19
newID=ID
print ID

TxData = [0x01] #TxData[0]
TxData.append(0x00)
TxData.append(0x00)
TxData.append(0x00)
TxData.append(0x00)#TxData[4]
TxData.append(0x00)
TxData.append(0x00)
TxData.append(0x00)
TxData.append(0x00)
TxData.append(0x00)#TxData[9]
TxData.append(0x00)
TxData.append(0x00)
TxData.append(0x00)
TxData.append(0x00)
TxData.append(0x00)#TxData[14]

check_sum = 0
TxData[0] = 0x08         #All byte
TxData[1] = 0x04     #Command
TxData[2] = 0x00     #Option/Status
TxData[3] = ID     #ID
TxData[4] = 0x02     #mode
TxData[5] = 0x28     #address
TxData[6] = 0x01     #device number
#check sum cal
for i in range(7):
        check_sum += TxData[i]
check_sum = 0x00FF & check_sum
TxData[7] = check_sum
print TxData
for i in range(8):
    ser.write(chr(TxData[i]))
time.sleep(0.005)

#change ID
#TxData[0] = 0x08        #All byte
#TxData[1] = 0x04        #Command
#TxData[2] = 0x00        #Option/Status
#TxData[3] = ID        #ID
#TxData[4] = newID       #data
#TxData[5] = 0x00        #address
#TxData[6] = 0x01        #device number
#check sum cal
#check_sum=0
#for i in range(7):
#        check_sum += TxData[i]
#check_sum = 0x00FF & check_sum
#TxData[7] = check_sum
#for i in range(8):
#        ser.write(chr(TxData[i]))
#print TxData
#time.sleep(0.005)
#ID=newID

#change boadrate
#TxData[0] = 11        #All byte
#TxData[1] = 0x04        #Command
#TxData[2] = 0x00        #Option/Status
#TxData[3] = ID        #ID
#TxData[4] = 0x00       #data1
#TxData[5] = 0xC2       #data2
#TxData[6] = 0x01       #data3
#TxData[7] = 0x00       #data4
#TxData[8] = 0x01        #address
#TxData[9] = 0x01        #device number
#check_sum=0
#for i in range(10):
#        check_sum += TxData[i]
#check_sum = 0x00FF & check_sum
#TxData[10] = check_sum
#for i in range(11):
#        ser.write(chr(TxData[i]))
#print TxData
#time.sleep(0.005)
#ser.close()
#ser = serial.Serial('/dev/ttyAMA0', 115200)

TxData[0] = 0x08        #All byte
TxData[1] = 0x04        #Command
TxData[2] = 0x00        #Option/Status
TxData[3] = ID        #ID
TxData[4] = 0x01        #mode
TxData[5] = 0x29        #address
TxData[6] = 0x01        #device number
#check sum cal
check_sum=0
for i in range(7):
        check_sum += TxData[i]
check_sum = 0x00FF & check_sum
TxData[7] = check_sum

for i in range(8):
        ser.write(chr(TxData[i]))
print TxData
time.sleep(0.005)

TxData[0] = 0x08        #All byte
TxData[1] = 0x04        #Command
TxData[2] = 0x00        #Option/Status
TxData[3] = ID        #ID
TxData[4] = 0x00        #mode
TxData[5] = 0x5C        #address
TxData[6] = 0x01        #device number
#check sum cal
for i in range(7):
        check_sum += TxData[i]
check_sum = 0x00FF & check_sum
TxData[7] = check_sum
for i in range(8):
        ser.write(chr(TxData[i]))
print TxData
time.sleep(0.005)

TxData[0] = 0x08        #All byte
TxData[1] = 0x04        #Command
TxData[2] = 0x00        #Option/Status
TxData[3] = ID        #ID
TxData[4] = 0x00        #mode
TxData[5] = 0x28        #address
TxData[6] = 0x01        #device number
#check sum cal
check_sum=0
for i in range(7):
        check_sum += TxData[i]
check_sum = 0x00FF & check_sum

TxData[7] = check_sum

for i in range(8):
        ser.write(chr(TxData[i]))
print TxData
time.sleep(0.005)


#angle = 1600
deg = 1
TxData[0] = 0x09                #All byte
TxData[1] = 0x06        #Command
TxData[2] = 0x00        #Option/Status
TxData[3] = ID        #ID
TxData[4] = 0x00FF & angle              #mode
TxData[5] = 0x00FF & (angle >> 8)       #address
TxData[6] = 0x00FF & deg        #device number
TxData[7] = 0x00FF & (deg >> 8) #check sum cal

#check sum
check_sum=0
for i in range(8):
        check_sum += TxData[i]

check_sum = 0x00FF & check_sum

TxData[8] = check_sum

for i in range(9):
        ser.write(chr(TxData[i]))
print TxData
time.sleep(0.005)
GPIO.output(18, False)
#str = ser.read()
#print str

ser.close()