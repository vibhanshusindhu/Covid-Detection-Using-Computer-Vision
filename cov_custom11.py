# -*- coding: utf-8 -*-
"""cov_custom11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Wv1AdNmEccNEoRWsSHRBHmfZrm5xDm_

**Get the runtime details**
"""

# Commented out IPython magic to ensure Python compatibility.
# %cat/etc/lsb-release

"""**Update the repo list**"""

!apt-get update

"""**show the current working directory**"""

# Commented out IPython magic to ensure Python compatibility.
# %pwd

"""**Unzip the darknet zip file to the /content folder**"""

!unzip "/content/drive/My Drive/custom_cov_model/darknet.zip"

"""**Go inside the darknet folder of our runtime**"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/darknet

"""**Install dos2unix to convert dos files to unix encoding**"""

!sudo apt install dos2unix

"""**Convert all files in darknet folder to unix encoding**"""

!find . -type f -print0 | xargs -0 dos2unix

"""**Give executable permission for files in /content/darknet**"""

!chmod +x /content/darknet

"""**make sure of the current working directory**"""

# Commented out IPython magic to ensure Python compatibility.
# %pwd

"""**Compile the darknet framework**"""

!make

"""**Test the darknet framework with sample object detection**"""

!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights data/person.jpg

"""**Remove the backup folder of darknet in runtime**"""

!rm /content/darknet/backup -r

"""**Create a symbolic link from runtime darknet folder to google drive backup folder with the name 'backup'**"""

!ln -s /content/drive/'My Drive'/cov_weights/backup /content/darknet

"""**check the directory**"""

# Commented out IPython magic to ensure Python compatibility.
# %pwd

"""**Proceed with fresh training using the cov dataset**"""

!./darknet detector train cov_data/cov.data cov_yolov4.cfg yolov4.conv.137 -map -dont_show

"""**Resume training from the last best weight file if required**"""

#!./darknet detector train cov_data/cov.data cov_yolov4.cfg /content/drive/'My Drive'/cov_weights/backup/cov_yolov4_best.weights -map -dont_show