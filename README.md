# AP4ETS2
Real time adapting auto pilot for Euro Truck Simulator 2.

# Jayesk's Screenshotter
Jayesk's Screenshotter is my publicly avaliable software for collecting data to train my AI models on. It has various options, most of which do not function at the moment.

# Setup Instructions
1. Download the Screenshotter from [here.](https://github.com/Jayesk/AP4ETS2/releases/download/v0.1/Jayesk.s.Screenshotter.-.ETS2.Data.Collection.zip)
2. Extract the .zip file into a folder.
3. If not already there, create a folder called 'captured'.
4. Open 'install_requirements.bat' and wait for the required plugins to be installed.
5. Once this is done, edit the 'start.bat' file so you replace the existing Python.exe directory with yours, it should look something like this:
`C:\Users\Joel\AppData\Local\Programs\Python\Python310\python.exe screenshotter.py`
6. Now, opening 'start.bat' should open the Screenshotter program, if it didn't work, please create an issue on this page and I will help you to resolve it.
7. If you open ETS2 and click 'Start Recording' the program should start to take screenshots and put them all in \captured\. 
8. You now have it working, for more details on individual components, look below.

## To be added/fixed
- Screenshot Preview Size.
- Presets for most trucks in the game.
- More intuitive settings menu/UI.
- Fixes for broken elements.
- Keybinds.

## Features and Settings

### Start/Stop Recording
Buttons to start and stop the software taking screenshots.

### Screenshots taken
Counts your overall amount of screenshots taken.

### Screenshot Preview
Under the Screenshots Taken label, you can preview your screenshots in real-time.

### Screenshot Area
Input what area you want to screenshot. By default it is set to be used on the Scania S, with no accessories blocking the view and the steering wheel lowered or hidden.

### Screenshot Frequency 
Input how frequent you want screenshots to be taken, can be a decimal, it is suggested you put it to 1 second. By default it is set to take a screenshot every 0.5 seconds.

### ETS2 Check
By clicking on this button, you can spoof that 'Euro Truck Simulator 2' is open, allowing it to be used outside of the game. Note: The extra window it opens has to stay open for the duration you want to use it out of ETS2.

### Coords Finder
Works if you know how to use it, it should really be under Troubleshooting.

### Presets
Not currently working, presets will be added soon, the pop-up proclaiming the Scania S preset has been loaded was purely for testing.

### Screenshot Counter
Currently not working. Will be used to set the Screenshots Taken counter manually and to troubleshoot potential errors.

