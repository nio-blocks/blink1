Blink1
======
Control a [blink(1) dongle](http://blink1.thingm.com/).

Installation Notes:
--------------------
- **Linux**: In modern Linux kernels, you can enable `CONFIG_HID_THINGM` or `CONFIG_HID_LEDS` to enable blink1 support in the kernel. Some kernels, such as Raspbian for the Raspberry Pi has this enabled by default so no additional installation steps are necessary.
- **Mac and Windows**: Upgrade to the newest blink1 version: `pip3 install -U blink1`.

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
