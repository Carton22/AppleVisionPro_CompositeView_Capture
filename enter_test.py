import time
import Quartz
import CoreFoundation

# Keycodes (macOS)
VK_A = 0x00
VK_SPACE = 49  # 49

def send_key(vk, delay=0.05):
    ev_down = Quartz.CGEventCreateKeyboardEvent(None, vk, True)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, ev_down)
    time.sleep(delay)
    ev_up = Quartz.CGEventCreateKeyboardEvent(None, vk, False)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, ev_up)

triggered = False
tap = None

def on_event(proxy, type_, event, refcon):
    global triggered, tap
    if type_ == Quartz.kCGEventKeyDown and not triggered:
        keycode = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeycode)
        if keycode == VK_A:
            triggered = True
            # Stop listening after the first "A"
            Quartz.CGEventTapEnable(tap, False)
            CoreFoundation.CFRunLoopStop(CoreFoundation.CFRunLoopGetCurrent())
    return event

print("Press 'A' to trigger...")

mask = Quartz.CGEventMaskBit(Quartz.kCGEventKeyDown)
tap = Quartz.CGEventTapCreate(
    Quartz.kCGSessionEventTap,
    Quartz.kCGHeadInsertEventTap,
    Quartz.kCGEventTapOptionDefault,
    mask,
    on_event,
    None,
)

if tap is None:
    raise RuntimeError(
        "Failed to create event tap. Grant Accessibility permission to your Terminal/Python, then retry."
    )

source = Quartz.CFMachPortCreateRunLoopSource(None, tap, 0)
CoreFoundation.CFRunLoopAddSource(
    CoreFoundation.CFRunLoopGetCurrent(),
    source,
    CoreFoundation.kCFRunLoopCommonModes,
)
Quartz.CGEventTapEnable(tap, True)

CoreFoundation.CFRunLoopRun()  # blocks until 'A' is detected

print("Detected 'A'. Waiting 3 seconds...")
time.sleep(3)

# Do others here (add more send_key(...) calls if you want)
send_key(VK_SPACE)

print("Done.")