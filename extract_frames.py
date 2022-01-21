import subprocess
import os
import sys
Video = sys.argv[0]


workspace = os.getenv('workspace_DIR', "")

cmd = workspace + "main.py videoed extract-video"

if Video == "data_dst":
    cmd += " --input-file " + workspace + \
        "/data_dst.* --output-dir " + workspace + "/data_dst/"
else:
    cmd += " --input-file " + workspace + \
        "/data_src.* --output-dir " + workspace + "/data_src/"

subprocess.run("ls")
