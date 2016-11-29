""" Configuration variables. """

import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

FB_APP_ID = os.environ.get("FB_APP_ID")
FB_APP_NAME = os.environ.get("FB_APP_NAME")
FB_APP_SECRET = os.environ.get("FB_APP_SECRET")
FFS_GROUP_ID = os.environ.get("FFS_GROUP_ID")
GOOG_API_KEY = os.environ.get("GOOG_API_KEY")

DESC_FMT_STRING = "(?P<item>.+)" + \
                  "\n" + \
                  "(?P<price>\S+)" + \
                  " - " + \
                  "(?:<<not-applicable>>|(?P<location>.+))" + \
                  "(?:\n\n)*" + \
                  "(?P<description>[\s\S]*)"
