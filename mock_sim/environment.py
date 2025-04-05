from .simulation import DroneCtl


def initialize_environment(drone_count: int) -> DroneCtl:
    return DroneCtl(drone_count)


def kill_environment():
    pass
