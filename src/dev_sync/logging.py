import os
import logging

from typing import Optional
from enum import Enum

from rich.theme import Theme
from rich.style import Style

from rich.logging import RichHandler
from rich.console import Console
from rich.traceback import install

from rich import reconfigure

_rich_configured = False

class Color(Enum):
    RED = "rgb(215,0,0)"
    GREEN = "rgb(0,135,0)"
    BLUE = "rgb(0,105,255)"
    YELLOW = "rgb(215,175,0)"
    PURPLE = "rgb(225,0,225)"
    BRIGHT_RED = "rgb(255,0,0)"

TEXTUAL_RICH_THEME = Theme({
    "logging.level.info": Style(color=Color.BLUE.value, bold=True),
    "logging.level.debug": Style(color=Color.GREEN.value, bold=True),
    "logging.level.warning": Style(color=Color.YELLOW.value, bold=True),
    "logging.level.error": Style(color=Color.RED.value, bold=True),
    "logging.keyword": Style(color=Color.YELLOW.value, bold=True),
    "repr.attrib_name": Style(color=Color.YELLOW.value, italic=False),
    "repr.attrib_value": Style(color=Color.PURPLE.value, italic=False),
    "repr.bool_true": Style(color=Color.GREEN.value, italic=True),
    "repr.bool_false": Style(color=Color.RED.value, italic=True),
    "repr.call": Style(color=Color.PURPLE.value, bold=True),
    "repr.none": Style(color=Color.PURPLE.value, italic=True),
    "repr.str": Style(color=Color.GREEN.value),
    "repr.path": Style(color=Color.PURPLE.value),
    "repr.filename": Style(color=Color.PURPLE.value),
    "repr.url": Style(color=Color.BLUE.value, underline=True),
    "repr.tag_name": Style(color=Color.PURPLE.value, bold=True),
    "json.bool_true": Style(color=Color.GREEN.value, italic=True),
    "json.bool_false": Style(color=Color.RED.value, italic=True),
    "json.null": Style(color=Color.PURPLE.value, italic=True),
    "json.str": Style(color=Color.GREEN.value),
    "json.key": Style(color=Color.BLUE.value, bold=True),
    "traceback.error": Style(color=Color.BRIGHT_RED.value, italic=True),
    "traceback.border": Style(color=Color.BRIGHT_RED.value),
    "traceback.title": Style(color=Color.BRIGHT_RED.value, bold=True),
})

console = Console(theme=TEXTUAL_RICH_THEME)

def _configure_rich_theme():
    """Configure Textual Rich theme"""
    global _rich_configured
    if _rich_configured:
        return
    reconfigure(theme=TEXTUAL_RICH_THEME)

    global console
    console = Console(theme=TEXTUAL_RICH_THEME)
    install(console=console)
    

def _get_textual_rich_logger(name: str, log_level: Optional[str] = None) -> logging.Logger:
    """Get textual rich logger"""
    logger = logging.getLogger(name)

    if not any(isinstance(handler, RichHandler) for handler in logger.handlers):
        rich_handler = RichHandler(markup=True)
        rich_handler.setFormatter(logging.Formatter("%(message)s"))
        logger.addHandler(rich_handler)

    return logger

_configure_rich_theme()

logger = _get_textual_rich_logger(__name__)

def configure_logging(log_level: Optional[str] = None):
    """Configure logging"""
    if not log_level:
        log_level = os.environ.get("LOG_LEVEL", "INFO").upper()

    global logger
    logger = _get_textual_rich_logger(__name__, log_level=log_level)