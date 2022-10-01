import pyshark
try:
    capture = pyshark.LiveCapture(interface="WLAN", output_file="pyshark.pcap")
    capture.sniff()
except KeyboardInterrupt:
    print(capture)