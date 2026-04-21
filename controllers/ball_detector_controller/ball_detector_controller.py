from controller import Robot
import cv2
import numpy as np

robot = Robot()
timestep = int(robot.getBasicTimeStep())
camera = robot.getDevice("camera")
camera.enable(timestep)

print("Camera test - ball at robot position")

while robot.step(timestep) != -1:
    image = camera.getImage()
    if image:
        width = camera.getWidth()
        height = camera.getHeight()
        img_array = np.frombuffer(image, dtype=np.uint8).reshape(height, width, 4)
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_BGRA2BGR)
        
        center = img_bgr[height//2, width//2]
        print(f"R={center[2]} G={center[1]} B={center[0]}")
        
        if center[2] > 200:
            print("RED SEEN!")