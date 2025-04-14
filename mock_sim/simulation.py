class Drone:
    """Pseudo drone control class.

    Drone control commands may block the thread until a response is received
    from the simulation. Therefore, a non-blocking listener should be
    implemented in any code that calls `Drone` methods.
    """

    def __init__(self, id: int):
        self.id = id
        self.is_armed = False

        self.pos = [0, 0, 0]

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
        """Moves drone to provided absolute position.

        Relative calculations should NOT implemented in `Drone` class.
        """
        self.pos = [x, y, z]
        return self.is_armed

    def get_telemetry(self):
        return {
            'pos': self.pos,
            'v': 0,
        }


class BulkControl:
    """A class to manage bulk control actions for a set of drones.

    Wraps a list, applies commands to all drones in the list.
    """

    def __init__(self, drones: [Drone]):
        self.drones = drones
        pass

    def swarm_origin(self):
        """Calculate the origin for the drones.

        This method should be implemented to return the origin for the drones.
        """

        origin = [0, 0, 0]
        for drone in self.drones:
            for i in range(3):
                origin[i] += drone.pos[i]

        origin = [
            i / len(self.drones) for i in origin
        ]

        return origin

    def move(self, x: float, y: float, z: float, v: float):
        """Overriding function for `DroneCtl.move`.

        Moves the center of the swarm to the provided {x, y, z} coordinates
        if more than one drone is controlled by this instance of `BulkControl`.
        """

        origin = self.swarm_origin()

        results = []
        for drone in self.drones:
            # Shifted drone position with respect to the origin.
            target = [
                pos + drone.pos[i] - origin[i]
                for (i, pos) in enumerate([x, y, z])
            ]

            # TODO: Multithreaded listener design for bulk control.
            results.append(drone.move(*target, v))

        return results

    def formation(self, formation: str, v: float):
        match formation:
            case "V":
                pass
            case "INVERSE-V":
                pass
            case "LINE":
                pass
        # Target position refers to the relative positions of drones in the
        # formation.
        target_positions = [
            [0, 0, 0] for _ in self.drones
        ]

        # Applies relative transformations to target_positions.
        origin = self.swarm_origin()

        target_positions = [
            [p + origin[i] for (i, p) in enumerate(pos)]
            for pos in target_positions
        ]

        # TODO: Multithreaded listener design for bulk control.
        return [
            drone.move(*target_positions[i], v)
            for (i, drone) in enumerate(self.drones)
        ]

    def __getattr__(self, attr):
        def dynamic_method(*args, **kwargs):
            # TODO: Multithreaded listener design for bulk control.
            return [
                getattr(drone, attr)(*args, **kwargs)
                for drone in self.drones
            ]
        return dynamic_method


class DroneCtl:
    """A class to manage a collection of drones in a simulation.

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
        """Retrieves a `BulkControl` object that allows bulk control over
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

    def mainloop(self, stop_event):
        import time
        while not stop_event.is_set():
            print(f"Mock simulation running with {self.drone_count} drones")
            time.sleep(1)
