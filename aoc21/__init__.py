from pathlib import Path
from typing import List

path_input = Path(__file__).parent.parent / 'input'


def get_input_lines(day: int) -> List[str]:
    text_raw = (path_input / f'{day}.txt').read_text(encoding='utf8')
    return text_raw.splitlines()
