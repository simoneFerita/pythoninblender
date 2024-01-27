import subprocess
import ensurepip
import sys
ensurepip.bootstrap() 
pybin = sys.executable
subprocess.check_call([pybin, '-m', 'pip', 'install', 'pandas'])
subprocess.check_call([pybin, '-m', 'pip', 'install', 'openpyxl']) 
