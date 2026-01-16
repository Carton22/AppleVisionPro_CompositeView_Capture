import argparse
import os
import threading
import time

import Quartz
import socketio

# Keycodes (macOS)
VK_SPACE = 49


def send_key(vk: int, delay: float = 0.05) -> None:
    ev_down = Quartz.CGEventCreateKeyboardEvent(None, vk, True)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, ev_down)
    time.sleep(delay)
    ev_up = Quartz.CGEventCreateKeyboardEvent(None, vk, False)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, ev_up)


sio = socketio.Client(reconnection=True)
_lock = threading.Lock()
_in_flight = False


@sio.event
def connect():
    print("Socket.IO connected. Waiting for 'spacebar_click'...")


@sio.event
def disconnect():
    print("Socket.IO disconnected.")


@sio.on("spacebar_click")
def on_spacebar_click(data=None):
    global _in_flight
    with _lock:
        if _in_flight:
            return
        _in_flight = True

    def worker():
        global _in_flight
        try:
            print("Received 'spacebar_click'. Waiting 3 seconds...")
            time.sleep(3)
            send_key(VK_SPACE)
            print("Sent SPACE.")
        finally:
            with _lock:
                _in_flight = False

    threading.Thread(target=worker, daemon=True).start()


def main() -> int:
    parser = argparse.ArgumentParser(description="Trigger macOS SPACE keypress on Socket.IO event.")
    parser.add_argument(
        "--url",
        default=os.environ.get("SOCKETIO_URL", "http://localhost:5000"),
        help="Socket.IO server URL (env: SOCKETIO_URL). Default: http://localhost:5000",
    )
    args = parser.parse_args()

    try:
        sio.connect(args.url)
        sio.wait()  # blocks forever
    except KeyboardInterrupt:
        pass
    finally:
        try:
            sio.disconnect()
        except Exception:
            pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())