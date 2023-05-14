import socket 
import time
import random
import RPi.GPIO as GPIO  

pin = 1
#  aws server  
#host = '54.211.89.15'
# GPIO.setup(pin, GPIO.IN) 

# my ip
# this host is kevins homes
host = '98.222.114.146'
# host = '10.0.0.65'

button_pin = 18
GPIO.setmode(GPIO.BOARD)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


port = 8888
BUFFER_SIZE = 2000 
MESSAGE = str(1)
MESSAGEOFF = str(11)

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

prev_sent = False
state = True
count = 0


def send_msg(msg):
    i=0
    while i < 40:
        i = i +1
        try:
            tcpClientA.send(str(msg))
            break
        except Exception as e:
            time.sleep(random.uniform(0.1, 0.4))
                # print("ERROR : "+str(e))
            pass
        continue

# GPIO.add_event_detect(button_pin, GPIO.BOTH, callback=send_msg, bouncetime=300) 
GPIO.add_event_detect(button_pin, GPIO.RISING)
GPIO.add_event_callback(button_pin, send_msg)

    # count = count +1
last = 'off'
while MESSAGE != 'exit':
    try:
        if GPIO.input(button_pin):
        # if (input('input: ')):
     #       tcpClientA.connect((host, port))
            print('Input was HIGH')
            if (last == 'off'):
                send_msg(MESSAGEOFF)
                print("sent off")
                last ='on'
                time.sleep(1)
            else:
                send_msg(MESSAGE)
                print("sent on")
                last ='off'
                time.sleep(1)
        else:
            print("input = 0")
            time.sleep(1)
        # time.sleep(1)
        # data = tcpClientA.recv(BUFFER_SIZE)
        # state = GPIO.input(pin)
        # if ((state is True) and (prev_sent == False)):
        #         send_msg(MESSAGE)
        #         prev_sent = True
        #         print('sent msg')
        #         time.sleep(1)
        # else:
        #     send_msg(MESSAGEOFF)
        #     print("off message")
        #     time.sleep(1)
        #     pass
    except Exception as e:
            print("ERROR : "+str(e))


tcpClientA.close() 





