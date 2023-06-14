from enum import Enum


class HeightMetric(str, Enum):
    """Possible height metrics"""

    feet: str = "feet"
    cm: str = "cm"


class WeightMetric(str, Enum):
    """Possible weight metrics"""

    lbs: str = "lbs"
    kg: str = "kg"
