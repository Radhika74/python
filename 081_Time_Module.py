import time
print(time.time())

#use of stfrtine() method
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)

 # use of sleep() method 
print("Start",time.time())
time.sleep(2)
print("End",time.time())

