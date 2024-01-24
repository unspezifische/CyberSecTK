# cybersectk

This is a fork of [cybersectk](https://github.com/sumendrabsingh/CyberSecTK-Library) by SumendraBSingh, a Python library for Machine Learning CyberSec feature extraction.

## Installation Instructions

This library is available through PyPi and can be installed using the following command:

```sh
pip install cybersectk
```

This will install all the necessary dependencies before installing the package itself.

If you are interested in developing for this library yourself, clone the repo, then run the following commands:

```sh
cd CyberSecTK
python -m venv env
source env/bin/activate
pip install -e .
```

This will move you into the freshly cloned repo, create a virtual environment so any changes you make won't affect the rest of your Python installation, actiavte that virutal environment, then install the CyberSecTK package in "editable" mode.

## Modules
 
### WLAN IOT
The `wiot` module extracts features from wireless DataLink layer header information
 
```python
 from cybersectk.wiot import wiot
 wiot()
```

This module outputs a NumPy array, which can be passed directly to a TensorFlow or PyTorch training script. 
 
NOTE: Ensure the file is in the same directory as the script, and don't forget specify the `.pcap` extension at the end of the file name.

### TCP IOT
The `iot` module extracts features from TCP/IP packets.

```python
from cybersectk.iot import iot
iot('path_to_your_pcap_file.pcap', **ip_filter)
 ```
 
This module outputs a NumPy array, which can be passed directly to a TensorFlow or PyTorch training script. 

#### Iterating Through a Directory of PCAPs
We can use Python's built-in `os` library to iterate through a directory containing PCAP files and pass each file to the `iot()` function, using the `ip_filter` dictionary provided by CyberSecTK:
```py
import os
from cybersectk.iot import iot

# Specify the directory path where the PCAP files are located
pcap_directory = '/path/to/pcap/files'

# Iterate through each file in the directory
for filename in os.listdir(pcap_directory):
    if filename.endswith('.pcap'):
        # Construct the full file path
        file_path = os.path.join(pcap_directory, filename)
        
        # Call the iot() function with the file path
        iot(file_path)
```

#### Filtering TCP PCAP Files
CyberSecTK allows you to filter specific TCP PCAP files using a Python dictionary named `ip_filter`. This dictionary should be defined in your script before calling the `iot` function.

The library uses `tshark` to extract the features from the given TCP pcap file. Make sure `tshark` is installed on your system.

The `ip_filter` dictionary uses keys to specify the type of device and values to specify the IP addresses to filter. The filtered pcap file will be saved with its filtered name inside the `filtered_pcap` directory.

Here are the available keys for the `ip_filter` dictionary:

- `TCP_Mobile`
- `TCP_Outlet`
- `TCP_Assistant`
- `TCP_Camera`
- `TCP_Miscellaneous`

Here's an example of how to define the `ip_filter` dictionary:

```python
ip_filter = {}
ip_filter['TCP_Miscellaneous'] = "'tcp && (ip.src==192.168.1.216) || (ip.src==192.168.1.46) || (ip.src==192.168.1.84) || (ip.src==192.168.1.91)'"
```

In this example, the `TCP_Miscellaneous` key is associated with a string that specifies a TCP filter for several IP addresses. You can replace these IP addresses with the ones you want to filter.

To use the `ip_filter` dictionary, pass it as an argument to the `iot` function:

```python
from cybersectk.iot import iot
iot(**ip_filter)
```


### MALEWARE
The `malware` module extracts features from system log files to identify malicious activity.

```python
from cybersectk.malware import malware
malware()
```
 
This module outputs a NumPy array, which can be passed directly to a TensorFlow or PyTorch training script. 

Note: Before running the feature extraction, please ensure that you have created a directory named `log_files` in the same working directory. Inside the `log_files` directory, add the non-malicious system log files with names like `Good1.CSV`, `Good2.CSV`, and so on. For infected log files, please refer to the sample dataset provided for better understanding.

You can download the sample dataset from the following link:

[Sample Dataset](https://drive.google.com/drive/folders/1_mJUvA99cHsE09UxFb1Cpyik3fVaSy0N?usp=sharing)


## Feature Desrciptions
Each module extracts a different set of features. For detailed descriptions of the features extracted by each module, see the [Feature Descriptions](Feature_Descriptions.md) document.

## Contributing
We welcome contributions to CyberSecTK! Please see out [Contributing Guide](Contributing_Guide.md) for more information.