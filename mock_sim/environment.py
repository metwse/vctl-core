from .simulation import DroneCtl
import time


def initialize_environment(drone_count: int) -> DroneCtl:
    # Mock sleep to emulate Gazebo startup delay.
    time.sleep(3)
    return DroneCtl(drone_count)


def kill_environment(drone_ctl: DroneCtl):
    time.sleep(1)
    return True
