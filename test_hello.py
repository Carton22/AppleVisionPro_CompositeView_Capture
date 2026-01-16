import time
import Quartz

# keycodes
VK_H = 4
VK_E = 14
VK_L = 37
VK_O = 31
VK_RETURN = 36

def press(vk, gap=0.01):
    down = Quartz.CGEventCreateKeyboardEvent(None, vk, True)
    up   = Quartz.CGEventCreateKeyboardEvent(None, vk, False)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, down)
    time.sleep(gap)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, up)

print("Switch focus to a text field/Terminal NOW... typing in 2 seconds")
time.sleep(2)

for k in [VK_H, VK_E, VK_L, VK_L, VK_O]:
    press(k)

press(VK_RETURN)
print("Done")