import time,picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture_continuous('img{counter:03d}.jpeg'):
        print('Captured %s' % filename)
        time.sleep(5) #Wait 5 seconds
