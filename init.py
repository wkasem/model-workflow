import subprocess
import os
import sys

STORAGE_DIR = sys.argv[0]


os.environ['WORKSPACE_DIR'] = STORAGE_DIR + '/workspace/'
os.environ['MODEL_DIR'] = STORAGE_DIR + '/model/'
os.environ['DEEPFACE_DIR'] = STORAGE_DIR + '/DeepFaceLab/'


cmd = "sudo pip install -r " + \
    os.environ['DEEPFACE_DIR'] + "/requirements-colab.txt"
cmd += " && pip install --upgrade scikit-image"
cmd += " && sudo apt-get install cuda-10-0"

subprocess.run(cmd)
