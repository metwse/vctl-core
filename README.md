# Drone Control Utilities
This repository contains low-level drone connection wrappers, mock drone APIs,
and guidelines for setting up simulation environments.

- [`simulation_setup.md`](simulation_setup.md) provides a thorough guide for
setting up the simulation environment required by `gz_ctl`.
- The `gz_ctl` package exposes two main functions: `initialize_environment`,
which starts a Gazebo simulation, and `kill_environment`, which stops the
currently running environment. After initialization, an instance of `DroneCtl`
is returned, offering a high-level interface for drone management.
- The `mock_sim` module provides the same interface as `gz_ctl`, acting as a
lightweight, dependency-free mock simulation. It's useful for fuzz testing
and in environments where Gazebo is not available.

For more information about each package, refer to their respective directories.
