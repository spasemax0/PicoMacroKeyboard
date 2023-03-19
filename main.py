//Author: Spase Sandoval
//Date: 3/18/23
//Circuitpython basic macro keyboard with LED functionality, add or remove buttons, and change "board.GPXX" and keycodes/controlcodes as needed.

import time
import digitalio
import board
import usb_hid
from digitalio import DigitalInOut, Direction
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from digitalio import Pull

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = False

btn1_pin = board.GP15
btn2_pin = board.GP14
btn3_pin = board.GP13
btn4_pin = board.GP12
keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

while True:
    if btn1.value:
        keyboard.press(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.KEYPAD_ASTERISK)
        keyboard.release(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.KEYPAD_ASTERISK)
        led.switch_to_output(True)
        time.sleep(0.1)
        led.switch_to_output(False)
    
    if btn2.value:
        keyboard.press(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.DELETE)
        keyboard.release(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.DELETE)
        led.switch_to_output(True)
        time.sleep(0.1)
        led.switch_to_output(False)
        
    
    if btn3.value:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        led.switch_to_output(True)
        time.sleep(0.1)
        led.switch_to_output(False)
        
    
    if btn4.value:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        led.switch_to_output(True)
        time.sleep(0.1)
        led.switch_to_output(False)
