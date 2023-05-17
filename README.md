# Trendnet TEG-S750
This 5 Port 10G switch supports nbase-t 802.3bz and has a maximum power consumption of 12W.
- SOC: RTL9303
- RAM: 256MB,  Nanya NT5CC128M16JR-EK
- Flash: 16MB, Macronix MX25L12833F 3.3V
- UART pin order: VCC (square), RX, GND, TX

Getting a shell
```
pyserial-miniterm --eol LF /dev/cu.usbserial-* 115200
```

Flash and run OpenWrt:
```
pip install pyserial xmodem
python3 ymodem.py /dev/cu.usbserial-* openwrt-realtek-rtl930x-zyxel_xgs1250-12-initramfs-kernel.bin
```

## Links
- https://openwrt.org/docs/guide-developer/add.new.device
- https://openwrt.org/docs/guide-developer/adding_new_device#collecting_relevant_data
- https://forum.openwrt.org/t/support-for-rtl838x-based-managed-switches/57875
- https://forum.openwrt.org/t/u-boot-for-xgs12xx-switches-and-others-based-on-realtek-rtl930x/134478
- https://svanheule.net/switches
- https://openwrt.org/docs/techref/flash.layout
