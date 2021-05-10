# -----------------------------------------------------------------------------
# CONFIG.PY
# -----------------------------------------------------------------------------
# The Flask application config file.
# -----------------------------------------------------------------------------

import os
import inspect

# -----------------------------------------------------------------------------
# DIRECTORIES
# -----------------------------------------------------------------------------
BASEDIR = os.path.abspath(inspect.stack()[-1][1])
BASEDIR = os.path.dirname(BASEDIR)


# -----------------------------------------------------------------------------
DEBUG = False
SECRET_KEY = '#SECRET-KEY#'
SESSION_TYPE = 'redis'
SESSION_LIFETIME = 36000

# -----------------------------------------------------------------------------
# SCRIPT
# -----------------------------------------------------------------------------
SCRIPT_PATH = os.path.abspath(os.path.join(BASEDIR, os.pardir)) + '/scripts/'

# -----------------------------------------------------------------------------
# STORAGE
# -----------------------------------------------------------------------------
DATA_PATH = 'app/storage/data.json'