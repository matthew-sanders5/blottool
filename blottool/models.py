from dataclasses import dataclass
from typing import Optional

@dataclass
class ROI:
    label: str
    x: int
    y: int
    width: int
    height: int
    bg_x: Optional[int] = None
    bg_y: Optional[int] = None
    bg_width: Optional[int] = None
    bg_height: Optional[int] = None
