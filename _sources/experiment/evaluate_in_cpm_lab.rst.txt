.. _evaluate_in_cpm_lab:

Evaluate in the CPM Lab
=======================

This guide explains how to run a trained SigmaRL policy through the CPM Lab ROS 2 workflow.

Before You Start
----------------

This page assumes that:

1. SigmaRL has already been installed inside the CPM Lab workspace as described in :ref:`install_sigmarl_within_cpm_lab`.
2. You have a trained SigmaRL policy folder available, as described in :ref:`evaluate_in_sigmarl`.

If these prerequisites are not satisfied yet, first complete the linked installation and SigmaRL evaluation guides.

Prepare the CPM Lab Simulation
------------------------------

Before starting the SigmaRL controller, prepare the CPM Lab simulation setup. Follow the :ref:`external_motions_planner` workflow until the experiment setup screen.

When selecting the map, choose ``Lab Full``. The external motions planner example uses ``Lab Outer Circle``, but the SigmaRL CPM Lab evaluation should use the full lab map.

.. important::

   If the Control Center offers a built-in high-level controller option, leave it disabled so that the external SigmaRL controller can take control.

Run the Controller in Separate Terminals
----------------------------------------

You will usually use three terminals. Every terminal is independent, so environment variables and ``source`` commands must be run again in each terminal.

Terminal 1: Optional Zenoh Router
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This terminal is only needed if your setup uses Zenoh.

.. code:: bash

   source /opt/ros/jazzy/setup.bash
   ros2 run rmw_zenoh_cpp rmw_zenohd

Terminal 2: RViz
~~~~~~~~~~~~~~~~

Open a new terminal and run:

.. code:: bash

   export WORKSPACE_DIR="$HOME/Documents/ros2-workspace-lab"
   cd "$WORKSPACE_DIR"
   export ROS_DOMAIN_ID=21
   source /opt/ros/jazzy/setup.bash
   source "$WORKSPACE_DIR/install/setup.bash"
   rviz2 -d ./src/cpm_lab/rviz/default.rviz

Terminal 3: SigmaRL Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open another new terminal and run:

.. code:: bash

   export WORKSPACE_DIR="$HOME/Documents/ros2-workspace-lab"
   export SIGMARL_VENV="$HOME/venvs/sigmarl-py312"
   export ROS_DOMAIN_ID=1
   cd "$WORKSPACE_DIR"
   source "$SIGMARL_VENV/bin/activate"
   source /opt/ros/jazzy/setup.bash
   source "$WORKSPACE_DIR/install/setup.bash"
   ros2 launch cpm_lab_sigmarl_control sigmarl_control_planner.launch.py vehicle_ids:=[1,2,3,4] period:=100 model_path:=<path-to-policy-output>

The ``vehicle_ids`` argument must match the vehicles started in the simulation. The ``period`` argument should match the bridge period configured in the Control Center. The ``model_path`` argument should point to the trained SigmaRL policy folder that you want to evaluate in the CPM Lab workflow.
