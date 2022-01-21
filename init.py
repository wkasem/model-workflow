import subprocess
import os
import sys

STORAGE_DIR = sys.argv[1]


os.environ['WORKSPACE_DIR'] = STORAGE_DIR + '/workspace/'
os.environ['MODEL_DIR'] = STORAGE_DIR + '/model/'
os.environ['DEEPFACE_DIR'] = STORAGE_DIR + '/DeepFaceLab/'


cmd1 = "pip install -r " + \
    os.environ['DEEPFACE_DIR'] + "requirements-colab.txt"
cmd2 = "pip install --upgrade scikit-image"
cmd3 = "apt-get install cuda-10-0"

subprocess.run([cmd1, cmd2])
