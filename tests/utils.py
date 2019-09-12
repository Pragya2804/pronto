import contextlib
import importlib
import os
import sys


# Resources
TESTDIR = os.path.dirname(os.path.abspath(__file__))
MAINDIR = os.path.dirname(TESTDIR)
DOCSDIR = os.path.join(MAINDIR, "docs")
DATADIR = os.path.join(TESTDIR, "resources")
RUNDIR = os.path.join(TESTDIR, "run")


# Shortcut to try import modules/functions
def try_import(*paths):
    for path in paths:
        if path is None:
            return None      
        with contextlib.suppress(ImportError, AttributeError):
            if ":" in path:
                modname, attrname = path.rsplit(":", 1)
                return getattr(importlib.import_module(modname), attrname)
            else:
                return importlib.import_module(path)
    raise ImportError(f"could not find any of the following: {', '.join(paths)}")

mock = try_import("unittest.mock", "mock")


# Force importing the local version of the module
sys.path.insert(0, MAINDIR)

# Launch a stub HTTP server to server local files
from .stubs import StubHTTPServer
StubHTTPServer(DATADIR).start()
