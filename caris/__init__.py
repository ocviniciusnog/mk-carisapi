"""
example_pkg: A sample Python package demonstrating package structure.

This package contains two modules, module1 and module2, which provide
various functionalities for demonstration purposes.

@Author: Vinicius Rezende Nogueira
@Email: contato@viniciusnogueira.com
@Version: 1.0.0
"""

__author__ = "Vinicius Rezende Nogueira"
__version__ = "1.0.0"
__email__ = "contato@viniciusnogueira.com"
__license__ = "MIT"

from . import carisbatch
from . import utils

__all__ = ["carisbatch", "utils.py"]