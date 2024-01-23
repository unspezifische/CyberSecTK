**Wireless IOT Features**
> Feature selection is based on wireless DataLink layer header information.

|Features	| Description|
|---|---|
|Version |	Radiotap Frame control field indicates the current WLAN protocol version.|
|Pad |	Radiotap Frame control field aligns onto natural word boundaries, that means all 8, 16, 32, and 64-bit fields must begin respectively to avoid unaligned accesses to radiotap capture fields.|
|Len |	Specifies entire length of radiotap data including radiotap header.|
|Rate |	Data transfer rate of a device i.e. 2.0 Mb/s etc.| 
|ChannelFrequency |	Device operating channel frequency i.e. radio wave spectrum type a,b,g,n |
|ChannelFlags |	Specifies device supported spectrum coding method designed to avoid collision.|
|DBM_AntSignal |	Transmitting wireless device radio antenna strength in dBm.|
|Antenna |	Number of available transceiving radio antennas.|
|Subtype |	Specified the frame sub type i.e. association request (0000), association response (0001), beacon (1000), probe request (0100) etc.|
|Type |	Determine the function of frame type i.e. management (00), control (01) or data (10).|  
|Proto	| WLAN Protocol version.|
|FCfield	| Specifies wireless frame flag i.e. to-DS, from-DS, retry, power, protected, etc.| 
|ID	| Connection ID assigned between source and destination over a period within maximum datagram lifetime (MDL).|
|Addr1 |	Wireless device MAC address (destination/recipient).|
|Addr2 |	Wireless device MAC address (relay/source).|
|Addr3 |	Wireless device MAC address (BSSID/source/destination).|
|SC |	Wireless packets Sequence control.|
|Addr4 |	Wireless device Mac Address (BSSID/source).|
|Dot11Elt.ID	| Dot11 beacon type specific e.g. 0 for management i.e. SSID.|  
|Dot11Elt.len |	Length of specific Dot11Elt packet sequence payload.|
|Dot11Elt.info	| Information of the Dot11Elt packet sequence.|

**IOT Features**
> Feature selection is based on TCP/IP packet.

| Features | Description |
|--- | --- |
|Label | Specifies the device type eg. Mobile, Camera, outlet, etc.|
|IPLength |	Total length of the IP packets.|
|IPHeaderLength |	Packets IP header length. |
|TTL |	Time to live filed, helps to maintain packets from looping endlessly.|
|Protocol |	Packet protocol field indicates packets upper-layer protocols.| 
|DestPort |	Destination Port fields helps to identify the end points of the connection.|
|SequenceNumber |	Initialize the sequence number assigned to PDU at the time of data transmission. |
|AckNumber |	Acknowledge the value specific to the sequence of data expecting to receive in the next sequence number.| 
|WindowSize	| Specified the packet buffer space available for incoming data.|
|TCPHeaderLength |	TCP packet header length.|
|TCPLength |	Total TCP packet length.|
|TCPStream |	Specifies the segments of the TCP PDU (Protocol Data Units).|
|TCPUrgentPointer | Data bytes set as urgent flag in the TCP header for immediate process.|
|IPFlags |	3 bits field value set to control or identify the fragments of the IP packets eg. Reserved (R) , Don’t fragment (DF) and More fragments (MF).|
|IPID |	Unique identification field value assigned for every PDU, between a source and destination of a given protocol over a period within maximum datagram lifetime (MDL).|
|IPchecksum |	Detect corruption in IPv4 packets header.|
|TCPflags |	Specifies the particular state of TCP connection, fields use like SYN, ACK, FIN, RST, etc. |
|TCPChecksum	| Detect corruption in TCP packed payload and the header.|

**Dynamic Malware Matrix Features** 
> TOP 20 Selected features out of 1000.

|Features |	Description |
|---|---|
|events_31bf3856ad364e35_6	| Windows system update service packages corrupt.|
|onent |	OneNote email association to send contents to notebooks by emailing.|
|directx	| DirectX error leading to tech support scams paying for unnecessary technical support service.| 
|resources_31bf3856ad364e35_8	| Error code 37 leading to tech support scams paying for unnecessary technical supports service.| 
|oem	| Original Equipment Manufacturer version use to build windows system.|
|adm_31bf3856ad364e35_6 |	Operating System misconfigured, missing or damaged important system files leading system crash with errors.| 
|resources_b03f5f7f11d50a3a_en |	.NET framework vulnerability could allow security feature bypass.|
|client_31bf3856ad364e35_6 |	Service stop error trying to connect to a printer server in windows (error 0x00000006).|
|rds |	Relational Database Service error.| 
|pcat |	Windows update patch error leading system crash, boot loader manager error.| 
|core_31bf3856ad364e35_6 |	Windows remote desktop service access error.|
|identity|	Services directory application or web service user authentication error due to account group policy.|  
|inf_31bf3856ad364e35_6 |	Windows OS network adaptor stop/disable error eg. Stop: 0x0000000A (parameter1, parameter2, parameter3, parameter4) IRQL_NOT_LESS_OR_EQUAL|
|resources_31bf3856ad364e35_6 |	Windows DNS service updates configuration rules.|
|anguagepack_31bf3856ad364e35_6|	Windows system32 components service configuration error.|
|resources_b03f5f7f11d50a3a_6 |	Windows security update for .NET framework.|
|mdac	|Microsoft Data Access Components core data access components eg. Microsoft SQL server.|
|dll_31bf3856ad364e35_6 |	Microsoft windows operating system, crypto API32.DLL file.|
|driverclass_31bf3856ad364e35_6 |	Windows security update installation problem.|
|msil_system	| Security update for .NET framework service.|
