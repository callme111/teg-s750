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