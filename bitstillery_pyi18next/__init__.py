"""
bitstillery_pyi18next - A Python implementation of i18next with pluralisation fixes.

This is a fork of pyi18next that fixes pluralisation count issues.
"""

__version__ = "0.0.3"
__author__ = "Gongziting Tech Ltd., Bitstillery"

from .i18next import I18next
from .translate import translate
from .functions import t

__all__ = ["I18next", "translate", "t"]
