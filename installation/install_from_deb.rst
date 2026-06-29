.. _install_from_deb:

Install from Debian Packages
=============================

This guide will help you build the CPM Lab ROS2 project from Debian packages. This installation
does not allow to modify components of the CPM Lab but it allows the user to run the CPM Lab ROS2
stack with all its features.

Installation Steps
--------------------------------------

Follow these steps to set up the CPM Lab ROS2 environment:

1. Install ROS2
~~~~~~~~~~~~~~~

Follow the official installation instructions for your system:

* `ROS2 Humble (Ubuntu 22.04) <https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html>`_
* `ROS2 Jazzy (Ubuntu 24.04) <https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html>`_

2. Setup Repository
~~~~~~~~~~~~~~~~~~~~

The installation of the CPM Lab ROS2 strack is similar to the installation of ROS. First, you need to add our GPG key to your system. Download the :download:`key </assets/cpm-archive-keyring.gpg.key>` and navigate to the download direcotry. Remove the ASCII armor and move it to the keyring directory:

.. code:: bash

    cd <download-directory>
    gpg --dearmor < cpm-archive-keyring.gpg.key | sudo tee /usr/share/keyrings/cpm-archive-keyring.gpg > /dev/null

Then, add the repository to your system:

.. code:: bash

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/cpm-archive-keyring.gpg] https://cpm.lrt.unibw.de/apt $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/cpmros.list > /dev/null

3. Install the CPM Lab
~~~~~~~~~~~~~~~~~~~~~~

Now, you can install the CPM-Lab ROS2 workspace. First, update your package list and then install
the CPM-Lab ROS2 workspace:

.. code:: bash

    sudo apt update
    sudo apt install ros-<ros2-distro>-cpm-lab

4. Install alternative ROS2 Middleware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default ROS2 middleware, FastDDS, causes unexpected network issues. We recommend switching over to the more stable Eclipse CycloneDDS implementation.

.. code:: bash

    sudo apt update
    sudo apt install ros-<ros2-distro>*cyclone*
    
    # Manually setting the implementation for this terminal
    export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

    # Automatically setting the implementation for all future terminals
    echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc


5. Launch RViz
~~~~~~~~~~~~~~

🖥️  Download the CPM-Lab :download:`RViz configuration </assets/default.rviz>` and launch RViz.

.. code:: bash

    source /opt/ros/<ros2-distro>/setup.bash
    export ROS_DOMAIN_ID=21
    rviz2 -d <path-to-rviz-config>

🎉 You're Done! 🎉
-------------------

You have successfully installed the CPM Lab ROS2 stack using Debian packages. 

If you run into issues, refer to the :ref:`trouble_shooting_guide` or ask for help via our Slack.

.. admonition:: Next Steps

   Now that you have the CPM Lab ROS2 stack installed, you can start testing your motion planner. Refer to our :ref:`experiment` section for guidance on how to set up and run experiments in the CPM Lab.
