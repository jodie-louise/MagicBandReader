# Magic band reader project!

This is a project imitate the magic band reader at Disney World!


## Setting up with remote connection to a Raspberry Pi.
1. To aid in development, we're remoting to the pi using [VS Code ](https://code.visualstudio.com/)  the [Remote Development Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack), and the [Remote-SSH Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) Install these.
2. Open the command pallete (cmd+shift+p or ctrl+shift+p) and run the `Remote-SSH: Connect to Host...` command (you can find this by searching for "_Remote SSH_").
3. Enter (or select via the drop down menu) the address of the Pi, ie `ssh pi@123.456.789`. [Read the docs for Remote-SSH for more info here](https://code.visualstudio.com/docs/remote/ssh).
4. Connect to the pi and enter the password. Wait a few minuets while it is configured.
5. In the file explorer (file icon top left of VScode) open the `MagicBandReader` folder.
6. A new window should appear with the files in your edior. 🎉
7. HINT: you can open a terminal window with CMD+J or CTL+J.

## Running the project

### Hardware

For GPIO Header labels, refer to [this handy diagram](https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/).

![GPIO Diagram](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/raspberry_pi_3_model_b_plus_gpio.jpg)

**Lights**

See diagram below
![Raspberry Pi light setup GPIO diagram](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-WS2812-Steckplatine-600x361.png)
1. Connect lights Ground and power wire to a 5v power supply.
2. Connect the ground pin to Pin 14 (ground on pi) and data in to pin 12 (GPIO 18).

**RFID Reader**
1. `TODO DOCUMENT THIS`

### Software
1. `TODO: add deps to requirements.txt` Install dependancies (If runnig on Pi they _should_ be there already!).
2. Run the Magic band reader with `sudo python3 MagicBandReader.py`
3. Tap a valid magic band (thats ID matches one in MagicBandIds.py) to the reader.
4. It should work! 🐭🏰