import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "../common"))

from communication.client import Client


client = Client("192.168.1.123", "6969")
client.connect_to_server()

