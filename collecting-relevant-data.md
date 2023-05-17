Running on stock firmware on a root shell:
```
# ls /var/log/
# ls /sys/
```
```
# cat /proc/cmdline
 console=ttyS0,115200
```
```
# cat /proc/cpuinfo
system type		: RTL9300
machine			: RTL9300
processor		: 0
cpu model		: MIPS 34Kc V5.5
BogoMIPS		: 531.66
wait instruction	: yes
microsecond timers	: yes
tlb_entries		: 32
extra interrupt vector	: yes
hardware watchpoint	: no
isa			: mips1 mips32r2
ASEs implemented	: mips16
shadow register sets	: 1
kscratch registers	: 0
package			: 0
core			: 0
```
```
# cat /proc/meminfo
MemTotal:         255972 kB
MemFree:          233288 kB
MemAvailable:     241428 kB
Buffers:               0 kB
Cached:            13272 kB
SwapCached:            0 kB
Active:             7692 kB
Inactive:           5868 kB
Active(anon):        288 kB
Inactive(anon):        0 kB
Active(file):       7404 kB
Inactive(file):     5868 kB
Unevictable:           0 kB
Mlocked:               0 kB
HighTotal:             0 kB
HighFree:              0 kB
LowTotal:         255972 kB
LowFree:          233288 kB
SwapTotal:             0 kB
SwapFree:              0 kB
Dirty:                 0 kB
Writeback:             0 kB
AnonPages:           324 kB
Mapped:             1004 kB
Shmem:                 0 kB
Slab:               3952 kB
SReclaimable:        260 kB
SUnreclaim:         3692 kB
KernelStack:         168 kB
PageTables:           56 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:      127984 kB
Committed_AS:        948 kB
VmallocTotal:    1015800 kB
VmallocUsed:        4116 kB
VmallocChunk:    1005464 kB
```
```
# cat /proc/devices
Character devices:
  1 mem
  2 pty
  3 ttyp
  4 ttyS
  5 /dev/tty
  5 /dev/console
  5 /dev/ptmx
 10 misc
 90 mtd
128 ptm
136 pts
180 usb
189 usb_device
200 rtcore

Block devices:
259 blkext
  8 sd
 65 sd
 66 sd
 67 sd
 68 sd
 69 sd
 70 sd
 71 sd
128 sd
129 sd
130 sd
131 sd
132 sd
133 sd
134 sd
135 sd
```
```
# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 001e0000 00001000 "LOADER"
mtd1: 00010000 00001000 "BDINFO"
mtd2: 00010000 00001000 "SYSINFO"
mtd3: 00080000 00001000 "JFFS2 CFG"
mtd4: 00080000 00001000 "JFFS2 LOG"
mtd5: 00680000 00001000 "RUNTIME"
mtd6: 00680000 00001000 "RUNTIME2"
```
```
# ifconfig -a
eth0      Link encap:Ethernet  HWaddr 78:2D:7E:13:EE:BC
          inet addr:1.1.10.100  Bcast:1.255.255.255  Mask:255.0.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
          Interrupt:32

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
```
```
# ls -l /bin
-rwxr-xr-x    1 0        0           89612 ubirsvol
-rwxr-xr-x    1 0        0          115795 nandwrite
-rwxr-xr-x    1 0        0          137797 mtdinfo
-rwxr-xr-x    1 0        0          235708 ubiformat
lrwxrwxrwx    1 0        0              14 insmod -> ../bin/busybox
lrwxrwxrwx    1 0        0               7 echo -> busybox
lrwxrwxrwx    1 0        0               7 mount -> busybox
-rwxr-xr-x    1 0        0           84494 ubirename
-rwxr-xr-x    1 0        0           35579 ubicrc32
lrwxrwxrwx    1 0        0               7 rmdir -> busybox
lrwxrwxrwx    1 0        0               7 false -> busybox
lrwxrwxrwx    1 0        0               7 hostname -> busybox
-rwxr-xr-x    1 0        0           20807 nandtest
lrwxrwxrwx    1 0        0               7 sh -> busybox
lrwxrwxrwx    1 0        0              14 init -> ../bin/busybox
-rwxr-xr-x    1 0        0         2218660 diag
lrwxrwxrwx    1 0        0               7 kill -> busybox
-rwxr-xr-x    1 0        0           86900 ubirmvol
lrwxrwxrwx    1 0        0               7 pwd -> busybox
-rwxr-xr-x    1 0        0          110647 ubinize
lrwxrwxrwx    1 0        0               7 umount -> busybox
lrwxrwxrwx    1 0        0               7 mv -> busybox
-rwxr-xr-x    1 0        0           91574 ubiattach
lrwxrwxrwx    1 0        0              14 ifconfig -> ../bin/busybox
lrwxrwxrwx    1 0        0               7 more -> busybox
lrwxrwxrwx    1 0        0               7 touch -> busybox
-rwxr-xr-x    1 0        0           16426 mtdpart
lrwxrwxrwx    1 0        0               7 rm -> busybox
lrwxrwxrwx    1 0        0              14 lsmod -> ../bin/busybox
lrwxrwxrwx    1 0        0               7 true -> busybox
lrwxrwxrwx    1 0        0               7 mkdir -> busybox
lrwxrwxrwx    1 0        0               7 df -> busybox
-rwxr-xr-x    1 0        0          103371 ubinfo
lrwxrwxrwx    1 0        0               7 ln -> busybox
-rwxr-xr-x    1 0        0          243256 busybox
lrwxrwxrwx    1 0        0               7 chown -> busybox
lrwxrwxrwx    1 0        0               7 uname -> busybox
lrwxrwxrwx    1 0        0               7 stty -> busybox
-rwxr-xr-x    1 0        0           95873 ubimkvol
-rwxr-xr-x    1 0        0           82970 ubidetach
lrwxrwxrwx    1 0        0              14 reboot -> ../bin/busybox
lrwxrwxrwx    1 0        0               7 ps -> busybox
-rwxr-xr-x    1 0        0          111995 nanddump
-rwxr-xr-x    1 0        0           13894 doc_loadbios
lrwxrwxrwx    1 0        0              14 modprobe -> ../bin/busybox
-rwxr-xr-x    1 0        0          103066 flash_erase
lrwxrwxrwx    1 0        0              14 rmmod -> ../bin/busybox
lrwxrwxrwx    1 0        0               7 ls -> busybox
-rwxr-xr-x    1 0        0           24911 ftl_format
lrwxrwxrwx    1 0        0               7 chmod -> busybox
-rwxr-xr-x    1 0        0           22853 mtd_debug
lrwxrwxrwx    1 0        0               7 netstat -> busybox
lrwxrwxrwx    1 0        0              14 halt -> ../bin/busybox
lrwxrwxrwx    1 0        0              14 start-stop-daemon -> ../bin/busybox
lrwxrwxrwx    1 0        0               7 cp -> busybox
lrwxrwxrwx    1 0        0               7 cat -> busybox
lrwxrwxrwx    1 0        0               7 msh -> busybox
-rwxr-xr-x    1 0        0           91016 ubiupdatevol
-rwxr-xr-x    1 0        0           27754 flashcp
-rwxr-xr-x    1 0        0           80686 ubiblock
lrwxrwxrwx    1 0        0               7 ping -> busybox
lrwxrwxrwx    1 0        0               7 date -> busybox
lrwxrwxrwx    1 0        0              14 poweroff -> ../bin/busybox
lrwxrwxrwx    1 0        0               7 mknod -> busybox
```
```
# ubinfo -a
ubinfo: error!: UBI is not present in the system
```
```
# mtdinfo -a
Count of MTD devices:           7
Present MTD devices:            mtd0, mtd1, mtd2, mtd3, mtd4, mtd5, mtd6
Sysfs interface supported:      no

mtd0
Name:                           LOADER
Type:                           nor
Eraseblock size:                4096 bytes, 4.0 KiB
Amount of eraseblocks:          480 (1966080 bytes, 1.9 MiB)
Minimum input/output unit size: 1 byte
Bad blocks are allowed:         true
Device is writable:             false

mtd0
Name:                           LOADER
Type:                           nor
Eraseblock size:                4096 bytes, 4.0 KiB
Amount of eraseblocks:          480 (1966080 bytes, 1.9 MiB)
Minimum input/output unit size: 1 byte
Bad blocks are allowed:         true
Device is writable:             false

mtd1
Name:                           BDINFO
Type:                           nor
Eraseblock size:                4096 bytes, 4.0 KiB
Amount of eraseblocks:          16 (65536 bytes, 64.0 KiB)
Minimum input/output unit size: 1 byte
Bad blocks are allowed:         true
Device is writable:             true

mtd1
Name:                           BDINFO
Type:                           nor
Eraseblock size:                4096 bytes, 4.0 KiB
Amount of eraseblocks:          16 (65536 bytes, 64.0 KiB)
Minimum input/output unit size: 1 byte
Bad blocks are allowed:         true
Device is writable:             true

mtd2
Name:                           SYSINFO
Type:                           nor
Eraseblock size:                4096 bytes, 4.0 KiB
Amount of eraseblocks:          16 (65536 bytes, 64.0 KiB)
Minimum input/output unit size: 1 byte
Bad blocks are allowed:         true
Device is writable:             true

mtd2
Name:                           SYSINFO
Type:                           nor
Eraseblock size:                4096 bytes, 4.0 KiB
Amount of eraseblocks:          16 (65536 bytes, 64.0 KiB)
Minimum input/output unit size: 1 byte
Bad blocks are allowed:         true
Device is writable:             true

mtd3
Name:                           JFFS2 CFG
Type:                           nor
Eraseblock size:                4096 bytes, 4.0 KiB
Amount of eraseblocks:          128 (524288 bytes, 512.0 KiB)
Minimum input/output unit size: 1 byte
Bad blocks are allowed:         true
Device is writable:             true
```
```
# doc_loadbios -h
You must specify a device, the source firmware file and the offset
```

Running the diag tool (`/bin/diag`):
```
# diag
edimaxSystemInit():140,Edimax System Init
edimaxSystemInit():157, configure ip cmd <ifconfig eth0 1.1.10.100>
RTK.0>
exit             - exit diag shell
unit             - unit configure
terminal         - terminal configuration
sdk              - sdk configuration
nic              - NIC configuration
stack            - stack configuration
oam              - OAM configuration
l2-ntfy          - L2-notification configuration
acl              - ACL configuration
debug            - debug configuration
diag             - diag configuration
serdes           - serdes interface
eee              - EEE configuration
flowctrl         - flowctrl configuration
l2-table         - l2 table configuration
l3               - l3 configuration
led              - LED configuration
mib              - mib configuration
mirror           - mirror configuration
rspan            - RSPAN configuration
sflow            - sFlow configuration
port             - port configuration
qos              - QoS configuration
bandwidth        - bandwidth configuration
storm-control    - storm-control configuration
register         - register configuration
vlan             - VLAN configuration
security         - security configuration
stp              - stp configuration
switch           - switch configuration
sys              - system
rise             - stacking protocol demo 2
time             - time configuration
trap             - trap configuration
trunk            - trunk configuration
ipmcast          - ipmcast configuration
mcast            - mcast configuration
pie              - PIE configuration
field-selector   - field selector configuration
range-check      - range check configuration
gpio             - generalCtrl GPIO configuration
spi              - SPI configuration
i2c              - I2C configuration
sys-config       - sys-config configuration
```
```
RTK.0> sdk
set              - set configuration
```
```
RTK.0> nic
set              - set configuration
dump             - dump configuration
reset            - reset configuration
get              - get configuration

RTK.0> nic dump
buffer-usage     - buffer usage
pkthdr-mbuf      - packet and mbuf usage
counter          - counter
```
```
RTK.0> stack
get              - get configuration
set              - set configuration

RTK.0> stack get
port             - stacking ports
devID            - stacking device ID of the switch
master-devID     - stacking master device
loop-guard       - loop guard that drop the packets looping back to the switch
dev-port-map     - device to port map
non-unicast-block - non-unicast packets blocking configuration
```
```
RTK.0> oam
get              - get configuration
set              - set configuration

RTK.0> oam get
asic-auto-dying-gasp - asic dying gasp configuration
dying-gasp       - dying gasp configuration
loopback-ctrl    - loopback mode configuration
pdu              - pdu configuration
```
```
RTK.0> debug
get              - get configuration
dump             - dump configuration
set              - set configuration
flashtest        - flashtest configuration
phy              - phy

RTK.0> debug dump
hsa              - header stamp after information
hsb              - header stamp before information
hsm              - header stamp middle information
mib              - mib configuration
8295r            - 8295r
```
```
RTK.0> diag
set              - set configuration
get              - set configuration
dump             - dump registers or tables in console
wholedump        - dump whole chip information in console
clear            - clear configuration

RTK.0> diag wholedump
mac-reg          - whole MAC realted registers
phy-reg          - whole PHY standard registers
soc-reg          - soc related registers
table            - whole switch related tables
all              - mac-reg, phy-reg, soc-reg and table
```
(See diag-wholedump-all.txt)

```
RTK.0> serdes
get              - get configuration
set              - set configuration
reset            - reset configuration
clear            - clear configuration
eye-monitor      - eye-monitor configuration

RTK.0> serdes get
<UINT:sdsId>     - serdes index
id               - serdes index

RTK.0> serdes get 0
rx-cali          - rx-calibration
link-status      - link status information
rx-sym-err       - rx symbol error count
testmode         - test mode
leq              - LEQ configuration
cmu-band         - cmu band
eye-param        - eye parameter configuration
```
```
RTK.0> serdes get 0 link-status
Error (0xf00c): Input parameter is out of range

RTK.0> serdes get 1 link-status
Error (0xf00c): Input parameter is out of range

RTK.0> serdes get 2 link-status
Error (0xf00c): Input parameter is out of range

RTK.0> serdes get 3 link-status
sds3: sts1=0x0 sts0=0x0, latch_sts1=0x0 latch_sts0=0x0

RTK.0> serdes get 4 link-status
sds4: sts1=0x0 sts0=0x0, latch_sts1=0x0 latch_sts0=0x0

RTK.0> serdes get 5 link-status
sds5: sts1=0x0 sts0=0x0, latch_sts1=0x0 latch_sts0=0x0

RTK.0> serdes get 6 link-status
sds6: sts1=0x0 sts0=0x0, latch_sts1=0x0 latch_sts0=0x0

RTK.0> serdes get 7 link-status
sds7: sts1=0x0 sts0=0x0, latch_sts1=0x0 latch_sts0=0x0

RTK.0> serdes get 8 link-status
Error (0xf00c): Input parameter is out of range
```
```
RTK.0> serdes get 3 rx-cali param-cfg
SDS 3:
 dacLongCableOffset   : 0,
 tap0InitVal          : 0x1F,
 vthMinThr            : 0x1,
 eqHoldEnable         : DISABLED,
 dfeTap1_4Enable      : ENABLED,

RTK.0> serdes get 4 rx-cali param-cfg
SDS 4:
 dacLongCableOffset   : 0,
 tap0InitVal          : 0x1F,
 vthMinThr            : 0x1,
 eqHoldEnable         : DISABLED,
 dfeTap1_4Enable      : ENABLED,

RTK.0> serdes get 5 rx-cali param-cfg
SDS 5:
 dacLongCableOffset   : 0,
 tap0InitVal          : 0x1F,
 vthMinThr            : 0x1,
 eqHoldEnable         : DISABLED,
 dfeTap1_4Enable      : ENABLED,

RTK.0> serdes get 6 rx-cali param-cfg
SDS 6:
 dacLongCableOffset   : 0,
 tap0InitVal          : 0x1F,
 vthMinThr            : 0x1,
 eqHoldEnable         : DISABLED,
 dfeTap1_4Enable      : ENABLED,

RTK.0> serdes get 7 rx-cali param-cfg
SDS 7:
 dacLongCableOffset   : 0,
 tap0InitVal          : 0x1F,
 vthMinThr            : 0x1,
 eqHoldEnable         : DISABLED,
 dfeTap1_4Enable      : ENABLED,
 ```
 ```
 RTK.0> led
get              - get configuration
set              - set configuration

RTK.0> led get
software-control - software control configuration
system           - system configuration
blink-time       - blinking time

RTK.0> led get system
sys              - sys type

RTK.0> led get system sys
mode             - mode configuration
state            - state configuration

RTK.0> led get system sys mode
System LED mode: blinking per 64ms
RTK.0> led get system sys state
System LED: Disable

RTK.0> led get software-control
<PORT_LIST:port> - port list
all              - all ports

RTK.0> led get software-control all
mode             - mode configuration
state            - state configuration

RTK.0> led get software-control all mode
LED Softward Control Mode Configuration:
Port 8:
  LED entity 0:
    Copper mode: off
     Fiber mode: off
  LED entity 1:
    Copper mode: off
     Fiber mode: off
  LED entity 2:
    Copper mode: off
     Fiber mode: off
  LED entity 3:
    Copper mode: off
     Fiber mode: off
Port 16:
  LED entity 0:
    Copper mode: off
     Fiber mode: off
  LED entity 1:
    Copper mode: off
     Fiber mode: off
  LED entity 2:
    Copper mode: off
     Fiber mode: off
  LED entity 3:
    Copper mode: off
     Fiber mode: off
Port 20:
  LED entity 0:
    Copper mode: off
     Fiber mode: off
  LED entity 1:
    Copper mode: off
     Fiber mode: off
  LED entity 2:
    Copper mode: off
     Fiber mode: off
  LED entity 3:
    Copper mode: off
     Fiber mode: off
Port 24:
  LED entity 0:
    Copper mode: off
     Fiber mode: off
  LED entity 1:
    Copper mode: off
     Fiber mode: off
  LED entity 2:
    Copper mode: off
     Fiber mode: off
  LED entity 3:
    Copper mode: off
     Fiber mode: off
Port 25:
  LED entity 0:
    Copper mode: off
     Fiber mode: off
  LED entity 1:
    Copper mode: off
     Fiber mode: off
  LED entity 2:
    Copper mode: off
     Fiber mode: off
  LED entity 3:
    Copper mode: off
     Fiber mode: off

RTK.0> led get software-control all state
LED Softward Control State Configuration:
Port 8:
  LED entity 0: Disable
  LED entity 1: Disable
  LED entity 2: Disable
  LED entity 3: Disable
Port 16:
  LED entity 0: Disable
  LED entity 1: Disable
  LED entity 2: Disable
  LED entity 3: Disable
Port 20:
  LED entity 0: Disable
  LED entity 1: Disable
  LED entity 2: Disable
  LED entity 3: Disable
Port 24:
  LED entity 0: Disable
  LED entity 1: Disable
  LED entity 2: Disable
  LED entity 3: Disable
Port 25:
  LED entity 0: Disable
  LED entity 1: Disable
  LED entity 2: Disable
  LED entity 3: Disable
```
```
RTK.0> port
dump             - dump configuration
get              - get configuration
set              - set configuration
add              - add configuration
del              - del configuration
reset            - reset configuration

RTK.0> port dump
cpu-port         - CPU port id
isolation        - traffic isolation configuration
port             - port configuration

RTK.0> port dump cpu-port
CPU port: 28

RTK.0> port dump isolation
  Port  8 : Isolation Port list 0-28
  Port 16 : Isolation Port list 0-28
  Port 20 : Isolation Port list 0-28
  Port 24 : Isolation Port list 0-28
  Port 25 : Isolation Port list 0-28

 Restrict Route:Disable

RTK.0> port dump isolation vlan-based
Index |Lo-VID |Up-VID |Trust Port list       |State
------+-------+-------+----------------------+--------

Total Number Of Entries : 0

RTK.0> port dump port all
Port  8 :
  Media                 : Copper
  Admin                 : Enable
  Mac Tx                : Enable
  Mac Rx                : Enable
  Back Pressure         : Enable
  Link                  : UP  Speed : 1000F
  AutoNego              : Enable
  AutoNego Ability      : 100H 100F 1000F 2.5G 5G 10G/F Flow-Control Asy-Flow-Control
  Giga-Lite             : (Function is not supported by this port)
  Flow Control (actual) : Disable
  Cross Over Mode       : (Function is not supported by this port)
Port 16 :
  Media                 : Copper
  Admin                 : Enable
  Mac Tx                : Enable
  Mac Rx                : Enable
  Back Pressure         : Enable
  Link                  : DOWN
  AutoNego              : Enable
  AutoNego Ability      : 100H 100F 1000F 2.5G 5G 10G/F Flow-Control Asy-Flow-Control
  Giga-Lite             : (Function is not supported by this port)
  Cross Over Mode       : (Function is not supported by this port)
Port 20 :
  Media                 : Copper
  Admin                 : Enable
  Mac Tx                : Enable
  Mac Rx                : Enable
  Back Pressure         : Enable
  Link                  : DOWN
  AutoNego              : Enable
  AutoNego Ability      : 100H 100F 1000F 2.5G 5G 10G/F Flow-Control Asy-Flow-Control
  Giga-Lite             : (Function is not supported by this port)
  Cross Over Mode       : (Function is not supported by this port)
Port 24 :
  Media                 : Copper
  Admin                 : Enable
  Mac Tx                : Enable
  Mac Rx                : Enable
  Back Pressure         : Enable
  Link                  : DOWN
  AutoNego              : Enable
  AutoNego Ability      : 100H 100F 1000F 2.5G 5G 10G/F Flow-Control Asy-Flow-Control
  Giga-Lite             : (Function is not supported by this port)
  Cross Over Mode       : (Function is not supported by this port)
Port 25 :
  Media                 : Copper
  Admin                 : Enable
  Mac Tx                : Enable
  Mac Rx                : Enable
  Back Pressure         : Enable
  Link                  : DOWN
  AutoNego              : Enable
  AutoNego Ability      : 100H 100F 1000F 2.5G 5G 10G/F Flow-Control Asy-Flow-Control
  Giga-Lite             : (Function is not supported by this port)
  Cross Over Mode       : (Function is not supported by this port)
```
```
RTK.0> switch
get              - get configuration
set              - set configuration
kick             - kick configuration

RTK.0> switch get
chksum-err-type  - checksum error type
crc-recal        - CRC recalculation
dev-capabilities - dev capabilities
mac-address      - system MAC address configuration
oui-00-00-00     - OUI(00-00-00) comparing configuration
cpu-max-pkt-len  - CPU port maximum packet length
max-pkt-len      - max packet length
probe-information - probe information
sdk-version      - sdk version
tc               - tc configuration
watchdog         - watchdog configuration
pppoe-ip-parse   - pppoe-IP-parse configuration
pkt2cpu          - packet to cpu configuration
cpu-packet-truncate - CPU packet truncation configuration

RTK.0> switch get sdk-version
SDK       version : 3.6.1.1
OS        version : Linux 3.18.24
Compiler  version : GCC 4.8.5
C Library version : uClibc-0.9.33.2 with NPTL

RTK.0> switch get mac-address
MAC address : 78:2D:7E:13:EE:BC

RTK.0> switch get tc
id               - tc id

RTK.0> switch get tc id
<UINT:id>        - id configuration 0-4

RTK.0> switch get tc id 0
usec:120 tv.nsec:230
RTK.0> switch get tc id 1
usec:1956935 tv.nsec:110
RTK.0> switch get tc id 2
usec:0 tv.nsec:0
RTK.0> switch get tc id 3
usec:0 tv.nsec:0
RTK.0> switch get tc id 4
usec:237826 tv.nsec:870

RTK.0> switch get max-pkt-len
port             - port configuration

RTK.0> switch get max-pkt-len port
<PORT_LIST:ports> - port list
all              - all ports

RTK.0> switch get max-pkt-len port all
fe               - fast ethernet speed
ge               - giga speed
tag-length-state - tag counting state configuration

RTK.0> switch get max-pkt-len port all ge
Max Packet Length in Giga Speed
Port 8 : 12288
Port 16 : 12288
Port 20 : 12288
Port 24 : 12288
Port 25 : 12288

RTK.0> switch get cpu-max-pkt-len
rx-dir           - Rx direction
tx-dir           - Tx direction

RTK.0> switch get cpu-max-pkt-len tx-dir
CPU Port Max Packet Length (Tx) : 12288

RTK.0> switch get cpu-max-pkt-len rx-dir
CPU Port Max Packet Length (Rx) : 1536

RTK.0> switch get probe-information
Unit ID: 0
Chip ID: 9303 (RTL9303)
Family ID: 9300
Port Number:  6
All Port Number:  6, Minimum:  8, Maximum: 28, Ports: 8,16,20,24-25,28
Ether Port Number:  5, Minimum:  8, Maximum: 25, Ports: 8,16,20,24-25
10GE Port Number:  5, Minimum:  8, Maximum: 25, Ports: 8,16,20,24-25
Copper Port Number:  5, Minimum:  8, Maximum: 25, Ports: 8,16,20,24-25
CPU Port : 28

Port     PHY chip
======================
  8      CUST1
 16      CUST1
 20      CUST1
 24      CUST1
 25      CUST1

RTK.0> switch get dev-capabilities

CHIP_ID                       RTL9300_FAMILY_ID
HWP_IDENTIFIER_NAME               RTL9303_2x84892_1x84891
HWP_IDENTIFIER_ID                 9300009
HWP_UNIT_VALID_LOCAL              1
HWP_UNIT_VALID_STACK              1
HWP_IS_CPU_UNIT                   1
HWP_UNIT_VALID_LOCAL              1
HWP_PORT_COUNT                    6
HAL_GET_MAX_BANDWIDTH_OF_PORT                       1048575
HAL_MAX_NUM_OF_MIRROR                               4
HAL_MAX_NUM_OF_TRUNK                                64
HAL_MAX_NUM_OF_TRUNK_IN_STACKING_MODE               64
HAL_MAX_NUM_OF_STACK_TRUNK                          2
HAL_MAX_NUM_OF_LOCAL_TRUNK                          29
HAL_MAX_NUM_OF_TRUNKMEMBER                          8
HAL_MAX_NUM_OF_TRUNK_ALGO                           2
HAL_TRUNK_ALGO_SHIFT_MAX                            5
HAL_MAX_NUM_OF_DUMB_TRUNKMEMBER                     8
HAL_MAX_NUM_OF_TRUNKHASHVAL                         64
HAL_MAX_NUM_OF_MSTI                                 64
HAL_MAX_NUM_OF_SVL                                  1
HAL_MAX_NUM_OF_METERING                             256
HAL_MAX_NUM_OF_METER_BLOCK                          16
HAL_RATE_OF_METER_MAX                               1048575
HAL_BURST_SIZE_OF_ACL_METER_MIN                     3021
HAL_BURST_SIZE_OF_ACL_METER_MAX                     131071
HAL_MAX_NUM_OF_PIE_BLOCK                            16
HAL_MAX_NUM_OF_PIE_BLOCKSIZE                        128
HAL_MAX_NUM_OF_PIE_COUNTER                          2048
HAL_MAX_NUM_OF_PIE_TEMPLATE                         10
HAL_PIE_USER_TEMPLATE_ID_MIN                        5
HAL_PIE_USER_TEMPLATE_ID_MAX                        9
HAL_MAX_NUM_OF_FIELD_SELECTOR                       12
HAL_MAX_OFST_OF_FIELD_SELECTOR                      179
HAL_MAX_NUM_OF_PIE_FILTER_ID                        2048
HAL_MAX_NUM_OF_PIE_BLOCK_TEMPLATESELECTOR           2
HAL_MAX_NUM_OF_PIE_BLOCK_GRP                        16
HAL_MAX_NUM_OF_PIE_BLOCK_LOGIC                      16
HAL_MAX_NUM_OF_PIE_TEMPLATE_FIELD                   12
HAL_MAX_NUM_OF_RANGE_CHECK_IP                       8
HAL_MAX_NUM_OF_RANGE_CHECK                          16
HAL_MAX_NUM_OF_METADATA                             256
HAL_L2_HASHDEPTH                                    4
HAL_L2_HASHWIDTH                                    0
HAL_MAX_NUM_OF_QUEUE                                8
HAL_MIN_NUM_OF_QUEUE                                1
HAL_MAX_NUM_OF_CPU_QUEUE                            32
HAL_MAX_NUM_OF_STACK_QUEUE                          12
HAL_MAX_NUM_OF_IGR_QUEUE                            0
HAL_MIN_NUM_OF_IGR_QUEUE                            0
HAL_MAX_NUM_OF_CVLAN_TPID                           4
HAL_MAX_NUM_OF_SVLAN_TPID                           4
HAL_MAX_NUM_OF_EVLAN_TPID                           1
HAL_TPID_ENTRY_IDX_MAX                              3
HAL_TPID_ENTRY_MASK_MAX                             15
HAL_PROTOCOL_VLAN_IDX_MAX                           7
HAL_VLAN_FID_MAX                                    4095
HAL_FLOWCTRL_THRESH_MAX                             4095
HAL_FLOWCTRL_PAUSEON_PAGE_PACKET_LEN_MAX            65535
HAL_FLOWCTRL_PAUSEON_PAGE_PACKET_MAX                4095
HAL_PRI_OF_SELECTION_MAX                            8
HAL_PRI_OF_SELECTION_MIN                            0
HAL_DP_OF_SELECTION_MAX                             3
HAL_DP_OF_SELECTION_MIN                             0
HAL_PRI_SEL_GROUP_INDEX_MAX                         3
HAL_QUEUE_WEIGHT_MAX                                127
HAL_IGR_QUEUE_WEIGHT_MAX                            0
HAL_RATE_OF_BANDWIDTH_MAX                           1048575
HAL_RATE_OF_10G_BANDWIDTH_MAX                       625000
HAL_BURST_OF_IGR_BANDWIDTH_MAX                      2147483647
HAL_BURST_OF_BANDWIDTH_MAX                          65535
HAL_BURST_OF_STORM_CONTROL_MAX                      65535
HAL_BURST_OF_STORM_PROTO_CONTROL_MAX                0
HAL_THRESH_OF_EGR_QUEUE_DROP_GROUP_IDX_MAX          3
HAL_THRESH_OF_ETE_FC_REMOTE_PORT_GROUP_IDX_MAX      1
HAL_THRESH_OF_IGR_PORT_PAUSE_CONGEST_GROUP_IDX_MAX  3
HAL_THRESH_OF_IGR_BW_FLOWCTRL_MIN                   0
HAL_THRESH_OF_IGR_BW_FLOWCTRL_MAX                   2147483647
HAL_MAX_NUM_OF_FASTPATH_OF_RATE                     0
HAL_RATE_OF_STORM_CONTROL_MAX                       16777215
HAL_RATE_OF_STORM_PROTO_CONTROL_MAX                 511
HAL_BURST_RATE_OF_STORM_CONTROL_MIN                 5178
HAL_BURST_RATE_OF_STORM_CONTROL_MAX                 65535
HAL_BURST_RATE_OF_10G_STORM_CONTROL_MIN             5178
HAL_BURST_RATE_OF_10G_STORM_CONTROL_MAX             65535
HAL_BURST_RATE_OF_STORM_PROTO_CONTROL_MAX           255
HAL_INTERNAL_PRIORITY_MAX                           7
HAL_DROP_PRECEDENCE_MAX                             2
HAL_PRIORITY_REMAP_GROUP_IDX_MAX                    0
HAL_PRIORITY_REMARK_GROUP_IDX_MAX                   0
HAL_WRED_WEIGHT_MAX                                 0
HAL_WRED_MPD_MAX                                    0
HAL_WRED_DROP_PROBABILITY_MAX                       255
HAL_MAX_NUM_OF_L2_HASH_ALGO                         2
HAL_L2_LEARN_LIMIT_CNT_MAX                          16448
HAL_L2_LEARN_LIMIT_CNT_WO_CAM_MAX                   16384
HAL_L2_LEARN_LIMIT_CNT_DISABLE                      32767
HAL_L2_FID_LEARN_LIMIT_ENTRY_MAX                    8
HAL_L2_NTFY_BP_THR_MAX                              1024
HAL_MAX_NUM_OF_VRF                                  0
HAL_MAX_NUM_OF_INTF                                 64
HAL_MAX_NUM_OF_INTF_MTU                             8
HAL_MAX_NUM_OF_INTF_MTU_VALUE                       16383
HAL_MAX_NUM_OF_L3_ECMP                              0
HAL_MAX_NUM_OF_L3_ECMP_HASH_IDX                     0
HAL_MAX_NUM_OF_L3_ECMP_NEXTHOP                      0
HAL_MAX_NUM_OF_L3_NEXTHOP                           2048
HAL_MAX_NUM_OF_L3_HOST                              6144
HAL_MAX_NUM_OF_L3_ROUTE                             512
HAL_MAX_NUM_OF_L3_CONFLICT_HOST                     16
HAL_MAX_NUM_OF_L3_MCAST_GROUP_NEXTHOP               66
HAL_MAX_NUM_OF_TUNNEL                               0
HAL_MAX_NUM_OF_TUNNEL_QOS_PROFILE                   0
HAL_EEE_QUEUE_THRESH_MAX                            4095
HAL_SEC_MINIPV6FRAGLEN_MAX                          65535
HAL_SEC_MAXPINGLEN_MAX                              65535
HAL_SEC_SMURFNETMASKLEN_MAX                         32
HAL_MAX_NUM_OF_IP_MAC_BIND_ENTRY                    0
HAL_SFLOW_RATE_MAX                                  65535
HAL_MAX_NUM_OF_MCAST_FWD                            1024
HAL_MIIM_PAGE_ID_MAX                                4095
HAL_MAX_NUM_OF_C2SC_ENTRY                           1024
HAL_MAX_NUM_OF_C2SC_BLK_ENTRY                       128
HAL_MAX_NUM_OF_C2SC_BLK                             8
HAL_MAX_NUM_OF_C2SC_RANGE_CHECK_VID                 32
HAL_MAX_NUM_OF_C2SC_RANGE_CHECK_SET                 2
HAL_MAX_NUM_OF_SC2C_ENTRY                           512
HAL_MAX_NUM_OF_SC2C_RANGE_CHECK_VID                 32
HAL_MAX_NUM_OF_SC2C_RANGE_CHECK_SET                 2
HAL_MAX_NUM_OF_VLAN_PROFILE                         8
HAL_MAX_ACCEPT_FRAME_LEN                            12288
HAL_MAX_NUM_OF_MCAST_ENTRY                          1024
HAL_MAX_NUM_OF_VLAN_PORT_ISO_ENTRY                  16
HAL_MAX_NUM_OF_MPLS_ENCAP                           0
HAL_MAX_NUM_OF_MPLS_DECAP                           0
HAL_MAX_NUM_OF_MPLS_DECAP_CAM                       0
HAL_MAX_NUM_OF_MPLS_DECAP_ENTRY                     0
HAL_MAX_NUM_OF_MPLS_NEXTHOP                         0
HAL_MPLS_HASHDEPTH                                  0
HAL_OF_BYTE_CNTR_TH_MAX                             0
HAL_OF_PKT_CNTR_TH_MAX                              0
HAL_MAX_NUM_OF_OF_IGR_FLOWTBL                       0
HAL_MAX_NUM_OF_OF_VIRTUAL_IGR_FLOWTBL               0
HAL_OF_LOOPBACK_MAX                                 7
HAL_OF_MAX_NUM_OF_GRP_ENTRY                         0
HAL_OF_MAX_NUM_OF_GRP_ENTRY_BUCKET                  0
HAL_OF_MAX_NUM_OF_ACTION_BUCKET                     0
HAL_OF_MAX_NUM_OF_DMAC_ENTRY                        0
HAL_MAX_NUM_OF_ROUTE_HOST_ADDR                      2048
HAL_MAX_NUM_OF_ROUTE_SWITCH_ADDR                    64
HAL_MAX_NUM_OF_NEXTHOP                              2048
HAL_MAX_NUM_OF_LED_ENTITY                           4
HAL_MAX_NUM_OF_DYING_GASP_PKT_CNT                   7
HAL_DYING_GASP_SUSTAIN_TIME_MAX                     65535
HAL_MAX_NUM_OF_RMA_USER_DEFINED                     4
HAL_TIME_NSEC_MAX                                   0
HAL_TIME_FREQ_MAX                                   0
HAL_MAX_NUM_OF_ETHDM_RX_TIMESTAMP                   0
HAL_BPE_PVID_HASHDEPTH                              0
HAL_MAX_NUM_OF_STACK_PORT                           4
 RTK_DOT1P_PRIORITY_MAX                         7
 RTK_VLAN_ID_MAX                                4095
 RTK_VLAN_ID_MIN                                0
 RTK_DOT1P_CFI_MAX                              1
 RTK_DOT1P_DEI_MAX                              1
 RTK_VALUE_OF_DSCP_MAX                          63
 RTK_DROP_PRECEDENCE_MAX                        2
HWP_PORT_EXIST(0) 0
HWP_PORT_EXIST(1) 0
HWP_PORT_EXIST(2) 0
HWP_PORT_EXIST(3) 0
HWP_PORT_EXIST(4) 0
HWP_PORT_EXIST(5) 0
HWP_PORT_EXIST(6) 0
HWP_PORT_EXIST(7) 0
HWP_PORT_EXIST(8) 1
HWP_PORT_EXIST(9) 0
HWP_PORT_EXIST(10) 0
HWP_PORT_EXIST(11) 0
HWP_PORT_EXIST(12) 0
HWP_PORT_EXIST(13) 0
HWP_PORT_EXIST(14) 0
HWP_PORT_EXIST(15) 0
HWP_PORT_EXIST(16) 1
HWP_PORT_EXIST(17) 0
HWP_PORT_EXIST(18) 0
HWP_PORT_EXIST(19) 0
HWP_PORT_EXIST(20) 1
HWP_PORT_EXIST(21) 0
HWP_PORT_EXIST(22) 0
HWP_PORT_EXIST(23) 0
HWP_PORT_EXIST(24) 1
HWP_PORT_EXIST(25) 1
HWP_PORT_EXIST(26) 0
HWP_PORT_EXIST(27) 0
HWP_PORT_EXIST(28) 1
HWP_CPU_PORT(28) 8
HWP_PORT_EXIST(29) 0
HWP_PORT_EXIST(30) 0
HWP_PORT_EXIST(31) 0
HWP_PORT_EXIST(32) 0
HWP_PORT_EXIST(33) 0
HWP_PORT_EXIST(34) 0
HWP_PORT_EXIST(35) 0
HWP_PORT_EXIST(36) 0
HWP_PORT_EXIST(37) 0
HWP_PORT_EXIST(38) 0
HWP_PORT_EXIST(39) 0
HWP_PORT_EXIST(40) 0
HWP_PORT_EXIST(41) 0
HWP_PORT_EXIST(42) 0
HWP_PORT_EXIST(43) 0
HWP_PORT_EXIST(44) 0
HWP_PORT_EXIST(45) 0
HWP_PORT_EXIST(46) 0
HWP_PORT_EXIST(47) 0
HWP_PORT_EXIST(48) 0
HWP_PORT_EXIST(49) 0
HWP_PORT_EXIST(50) 0
HWP_PORT_EXIST(51) 0
HWP_PORT_EXIST(52) 0
HWP_PORT_EXIST(53) 0
HWP_PORT_EXIST(54) 0
HWP_PORT_EXIST(55) 0
HWP_PORT_EXIST(56) 0
HWP_PORT_EXIST(57) 0
HWP_PORT_EXIST(58) 0
HWP_PORT_EXIST(59) 0
HWP_PORT_EXIST(60) 0
HWP_PORT_EXIST(61) 0
HWP_PORT_EXIST(62) 0
HWP_PORT_EXIST(63) 0
```
```
RTK.0> sys
dump             - dump configuration
load             - load configuration
command          - command

RTK.0> sys dump
hwp              - hardware profile

RTK.0> sys dump hwp
all              - all info
info             - hwp info
unit             - unit info
parsed_info      - parsed info

RTK.0> sys dump hwp all
    Profile Information (C0090BD8):
      Profile-Name: RTL9303_2x84892_1x84891
      Profile-ID: 9300009
      Profile-ID-Type: 0
      CPU Type: Embedded
      SW Desc IDX: 0
      Slave Interrupt Pin: 255
      Chip count: 1
      Cascade Mode: No
        unit  0, 9303(1) (cpu)
          swcore support: 1
          swcore-CPU Interface(1:normal, 2:SPI, 3: PCIe): 1
          nic support: 1
          port count: 6
          macId: 8,16,20,24,25,28,
          CpuMacId: 28  (attr)
          Ether   cnt: 5, macId(m/M): 8/25 msk:0x03110100 0x00000000 (A)
          Uplink  cnt: 2, macId(m/M):24/25 msk:0x03000000 0x00000000 (A)
          XGE     cnt: 5, macId(m/M): 8/25 msk:0x03110100 0x00000000 (E)
          Copper  cnt: 5, macId(m/M): 8/25 msk:0x03110100 0x00000000 (M)
          port: 8, phyIdx0
          port:16, phyIdx1
          port:20, phyIdx1
          port:24, phyIdx2
          port:25, phyIdx2
          port:28, phyIdx255

          PHY Count:3
            type:19(CUST1       ) port:1 baseMac:8
            type:19(CUST1       ) port:2 baseMac:16
            type:19(CUST1       ) port:2 baseMac:24
          PHY[0]: chipID 19, baseMacId  8, phy_max  1
          PHY[1]: chipID 19, baseMacId 16, phy_max  2
          PHY[2]: chipID 19, baseMacId 24, phy_max  2
unitMapStruct[0].pUnitInfo:8eeb4014,parsed_info=8eeb4000,swDescp=c0090c24
unitMapStruct[1].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[2].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[3].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[4].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[5].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[6].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[7].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[8].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[9].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[10].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[11].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[12].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[13].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[14].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
unitMapStruct[15].pUnitInfo:c009e50c,parsed_info=0,swDescp=0
(&parsedInfoEmpty.unitInfo[EMPTY]=c009e50c)
info->hwp=RTL9303_2x84892_1x84891(c0090bd8)
info->hwp_localUnitCnt=1
info->hwp_embeddedCpuUnitId=0
info->hwp_cascade_mode=0
info->hwp_cascadeSlaveUnitID=0
info->hwp->swDescp[0]=c0090c24
info->hwp->swDescp[1]=0
info->hwp->swDescp[2]=0
info->unitInfo[0].hwp_chip_id=93030000
info->unitInfo[0].hwp_chip_revision=1
info->unitInfo[0].hwp_chip_family_id=93000000
info->unitInfo[0].hwp_maxMacId=28
info->unitInfo[0].hwp_minMacId=8
info->unitInfo[0].hwp_macID2PortDescp:
p[0]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[1]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[2]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[3]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[4]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[5]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[6]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[7]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[8]=c0090c38,mac_id=8,phyIdx=0,sdsIdx=0,smi=0,phy_addr=4,attr=1,eth=8,medi=1,
p[9]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[10]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[11]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[12]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[13]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[14]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[15]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[16]=c0090c48,mac_id=16,phyIdx=1,sdsIdx=1,smi=0,phy_addr=0,attr=1,eth=8,medi=1,
p[17]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[18]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[19]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[20]=c0090c58,mac_id=20,phyIdx=1,sdsIdx=2,smi=0,phy_addr=1,attr=1,eth=8,medi=1,
p[21]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[22]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[23]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[24]=c0090c68,mac_id=24,phyIdx=2,sdsIdx=3,smi=0,phy_addr=2,attr=3,eth=8,medi=1,
p[25]=c0090c78,mac_id=25,phyIdx=2,sdsIdx=4,smi=0,phy_addr=3,attr=3,eth=8,medi=1,
p[26]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[27]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[28]=c0090c88,mac_id=28,phyIdx=255,sdsIdx=255,smi=255,phy_addr=255,attr=8,eth=255,medi=255,
p[29]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[30]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[31]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[32]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[33]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[34]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[35]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[36]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[37]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[38]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[39]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[40]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[41]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[42]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[43]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[44]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[45]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[46]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[47]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[48]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[49]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[50]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[51]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[52]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[53]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[54]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[55]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[56]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[57]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[58]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[59]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[60]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[61]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[62]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,
p[63]=c00a0afc,mac_id=0,phyIdx=0,sdsIdx=0,smi=0,phy_addr=0,attr=0,eth=0,medi=0,

info->unitInfo[0].hwp_macID2SerdesID:
  p[0]=255,p[1]=255,p[2]=255,p[3]=255,p[4]=255,p[5]=255,p[6]=255,p[7]=255,p[8]=3,p[9]=255,p[10]=255,p[11]=255,p[12]=255,p[13]=255,p[14]=255,p[15]=255,p[16]=4,p[17]=255,p[18]=255,p[19]=255,p[20]=5,p[21]=255,p[22]=255,p[23]=255,p[24]=6,p[25]=7,p[26]=255,p[27]=255,p[28]=255,p[29]=255,p[30]=255,p[31]=255,p[32]=255,p[33]=255,p[34]=255,p[35]=255,p[36]=255,p[37]=255,p[38]=255,p[39]=255,p[40]=255,p[41]=255,p[42]=255,p[43]=255,p[44]=255,p[45]=255,p[46]=255,p[47]=255,p[48]=255,p[49]=255,p[50]=255,p[51]=255,p[52]=255,p[53]=255,p[54]=255,p[55]=255,p[56]=255,p[57]=255,p[58]=255,p[59]=255,p[60]=255,p[61]=255,p[62]=255,p[63]=255,
info->unitInfo[0].hwp_portCpuMacId=28
Ether  : count=5, max=25, min=8
Uplink : count=2, max=25, min=24
Cascade: count=0, max=0, min=64
Fe     : count=0, max=0, min=64
Ge     : count=0, max=0, min=64
Xge    : count=5, max=25, min=8
SXge   : count=0, max=0, min=64
Copper : count=5, max=25, min=8
Fiber  : count=0, max=0, min=64
Combo  : count=0, max=0, min=64
Serdes : count=0, max=0, min=64
info->unitInfo[0].hwp_sdsID2phyType:
  SDS  3 PHY:19
SDS  4 PHY:19
SDS  5 PHY:19
SDS  6 PHY:19
SDS  7 PHY:19
info->unitInfo[0].hwp_sdsID2MacID:
  s[3]=8,s[4]=16,s[5]=20,s[6]=24,s[7]=25,
info->unitInfo[0].hwp_attriPortMask:
  attr[0]=3110100
attr[0]=0
attr[1]=3000000
attr[1]=0
attr[2]=0
attr[2]=0
attr[3]=10000000
attr[3]=0
attr[4]=0
attr[4]=0

info->unitInfo[0].hwp_ethTypePortMask:
  eth[0]=0
eth[0]=0
eth[1]=0
eth[1]=0
eth[2]=0
eth[2]=0
eth[3]=3110100
eth[3]=0
eth[4]=0
eth[4]=0

info->unitInfo[0].hwp_mediumPortMask:
  med[0]=3110100
med[0]=0
med[1]=0
med[1]=0
med[2]=0
med[2]=0
med[3]=0
med[3]=0

info->unitInfo[0].hwp_allPortMask=13110100

info->unitInfo[0].hwp_allPortMask=0
info->unitInfo[0].hwp_macID2phyAddr:
  p[0]=255,p[1]=255,p[2]=255,p[3]=255,p[4]=255,p[5]=255,p[6]=255,p[7]=255,p[8]=4,p[9]=255,p[10]=255,p[11]=255,p[12]=255,p[13]=255,p[14]=255,p[15]=255,p[16]=0,p[17]=255,p[18]=255,p[19]=255,p[20]=1,p[21]=255,p[22]=255,p[23]=255,p[24]=2,p[25]=3,p[26]=255,p[27]=255,p[28]=255,p[29]=255,p[30]=255,p[31]=255,p[32]=255,p[33]=255,p[34]=255,p[35]=255,p[36]=255,p[37]=255,p[38]=255,p[39]=255,p[40]=255,p[41]=255,p[42]=255,p[43]=255,p[44]=255,p[45]=255,p[46]=255,p[47]=255,p[48]=255,p[49]=255,p[50]=255,p[51]=255,p[52]=255,p[53]=255,p[54]=255,p[55]=255,p[56]=255,p[57]=255,p[58]=255,p[59]=255,p[60]=255,p[61]=255,p[62]=255,p[63]=255,
info->unitInfo[0].hwp_macID2phyType:
  p[0]=26,p[1]=26,p[2]=26,p[3]=26,p[4]=26,p[5]=26,p[6]=26,p[7]=26,p[8]=19,p[9]=26,p[10]=26,p[11]=26,p[12]=26,p[13]=26,p[14]=26,p[15]=26,p[16]=19,p[17]=26,p[18]=26,p[19]=26,p[20]=19,p[21]=26,p[22]=26,p[23]=26,p[24]=19,p[25]=19,p[26]=26,p[27]=26,p[28]=18,p[29]=26,p[30]=26,p[31]=26,p[32]=26,p[33]=26,p[34]=26,p[35]=26,p[36]=26,p[37]=26,p[38]=26,p[39]=26,p[40]=26,p[41]=26,p[42]=26,p[43]=26,p[44]=26,p[45]=26,p[46]=26,p[47]=26,p[48]=26,p[49]=26,p[50]=26,p[51]=26,p[52]=26,p[53]=26,p[54]=26,p[55]=26,p[56]=26,p[57]=26,p[58]=26,p[59]=26,p[60]=26,p[61]=26,p[62]=26,p[63]=26,
info->unitInfo[0].hwp_sdsID2SerdesDescp:
  sds[0]=c00a0af8,sds[1]=c00a0af8,sds[2]=c00a0af8,sds[3]=c0091039,sds[4]=c009103b,sds[5]=c009103d,sds[6]=c009103f,sds[7]=c0091041,sds[8]=c00a0af8,sds[9]=c00a0af8,sds[10]=c00a0af8,sds[11]=c00a0af8,sds[12]=c00a0af8,sds[13]=c00a0af8,sds[14]=c00a0af8,sds[15]=c00a0af8,sds[16]=c00a0af8,sds[17]=c00a0af8,sds[18]=c00a0af8,sds[19]=c00a0af8,sds[20]=c00a0af8,sds[21]=c00a0af8,sds[22]=c00a0af8,sds[23]=c00a0af8,
info->unitInfo[0].hwp_phyBaseMacID:
  p[0]=255,p[1]=255,p[2]=255,p[3]=255,p[4]=255,p[5]=255,p[6]=255,p[7]=255,p[8]=8,p[9]=255,p[10]=255,p[11]=255,p[12]=255,p[13]=255,p[14]=255,p[15]=255,p[16]=16,p[17]=255,p[18]=255,p[19]=255,p[20]=16,p[21]=255,p[22]=255,p[23]=255,p[24]=24,p[25]=24,p[26]=255,p[27]=255,p[28]=28,p[29]=255,p[30]=255,p[31]=255,p[32]=255,p[33]=255,p[34]=255,p[35]=255,p[36]=255,p[37]=255,p[38]=255,p[39]=255,p[40]=255,p[41]=255,p[42]=255,p[43]=255,p[44]=255,p[45]=255,p[46]=255,p[47]=255,p[48]=255,p[49]=255,p[50]=255,p[51]=255,p[52]=255,p[53]=255,p[54]=255,p[55]=255,p[56]=255,p[57]=255,p[58]=255,p[59]=255,p[60]=255,p[61]=255,p[62]=255,p[63]=255,
info->unitInfo[0].hwp_ledNum:
  p[0]=0,p[1]=0,p[2]=0,p[3]=0,p[4]=0,p[5]=0,p[6]=0,p[7]=0,p[8]=4,p[9]=0,p[10]=0,p[11]=0,p[12]=0,p[13]=0,p[14]=0,p[15]=0,p[16]=4,p[17]=0,p[18]=0,p[19]=0,p[20]=4,p[21]=0,p[22]=0,p[23]=0,p[24]=4,p[25]=4,p[26]=0,p[27]=0,p[28]=255,p[29]=0,p[30]=0,p[31]=0,p[32]=0,p[33]=0,p[34]=0,p[35]=0,p[36]=0,p[37]=0,p[38]=0,p[39]=0,p[40]=0,p[41]=0,p[42]=0,p[43]=0,p[44]=0,p[45]=0,p[46]=0,p[47]=0,p[48]=0,p[49]=0,p[50]=0,p[51]=0,p[52]=0,p[53]=0,p[54]=0,p[55]=0,p[56]=0,p[57]=0,p[58]=0,p[59]=0,p[60]=0,p[61]=0,p[62]=0,p[63]=0,
info->unitInfo[0].hwp_multiSdsPortSdsmask:

info->unitInfo[0].hwp_multiSdsBaseSds:

info->unitInfo[0].hwp_macID2SCDescp:

info->unitInfo[0].hwp_scBaseMacID:

info->unitInfo[0].swDescp=c0090c24
info->unitInfo[0].parsed_info=8eeb4000
```
```
RTK.0> sys-config
set              - set configuration
get              - get configuration

RTK.0> sys-config get
serialnumber     - serialnumber configuration
stop-ip          - stop ip configuration

RTK.0> sys-config get serialnumber
get serial number fail

RTK.0> sys-config get stop-ip
stop ip :1
```
```
RTK.0> gpio
set              - set configuration
get              - get configuration

RTK.0> gpio get
dev              - GPIO device configuration

RTK.0> gpio get dev
<UINT:dev_id>    - GPIO device id

RTK.0> gpio get dev 0
pin              - GPIO pin configuration

RTK.0> gpio get dev 0 pin
<UINT:gpio_id>   - GPIO pin id <0-36>

RTK.0> gpio get dev 0 pin 0
GPIO data = 1

RTK.0> gpio get dev 0 pin 1
GPIO data = 1

RTK.0> gpio get dev 0 pin 2
GPIO data = 0

RTK.0> gpio get dev 0 pin 3
GPIO data = 1

RTK.0> gpio get dev 0 pin 4
GPIO data = 1

RTK.0> gpio get dev 0 pin 5
GPIO data = 1

RTK.0> gpio get dev 0 pin 6
GPIO data = 1

RTK.0> gpio get dev 0 pin 7
GPIO data = 0

RTK.0> gpio get dev 0 pin 8
GPIO data = 0

RTK.0> gpio get dev 0 pin 9
GPIO data = 0

RTK.0> gpio get dev 0 pin 10
GPIO data = 1

RTK.0> gpio get dev 0 pin 11
GPIO data = 1

RTK.0> gpio get dev 0 pin 12
GPIO data = 1

RTK.0> gpio get dev 0 pin 13
GPIO data = 1

RTK.0> gpio get dev 0 pin 14
GPIO data = 1

RTK.0> gpio get dev 0 pin 15
GPIO data = 1

RTK.0> gpio get dev 0 pin 16
GPIO data = 1

RTK.0> gpio get dev 0 pin 17
GPIO data = 1

RTK.0> gpio get dev 0 pin 18
GPIO data = 1

RTK.0> gpio get dev 0 pin 19
GPIO data = 1

RTK.0> gpio get dev 0 pin 20
GPIO data = 0

RTK.0> gpio get dev 0 pin 21
GPIO data = 1

RTK.0> gpio get dev 0 pin 22
GPIO data = 0

RTK.0> gpio get dev 0 pin 23
GPIO data = 0

RTK.0> gpio get dev 0 pin 24

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 25

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 26

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 27

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 28

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 29

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 30

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 31

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 32

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 33

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 34

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 35

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2


RTK.0> gpio get dev 0 pin 35

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2

RTK.0> gpio get dev 0 pin 36

Get drv_generalCtrlGPIO_dataBit_get() ERROR = 61452
GPIO data = 2
```