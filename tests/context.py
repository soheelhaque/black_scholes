# this file allows tests to exist in a different directory to the code that is being tested
# without this, the source package will not be on the search path
# this assume that the parent directory contains the source package
import os
import sys
import sys

# insert the parent directory of the current module into the search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import black_scholes