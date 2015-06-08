Blink1
======

Control a blink(1) dongle. http://blink1.thingm.com/

Note: The blink1 python module has a dependency on pyusb. On some machines it may be that pyusb from pypi is not a recent enough version. If you the block connects the to the Blink1 device but is unable to fade the colors, try installing from source: https://github.com/walac/pyusb. In addition to this, you can also try a newer version of blink1: https://github.com/todbot/blink1. This todbot repo is the official repo fro thingm, yet it is not the one on pypi.

Properties
----------
-   **fade_milliseconds**: Time it takes to fade to new color.
-   **color (red, green, blue)** RGB color to fade to.


Dependencies
------------
-   **blink1**

Commands
--------
None

Input
-----
Any list of signals.

Output
------
None
