import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_key=os.getenv("GEMINI_API_KEY","")
MODEL=os.getenv("GEMINI_MODEL","gemini_3.5-flash")

