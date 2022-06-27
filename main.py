import paho.mqtt.client as mqtt
import time
import json
import threading
from random import randrange

def on_log(client, userdata, flags, buf):
    print("log:" + buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

mqtt.Client.connected_flag=False#create flag in class
broker="77.237.53.201"
client = mqtt.Client("python1")
client.on_connect=on_connect
client.on_log = on_log
client.loop_start()
client.username_pw_set("marbanriedl", "WFP1")
print("Connecting to broker ",broker)
def run(name):
    name = "Sensor " + name
    try:
        client.connect(broker, 13883)
    except:
        print("connection failed")
        exit(1)
    while not client.connected_flag:
        i = 1
        while i < 15:
            print("In wait loop")
            temp = randrange(-15, 45)
            luftdruck = randrange(100);
            luftfeuchtigkeit = randrange(100);
            kohlendioxid = randrange(100);
            zustand = "OK";

            if(temp > 30 and luftfeuchtigkeit < 50):
                zustand = "NICHT OK";
            else:
                zustand = "OK";

            #neu
            client_msg = json.dumps({"name": name, "temp": temp, "luftdruck": luftdruck, "luftfeuchtigkeit": luftfeuchtigkeit, "kohlendioxid": kohlendioxid, "zustand": zustand});
            a="sensor-data"
            client.publish(a, client_msg)

            time.sleep(20)
            i = i + 1
    print("in Main Loop")
    client.loop_stop()
    client.disconnect()
arr = ["1", "2", "3", "4", "5", "6"];
thread1 = threading.Thread(target=run, args=(arr[0]))
thread2 = threading.Thread(target=run, args=(arr[1]))
thread3 = threading.Thread(target=run, args=(arr[2]))
thread4 = threading.Thread(target=run, args=(arr[3]))
thread5 = threading.Thread(target=run, args=(arr[4]))
thread6 = threading.Thread(target=run, args=(arr[5]))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()