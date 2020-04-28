import os
import sys
import sys

# insert the parent directory of the current module into the search path
# we assume that this parent directory contains the source package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import black_scholes