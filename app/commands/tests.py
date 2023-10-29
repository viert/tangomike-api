import unittest
import logging
import inspect
import sys
from types import ModuleType
from croydon.command import Command

MODULE_NAME = "_all_tests"


class Test(Command):

    NAME = "test"
    HELP = "run application tests"
    ASYNC_RUN = False

    def run_sync(self):
        logging.disable(logging.CRITICAL)
        all_tests_module = ModuleType(MODULE_NAME)
        module = __import__("app.tests").tests

        for objname in dir(module):
            obj = getattr(module, objname)
            if (inspect.isclass(obj) and
                    issubclass(obj, unittest.TestCase) and
                    obj != unittest.TestCase):
                setattr(all_tests_module, objname, obj)

        sys.modules[MODULE_NAME] = all_tests_module
        unittest.main(argv=["crcmd.py test"], module=MODULE_NAME)
