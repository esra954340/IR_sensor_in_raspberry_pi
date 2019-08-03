import RPi.GPIO as IO
#import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(2,IO.OUT) #GPIO 2 -> Red LED as output
IO.setup(3,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(22,IO.OUT) #GPIO 14 -> Buzzer as output
IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input

while True:

    if(IO.input(14)==True): #object is far away
        IO.output(2,True) #Red led ON
        IO.output(3,False) # Green led OFF
        IO.output(22,False) # Buzzer OFF
        print("No object")
    
    if(IO.input(14)==False): #object is near
        IO.output(3,True) #Green led ON
        IO.output(22,True) #Buzzer ON
        IO.output(2,False) # Red led OFF
        print("move the object")
        
