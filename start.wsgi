import os, sys

PROJECT_DIR = '/groups/AccidentVisualizations/flaskapp'

activate_this = '/groups/AccidentVisualizations/flaskapp/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.append(PROJECT_DIR)

from flaskapp import app as application
