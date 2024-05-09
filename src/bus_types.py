from enum import Enum, auto


class BusTypes(Enum):
    """Enum to define supported CAN bus interface types."""

    SIM = auto()
    VIRTUAL = auto()
    PEAK = auto()
