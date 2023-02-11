#Required libraries.
import time,board,busio
import numpy as np
import adafruit_mlx90640

#vars
#Define i2c port availability and baud rate.
i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000)
#Define the camera.
mlx = adafruit_mlx90640.MLX90640(i2c)
#Define refresh rate.
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ
#Define frame H*W
frame = np.zeros((24*32,))
while True:
    try:
        mlx.getFrame(frame)
        break
    except ValueError:
        continue


print('Average MLX90640 Temperature: {0:2.1f}C ({1:2.1f}F)'.\
      format(np.mean(frame),(((9.0/5.0)*np.mean(frame))+32.0)))  