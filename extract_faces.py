import subprocess
import os


Detector = "S3FD"

workspace = os.getenv('WORKSPACE_DIR')
deepface = os.getenv('DEEPFACE_DIR')
detect_type = "s3fd"

folder_src = workspace + "data_src"
folder_dst = workspace + "data_dst"
folder_aligned_src = folder_src+"/aligned"
folder_aligned_dst = folder_dst+"/aligned"

cmd_src = deepface + "main.py extract --input-dir " + \
    folder_src+" --output-dir "+folder_aligned_src
cmd_src += " --detector "+detect_type+" --force-gpu-idxs 0"

cmd_dst = deepface + "main.py extract --input-dir " + \
    folder_dst+" --output-dir "+folder_aligned_dst
cmd_dst += " --detector "+detect_type+" --force-gpu-idxs 0"

subprocess.run([cmd_src, cmd_dst])
