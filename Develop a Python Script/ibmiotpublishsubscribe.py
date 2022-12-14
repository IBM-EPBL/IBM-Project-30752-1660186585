import ibmiotf.application
import ibmiotf.device
import time
import random




#provide your ibm Watson Device Credentials



organization="ko3qfr"
deviceType="temp"
deviceid="4321"
authMethod="use-token-auth"
authToken="123456789"


#generate random values for random variables (temperature & humidity)
Temp=random.randint(0,100)
Humd=random.randint(0,100)
oxygen=30
lat=17
lon=18



def myCommandCallback(cmd):
    print("command received: %s"&cmd.data['command'])
    print(cmd)
    try:
        deviceOptions={'org':organization,'type':deviceType,'id':deviceid,'authentication method':authMethod,'authentication token':authToken}

        deviceCli=ibmiotf.device.Client(deviceOptions)
    except Exception as e:
        print("caught exception connecting device %s" %str(e))
        sys.exit()


#connect and send a data point "temp" value with integer value into the cloud as a type event for 10 seconds
deviceCli.connect()
while True:
    data={"d":{'temp':Temp,'humid':Humd,'oxygen':oxygen,"lat":lat,"lon":lon}}
    print(data)
    def myOnPublishCallBack():
        print("published temperature: %s C" %Temp,"humidity:%s %%" %Humd)
    success=deviceCli.publishEvent("IoTSensor","json",data,qos=0,on_publish=myOnPublishCallBack)
    if not success:
        print("not connected")
    time.sleep(1)
    deviceCli.commandCallback=myCommandCallback


#disconnect the device
deviceCli.disconnect()

    
