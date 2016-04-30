import sys

_exportpath = '/sys/class/gpio/gpiochip0/subsystem/export'
_unexportpath = '/sys/class/gpio/gpiochip0/subsystem/unexport'
_gpiopath = '/sys/class/gpio/gpio'

print sys.argv[1]