#!/usr/bin/python
import paho.mqtt.client as mqtt
import os
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/home/lr/feh")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    print(str(msg.payload))

    if str(msg.payload) == "button_D5_GPIO14":
        print(msg.topic + " " + str(msg.payload))
        os.system("slideshow &")
        time.sleep(3)

    if str(msg.payload) == "button_D6_GPIO12":
        print(msg.topic + " " + str(msg.payload))
        os.system("export DISPLAY=:0.0 && xdotool key Left &")

    if str(msg.payload) == "button_D2_GPIO02":
        print(msg.topic + " " + str(msg.payload))
        os.system("export DISPLAY=:0.0 && xdotool key Right &")

    if str(msg.payload) == "button_D3_GPIO00":
        print(msg.topic + " " + str(msg.payload))
	os.system("slideshow &")
	time.sleep(3)

    if str(msg.payload) == "power":
        print(msg.topic + " " + str(msg.payload))
        os.system("slideshow &")
        time.sleep(3)

    if str(msg.payload) == "meteo":
        os.system("meteo &")
        time.sleep(3)

    if str(msg.payload) == "left":
        print(msg.topic + " " + str(msg.payload))
        os.system("export DISPLAY=:0.0 && xdotool key Left &")

    if str(msg.payload) == "right":
        print(msg.topic + " " + str(msg.payload))
        os.system("export DISPLAY=:0.0 && xdotool key Right &")

    if str(msg.payload) == "up":
        print(msg.topic + " " + str(msg.payload))
        os.system("export DISPLAY=:0.0 && xdotool key 0 &")

    if str(msg.payload) == "down":
        print(msg.topic + " " + str(msg.payload))
        os.system("ff_kill &")
 
    if str(msg.payload) == "startstop":
        print(msg.topic + " " + str(msg.payload))
        os.system("export DISPLAY=:0.0 && xdotool key 1 &")

    if str(msg.payload) == "LGmode":
        print(msg.topic + " " + str(msg.payload))
        os.system("export DISPLAY=:0.0 && xdotool key e &")

    if str(msg.payload) == "LGturbo":
        print(msg.topic + " " + str(msg.payload))
        os.system("export DISPLAY=:0.0 && osdtest.sh &")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
