import pyshark
import dpkt
import socket

capture = pyshark.FileCapture("pyshark.pcap",  display_filter='ip.addr == 113.200.102.203')
#print(capture[0])
#f = open('pyshark.pcap', 'rb')
#pcap = dpkt.pcap.Reader(f)

def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            # KML = retKML(dst, src)
            # kmlPts = kmlPts + KML
            print
            'Source: ' + src + ' Destination: ' + dst
        except:
            pass
    return kmlPts

#plotIPs(pcap)


for i in capture:
    print(i.ip.src)
    print(i.ip.ttl)
    pre = i
    print(i.ip.version)
    print(i.ip.proto)
    print(i.highest_layer)
    print(i.sniff_time)
    print(i.sniff_timestamp)



