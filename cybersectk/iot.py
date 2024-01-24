import os
import glob
import numpy as np

#################### TCP IOT ##########################
'''
Define a dictionary of IP filters for different IoT devices
To be used a default argument for the iot function,
if no argument is passed by the user
'''
ip_filter = {}
    
ip_filter['TCP_Mobile'] = "'tcp && (ip.src==192.168.1.45)'"
ip_filter['TCP_Outlet'] = "'tcp && (ip.src==192.168.1.222) || \
                                        (ip.src==192.168.1.67)'"
ip_filter['TCP_Assistant'] = "'tcp && (ip.src==192.168.1.111) || \
                    (ip.src==192.168.1.30) || (ip.src==192.168.1.42) \
                 || (ip.src==192.168.1.59) || (ip.src==192.168.1.70)'"
ip_filter['TCP_Camera'] = "'tcp && (ip.src==192.168.1.128) || \
                    (ip.src==192.168.1.145) || (ip.src==192.168.1.78)'"
ip_filter['TCP_Miscellaneous'] = "'tcp && (ip.src==192.168.1.216) \
                  || (ip.src==192.168.1.46) || (ip.src==192.168.1.84) \
                     || (ip.src==192.168.1.91)'"

labelFeature = ["IPLength", "IPHeaderLength", "TTL", "Protocol", "SourcePort", 
                "DestPort", "SequenceNumber", "AckNumber", "WindowSize", 
                "TCPHeaderLength", "TCPLength", "TCPStream", "TCPUrgentPointer", 
                "IPFlags", "IPID", "IPchecksum", "TCPflags", "TCPChecksum"]


def iot(pcap_file, **ip_filter):
    all_features = []
    for k in ip_filter.keys():
        os.system("tshark -r " + pcap_file + " -w- -Y " +
                  ip_filter[k] + ">> filtered_pcap/" + k + ".pcap")

    for filteredFile in glob.glob('filtered_pcap/*.pcap'):
        filename = filteredFile.split('/')[-1]
        label = filename.replace('.pcap', '')
        tsharkCommand = "tshark -r " + filteredFile + " -T fields \
                        -e ip.len -e ip.hdr_len -e ip.ttl \
                        -e ip.proto -e tcp.srcport -e tcp.dstport -e tcp.seq \
                        -e tcp.ack -e tcp.window_size_value -e tcp.hdr_len -e tcp.len \
                        -e tcp.stream -e tcp.urgent_pointer \
                        -e ip.flags -e ip.id -e ip.checksum -e tcp.flags -e tcp.checksum"

        feature_str = str(os.popen(tsharkCommand).read())
        feature_str = feature_str.replace('\t', ',')
        feature_list = feature_str.splitlines()
        for features in feature_list:
            feature_array = np.array(features.split(','))
            feature_array = np.append(feature_array, label)
            all_features.append(feature_array)

    return np.array(all_features)


if __name__ == "__main__":
    pcap_file = input("Enter the Pcap file:")
    features = iot(pcap_file, **ip_filter)
    for feature_dict in features:
        print(feature_dict)