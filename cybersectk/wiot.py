import scapy.all as scapy
import numpy as np

def wiot(pcap_file):
    frames = scapy.sniff(offline=pcap_file)
    data = []
    for frame in frames:
        if frame.haslayer(scapy.Dot11):
            for packets in frame:
                row = [frame.version, frame.pad, frame.len, frame.Rate, frame.ChannelFrequency, frame.ChannelFlags, 
                       frame.dBm_AntSignal, frame.Antenna, frame.subtype, frame.type, frame.proto, frame.FCfield, 
                       frame.ID, frame.addr1, frame.addr2, frame.addr3, frame.SC, frame.addr4]
                if packets.haslayer(scapy.Dot11Elt):
                    packets = scapy.Dot11Elt()
                    row.extend([frame.payload.ID, frame.payload.len, frame.info.decode()])
                data.append(row)
    return np.array(data)

if __name__ == "__main__":
    pcap_file = input("Enter the Pcap file:")
    data = wiot(pcap_file)
    print(data)