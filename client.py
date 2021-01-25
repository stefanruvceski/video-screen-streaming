import os

# msg = os.popen('pip install vidstream')
# msg = os.popen('pip install pillow')

from vidstream import CameraClient
from vidstream import VideoClient
from vidstream import ScreenShareClient

# Choose One
client1 = CameraClient('192.168.1.175', 11000)
client2 = VideoClient('192.168.1.175', 11000, 'video.mp4')
client3 = ScreenShareClient('192.168.1.175', 11000  )

client1.start_stream()
client2.start_stream()
client3.start_stream()