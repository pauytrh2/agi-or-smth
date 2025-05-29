import re
from typing import Tuple

def parse(text: str) -> Tuple[str, str]:
    # extract human
    human_match = re.search(r'#\s*Human:\s*\n(.+?)(?=\n#\s*Action:)', text, re.DOTALL)
    # extract action
    action_match = re.search(r'#\s*Action:\s*\n(.+)', text, re.DOTALL)

    if not human_match or not action_match:
        raise ValueError("Invalid format. Both # Human: and # Action: sections must be present.")

    human_text = human_match.group(1).strip()
    action = action_match.group(1).strip()

    return human_text, action