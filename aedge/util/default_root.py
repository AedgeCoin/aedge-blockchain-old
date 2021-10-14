import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("AEDGE_ROOT", "~/.aedge/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("AEDGE_KEYS_ROOT", "~/.aedge_keys"))).resolve()
