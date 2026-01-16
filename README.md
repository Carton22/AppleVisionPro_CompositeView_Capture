# Apple Vision Pro Composite View Capture 

## Why do we need this?

Using a programmatic way to capture composite views in Apple Vision Pro (AVP) is almost impossible, 

Need to configure the Enterprise License and install package
Or even jump between between Unity and SwiftUI

Unity Main Camera Access provided by Enterprise APIs is able to capture both left and right camera view now -> you will be able to get stereo view.

However, by using this main camera access, you can only capture the **physical real world view** without the **overlaid AR digital elements**.

We differentiate between the passthrough physical view and the composite view, composite view will contain both the passthrough view and the digital visual elements.

To capture the composite view, you can only do
1. OS-level screen recording
2. ReplayKit

But using the above 2 ways will be hard to capture a single image, specifically at the start frame, when the user pinches their thumb and finger.

All the above issues cause me big headaches.

Using this method, the image and video will also be saved directly in your local Macbook, comparatively more friendly than saving in XR headset client app and then send the large image data to the model server.

By saving on the laptop, we can alsso easily do sanity check and quick visualization to guarantee the scene image is saved correctly.

## Workflow

1. In your Macbook, Grant Access in Sytem - Privacy - Accessability for your terminal or IDE (VSCode or Cursor)
2. Open Developer Capture Tools in Reality Composer Pro (More Infor [here](https://developer.apple.com/documentation/visionos/capturing-screenshots-and-video-from-your-apple-vision-pro-for-2d-viewing))
3. make sure your laptop is connected successfully with Apple Vision Pro
4. run the script `enter_test.py`
5. make sure the Develpor Capture Tool is the main current window or task in you Macbook, this can be done by clicking on the window of the developer tool.
6. click A manually (this can be replaced by websocket message control), after 3 seconds, the script will simulate a click event and click the space, and then the developer capture tool will capture the current composite view in AVP and save in `\Desktop` folder.
7. and then you can take this image for any processing



## Features

1. using a programmatic way to trigger composite view screenshot capture/screen recording
2. do not require Apple Vision Pro Enterprise license
3. no Unity or its package and plugin
4. no Xcode or Swift UIonly macbook / realiy composer pro / apple vision pro needed + my little magic script
5. can be interfaced with WebSockets later to allow for XR headset control and cross-device control

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

## Others

The code for space in MacOS is 49.