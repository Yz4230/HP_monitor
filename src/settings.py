from typing import cast

from src.const_settings import TOKENS_JSON_PATH
from src.custom_types import TokenTable
from src.utils import load_json_default

TOKEN_TABLE = cast(TokenTable, load_json_default(TOKENS_JSON_PATH))
