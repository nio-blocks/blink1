Blink1
======
Control a [blink(1) dongle](http://blink1.thingm.com/).

Installation Notes:
--------------------
- **Linux**: In modern Linux kernels, you can enable `CONFIG_HID_THINGM` or `CONFIG_HID_LEDS` to enable blink1 support in the kernel. Some kernels, such as Raspbian for the Raspberry Pi has this enabled by default so no additional installation steps are necessary.
- **Mac OSX**: To use a blink1 with Mac OSX, upgrade to the newest blink1 version `pip3 install -U blink1`. 
- **Windows**: pyusb needs an additional backend to be installed, [download libusb from SourceForge](http://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/libusb-win32-bin-1.2.6.0.zip/download) and run the contained `inf-wizard.exe`. When prompted, select the connected blink1 from the list, save the file as requested, and click `Install Now`.

Properties
----------
- **color**: (colors= red|green|blue): RGB color to fade to, each component color brightness is an 8-bit value, so the values `0-255` are valid.
- **fade_milliseconds**: Time to fade to `color`.

Inputs
------
- **default**: Any list of signals, `color` and `fade_milliseconds` are evaluated for each signal.

Outputs
-------
None

Commands
--------
None

Dependencies
------------
-   [**blink1**](https://pypi.python.org/pypi/blink1/0.0.12)

Installation Notes:
-------------------
- **Linux**: In modern Linux kernels, you can enable `CONFIG_HID_THINGM` or `CONFIG_HID_LEDS` to enable blink1 support in the kernel. Some kernels, such as Raspbian for the Raspberry Pi has this enabled by default so no additional installation steps are necessary.
- **Mac OSX**: On some machines it may be that pyusb from pypi is not a recent enough version. If your block connects to the Blink1 device but is unable to fade the colors, try installing from [source](https://github.com/walac/pyusb). In addition to this, you can also try a [newer version](https://github.com/todbot/blink1) of blink1.
- **Windows**: pyusb needs an additional backend to be installed, [download libusb from SourceForge](http://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/libusb-win32-bin-1.2.6.0.zip/download) and run the contained `inf-wizard.exe`. When prompted, select the connected blink1 from the list, save the file as requested, and click `Install Now`.

