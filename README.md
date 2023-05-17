# Trendnet TEG-S750
This 5 Port 10G switch supports IEEE 802.3bz NBASE-t and has a maximum power consumption of 12W.
- SOC: RTL9303
- RAM: 256MB,  Nanya NT5CC128M16JR-EK
- Flash: 16MB, Macronix MX25L12833F 3.3V
- UART pin order: VCC (square), RX, GND, TX

Getting a shell
```
pyserial-miniterm --eol LF --raw /dev/cu.usbserial-* 115200
```

Flash and run OpenWrt:
```
pip install pyserial xmodem
python3 ymodem.py /dev/cu.usbserial-* openwrt-realtek-rtl930x-zyxel_xgs1250-12-initramfs-kernel.bin
```

## GPIO
- 489 = system (green)
- 490 = system (orange)
- 491 = port 2 act (green, active low)
- 492 = port 3 act (green, active low)
- 493 = port 4 act (green, active low)
- 494 = port 5 act (green, active low)
- 495 = port 1 act (green, active low)

Script:
```
#!/bin/sh
GPIOCHIP=488
BASE=$(cat /sys/class/gpio/gpiochip${GPIOCHIP}/base)
NGPIO=$(cat /sys/class/gpio/gpiochip${GPIOCHIP}/ngpio)
max=$(($BASE+$NGPIO))
gpio=$BASE
while [ $gpio -lt $max ] ; do
	echo $gpio > /sys/class/gpio/export
	[ -d /sys/class/gpio/gpio${gpio} ] && {
		echo out > /sys/class/gpio/gpio$gpio/direction

		echo "[GPIO$gpio] Trying value 0"
		echo 0 > /sys/class/gpio/gpio$gpio/value

		while read -n1 c; do
			if [[ $c == "t" ]]; then
				oldVal=$(cat /sys/class/gpio/gpio$gpio/value)
				newVal=$((oldVal ^= 1))
				echo "[GPIO$gpio] Trying value $newVal"
				echo $newVal > /sys/class/gpio/gpio$gpio/value
			else
				break
			fi
		done
 
		echo $gpio > /sys/class/gpio/unexport
	}
	gpio=$((gpio+1))
done
```

## Links
- https://openwrt.org/docs/guide-developer/add.new.device
- https://openwrt.org/docs/guide-developer/adding_new_device#collecting_relevant_data
- https://openwrt.org/docs/techref/flash.layout
- https://forum.openwrt.org/t/support-for-rtl838x-based-managed-switches/57875/2470
- https://forum.openwrt.org/t/u-boot-for-xgs12xx-switches-and-others-based-on-realtek-rtl930x/134478
- https://svanheule.net/switches
- https://svanheule.net/realtek
