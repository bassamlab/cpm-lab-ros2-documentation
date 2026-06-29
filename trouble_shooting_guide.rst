.. _trouble_shooting_guide:

Troubleshooting Guide
========================

RViz is not showing anything
--------------------------------

There is a problem with some rendering systems. If RViz is not showing the 3D world as expected, try disabling hardware acceleration.

.. code:: bash

    # Manually for this terminal
    export LIBGL_ALWAYS_SOFTWARE=1

    # Automatically for all future terminals
    echo "export LIBGL_ALWAYS_SOFTWARE=1" >> ~/.bashrc


Usefull commands
-----------------

Verify the IP address assignment:

.. code:: bash

    ip a

Check if time synchronization is working:

.. code:: bash

    timedatectl status

Check console log for NTP errors:

.. code-block:: bash

    journalctl -u systemd-timesyncd

Force the car to resync time

.. code-block:: bash

    sudo timedatectl set-ntp false
    sudo timedatectl set-ntp true