import time,picamera

with picamera.PiCamera() as camera:
    camera.resolution = (
    camera.start_preview()
    
    time.sleep(2)
    camera.capture( name +'.jpeg')
    time.sleep(0.5)
    camera.stop_preview()
    
