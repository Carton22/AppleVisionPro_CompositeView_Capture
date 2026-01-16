# Apple Vision Pro Composite View Capture 

Using a programmatic way to capture composite views in Apple Vision Pro is almost impossible, 

ReplayKit
Need to configure the Enterprise License and install package
Or even interface between Unity and SwiftUI

All the above issues cause me big headaches.

## Features

    - using a programmatic way to trigger composite view screenshot capture/screen recording
    - do not require Apple Vision Pro Enterprise license
    - no Unity or its package and plugin
    - no Xcode or Swift UIonly macbook / realiy composer pro / apple vision pro needed + my little magic script
    - can be interfaced with WebSockets later to allow for XR headset control and cross-device control

The code for space in MacOS is 49.

## Socket.IO-triggered SPACE keypress (macOS)

`socket_spacebar_trigger.py` runs a **Socket.IO client** and listens for a `spacebar_click` event. When received, it **waits 3 seconds** and then sends an **OS-level SPACE keypress** (requires Accessibility permission for your Terminal/Python).

### Install

```bash
python3 -m pip install -r requirements.txt
```

### Run

```bash
python3 socket_spacebar_trigger.py --url http://localhost:5000
```

You can also set `SOCKETIO_URL` instead of passing `--url`.