.. _install_sigmarl_within_cpm_lab:

Install SigmaRL within CPM Lab
==============================

This guide explains how to install SigmaRL in a dedicated virtual environment and build the ROS 2 workspace with the same Python interpreter.

The commands below assume that the CPM Lab ROS 2 workspace is located at:

.. code:: bash

   $HOME/Documents/ros2-workspace-lab

If your workspace is somewhere else, replace the paths accordingly.

What This Package Does
----------------------

``cpm_lab_sigmarl_control`` runs a SigmaRL-based high-level controller for CPM Lab vehicles.

The controller:

1. receives vehicle states from the bridge,
2. computes actions with a trained SigmaRL policy,
3. publishes vehicle commands back to the CPM Lab stack.

Before You Start
----------------

This guide assumes that:

1. ROS 2 Jazzy is already installed.
2. The CPM Lab ROS 2 workspace has already been cloned to ``~/Documents/ros2-workspace-lab``.
3. You want to keep SigmaRL and its Python dependencies in a separate virtual environment instead of installing them system-wide.

Using a dedicated virtual environment is recommended for SigmaRL because packages such as ``torch``, ``cvxpy``, and related ML dependencies should not be mixed into the system Python installation.

1. Define Helpful Paths
-----------------------

Open a terminal and run:

.. code:: bash

   export WORKSPACE_DIR="$HOME/Documents/ros2-workspace-lab"
   export SIGMARL_DIR="$HOME/Documents/marl_for_cavs"
   export SIGMARL_VENV="$HOME/venvs/sigmarl-py312"

These variables are only for convenience. They make the next commands easier to read and copy.

2. Clone the SigmaRL Repository
-------------------------------

If you have not cloned SigmaRL yet, run:

.. code:: bash

   mkdir -p "$HOME/Documents"
   cd "$HOME/Documents"
   git clone https://git.rwth-aachen.de/CPM/Project/jianye/software/marl_for_cavs "$SIGMARL_DIR"
   cd "$SIGMARL_DIR"

If you want a specific branch, switch to it now:

.. code:: bash

   git checkout <branch-name>

3. Create and Activate a Virtual Environment
--------------------------------------------

Create a Python virtual environment named ``sigmarl-py312``:

.. code:: bash

   python3 -m venv "$SIGMARL_VENV"

Activate it:

.. code:: bash

   source "$SIGMARL_VENV/bin/activate"

Upgrade the basic Python packaging tools:

.. code:: bash

   python -m pip install --upgrade pip setuptools wheel

Install ``colcon`` into the virtual environment. This helps ensure that ROS 2 Python entrypoints are built with the same interpreter as SigmaRL:

.. code:: bash

   python -m pip install colcon-common-extensions

4. Install SigmaRL in Editable Mode
-----------------------------------

Install the local ``marl_for_cavs`` checkout in editable mode:

.. code:: bash

   python -m pip install -e "$SIGMARL_DIR"

Editable mode means that changes inside the SigmaRL repository are picked up directly from the source tree without reinstalling the package every time.

You can verify that the installation worked with:

.. code:: bash

   python -m pip show sigmarl

5. Build the ROS 2 Workspace
----------------------------

Go to the workspace root:

.. code:: bash

   cd "$WORKSPACE_DIR"

Build the complete workspace with the helper script:

.. code:: bash

   ./bash/build-with-sigmarl-venv.sh --all --clean

This script:

1. activates the chosen virtual environment,
2. sources ROS 2 Jazzy,
3. runs the build with the virtual environment Python,
4. checks that the generated SigmaRL ROS 2 entrypoint uses the virtual environment interpreter.

After the build finishes, source the workspace overlay:

.. code:: bash

   source "$WORKSPACE_DIR/install/setup.bash"

6. Run the SigmaRL Planner
--------------------------

After the workspace has been built and sourced, you can launch the SigmaRL planner with a trained policy:

.. code:: bash

   export WORKSPACE_DIR="$HOME/Documents/ros2-workspace-lab"
   export SIGMARL_VENV="$HOME/venvs/sigmarl-py312"
   export ROS_DOMAIN_ID=1
   cd "$WORKSPACE_DIR"
   source "$SIGMARL_VENV/bin/activate"
   source /opt/ros/jazzy/setup.bash
   source "$WORKSPACE_DIR/install/setup.bash"
   ros2 launch cpm_lab_sigmarl_control sigmarl_control_planner.launch.py vehicle_ids:=[1,2,3,4] period:=100 model_path:=<path-to-policy-output>

The ``model_path`` argument should point to the trained SigmaRL policy folder. The ``vehicle_ids`` and ``period`` arguments must match the vehicles and bridge period used in the CPM Lab experiment setup.

For the full multi-terminal evaluation workflow, continue with :ref:`evaluate_in_cpm_lab`.
