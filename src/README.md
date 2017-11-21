# Usage Instructions
This folder contains all the python and shell scripts to train or test the Gesture Detector

## Testing
To test the Detector, simply run the test.py script. This scripts accepts an optional argument which is the filename of a test video. 
If the optional parameter is empty then the camera will be used as the capture device. Use _test1.flv_ or _test2.flv_ or _test3.flv_ and so on, test the Detector.

## Training
Training is a little more involved. To begin make sure you have the training precursor images.
1. Run the setup script (make sure the scripts are set as executables) or create three folders called pos, neg, info and data.
2. If you do not have positive precursors then use run hand_roi.py to collect images.
3. Copy your images to the pos folder. If you ran hand_roi then the images will be auto-saved in the pos folder.
4. Run the master script which takes care of negative image downloads, setting up training samples and training. You can open up the script to change the parameters as needed.
5. If the sample creator shell script (called through master) crashes, run the failed command manually.
6. The trained cascade would be available in the data folder. Import that in test.py to use that detector.
**NOTE**: The positive precursor names are of type *pos-<number>_burned* inside the *pos_burned* folder. If you want to use your own images then please follow naming convention. See *sample_creator.py* for naming conventions and changes.
