class Drone:
    def __init__(self, id: int):
        self.id = id
        self.is_armed = False

    def arm(self, force: bool):
        if not self.is_armed:
            self.is_armed = True
            return True
        return False

    def disarm(self, force: bool):
        if self.is_armed:
            self.is_armed = False
            return True
        return False

    def takeoff(self, altitude: int):
        return self.is_armed

    def emergency(self):
        return True

    def land(self):
        return self.is_armed

    def track(self):
        return self.is_armed

    def move(self, x: float, y: float, z: float, v: float):
        return self.is_armed


class BulkControl:
    """
    A class to manage bulk control actions for a set of drones.

    Wraps a list, applies commands to all drones in the list.
    """

    def __init__(self, drones: [Drone]):
        self.drones = drones
        pass

    def __getattr__(self, attr):
        def dynamic_method(*args, **kwargs):
            result = []
            for drone in self.drones:
                result.append(getattr(drone, attr)(*args, **kwargs))
            return result
        return dynamic_method


class DroneCtl:
    """
    A class to manage a collection of drones in a simulation.

    This class provides a high-level interface for interacting with drones
    in the simulation. It supports bulk operations on drones via indexing,
    and can execute control commands such as arming, disarming, and other
    high-level actions.

    Usage:
        - Access drones using indexing, e.g., `drone_ctl[1, 3, 4]` to control
        drones with IDs 1, 3, and 4.
        - Use `drone_ctl['all']` to control all drones in the simulation.
    """

    def __init__(self, drone_count: int):
        self.drone_count = drone_count
        self.drones = [
            Drone(i) for i in range(drone_count)
        ]

    def __getitem__(self, item) -> BulkControl:
        """
        Retrieves a `BulkControl` object that allows bulk control over
        specified drones (either by their IDs or 'all' for all drones).

        Example:
            drone_ctl[1, 3, 4].arm()   # Arms drones with IDs 1, 3, and 4
            drone_ctl['all'].disarm()  # Disarms all drones
        """

        if item == 'all':
            return BulkControl(self.drones)
        elif isinstance(item, int):
            return BulkControl([self.drones[item]])
        elif isinstance(item, tuple) or isinstance(item, list):
            return BulkControl([self.drones[i] for i in item])
        else:
            return BulkControl([])
