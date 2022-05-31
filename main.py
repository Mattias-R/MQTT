
import paho.mqtt.client as mqtt  #import the client1
import time

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
client = mqtt.Client("python1")             #create new instance
client.on_connect=on_connect  #bind call back function
client.on_log = on_log
client.loop_start()
client.username_pw_set("marbanriedl", "WFP1")
print("Connecting to broker ",broker)
try:
    client.connect(broker, 13883)      #connect to broker
    #client.connect(broker, 13080)  # connect to broker
    #client.connect(broker, 1883)  # connect to broker
    #client.connect(broker, 80)  # connect to broker
    #client.connect(broker)  # connect to broker
    #client.connect(broker, 22013)
except:
    print("connection failed")
    exit(1)
while not client.connected_flag: #wait in loop
    print("In wait loop")
    client.publish("luftfeuchtigkeit", 20)
    client.publish("temperatur", 59)
    client.publish("luftdruck", 400)
    client.publish("kohlendioxid", 35)
    client.publish("kohlenmonoxid", 70)
    time.sleep(1)
print("in Main Loop")
#client.connect(broker2, 1883)
client.loop_stop()    #Stop loop
client.disconnect() # disconnect
"""
import paramiko
host = "77.237.53.201"
port = 22013
username = "marbanriedl"
password = "WFP1"

command2 = "sudo docker exec -it 03fb0d0068c8 /bin/sh "
command = "mosquitto_pub -h localhost -t luftdruck -m '85'"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command2)
#stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)
"""
