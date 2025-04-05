class Drone:
    def __init__(self):
        pass


class BulkControl:
    """
    A class to manage bulk control actions for a set of drones.

    Wraps a list, applies commands to all drones in the list.
    """

    def __init__(self, drones: [Drone]):
        self.drones = drones
        pass


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

    def __init__(self):
        pass

    def __getitem__(self, key) -> BulkControl:
        """
        Retrieves a `BulkControl` object that allows bulk control over
        specified drones (either by their IDs or 'all' for all drones).

        Example:
            drone_ctl[1, 3, 4].arm()   # Arms drones with IDs 1, 3, and 4
            drone_ctl['all'].disarm()  # Disarms all drones
        """
        pass
