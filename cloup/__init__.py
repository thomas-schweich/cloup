"""Top-level package for cloup."""
# WARNING: _version.py is generated by setuptools-scm upon package building/installation
from . import _version

__author__ = """Gianluca Gippetto"""
__email__ = 'gianluca.gippetto@gmail.com'
__version__ = _version.version
__version_tuple__ = _version.version_tuple

# flake8: noqa F401
from click import (
    # decorators
    confirmation_option,
    help_option,
    pass_context,
    pass_obj,
    password_option,
    version_option,
    # types
    BOOL,
    Choice,
    DateTime,
    File,
    FLOAT,
    FloatRange,
    INT,
    IntRange,
    ParamType,
    Path,
    STRING,
    Tuple,
    UNPROCESSED,
    UUID,
)

from . import warnings
from .styling import (
    HelpTheme,
    Style,
    Color,
)
from .formatting import (
    HelpFormatter,
    HelpSection,
)
from ._context import Context
from ._params import GroupedOption, argument, option
from ._option_groups import (
    OptionGroup,
    OptionGroupMixin,
    option_group,
)
from ._sections import (
    Section,
    SectionMixin,
)
from ._commands import (
    BaseCommand,
    Command,
    Group,
    command,
    group,
)
from .constraints import (
    ConstraintMixin,
    constraint,
    constrained_params,
)
