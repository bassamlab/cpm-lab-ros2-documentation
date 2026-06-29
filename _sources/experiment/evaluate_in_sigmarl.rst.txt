.. _evaluate_in_sigmarl:

Evaluate in SigmaRL
===================

This guide explains how to train a SigmaRL policy and evaluate SigmaRL policies in simulation.

There are two common policy sources:

1. a policy that you train yourself with ``main_training.py``,
2. a published checkpoint that you download to reproduce the results from :ref:`Zero-Shot MARL Benchmark in the Cyber-Physical Mobility Lab <beerwerth2026zeroshot>`.

Both policies are evaluated with the same SigmaRL evaluation scripts. The downloaded checkpoint is mentioned only for users who want to reproduce the published results. See :ref:`literature` for the full citation.

Train a SigmaRL Policy
----------------------

Clone and enter the `SigmaRL repository <https://github.com/bassamlab/SigmaRL>`_:

.. code:: bash

   git clone https://github.com/bassamlab/SigmaRL.git
   cd SigmaRL

Before training, adjust ``parameters.where_to_save`` in the training script or configuration to define the folder where the trained policy should be saved. Then run ``main_training.py`` to train a MARL policy.

.. code:: bash

   python main_training.py

After training, place the saved policy folder where the evaluation scripts expect to find checkpoints, or adapt the script configuration to point to your policy output folder.

Evaluate a SigmaRL Policy
-------------------------

Use the SigmaRL evaluation scripts to evaluate either a policy trained with ``main_training.py`` or a downloaded checkpoint.

Run the parallel evaluation script:

.. code:: bash

   python sigmarl/eva_at25/run_models_parallel.py

The evaluation results are saved automatically. This script requires Python parallel workers. If you do not want to use parallel workers, run the sequential script instead:

.. code:: bash

   python sigmarl/eva_at25/run_models.py

After the evaluation finishes, run the aggregation script to analyze the results and obtain the performance metrics:

.. code:: bash

   python sigmarl/eva_at25/marl_aggregated_evaluation.py

Reproduce the SigmaRL Simulation Results
----------------------------------------

To reproduce the SigmaRL simulation results reported in :ref:`Zero-Shot MARL Benchmark in the Cyber-Physical Mobility Lab <beerwerth2026zeroshot>`, use the tagged SigmaRL release and the published checkpoints.

First, check out the corresponding tag:

.. code:: bash

   cd <path-to-SigmaRL-repository>
   git checkout 1.5.0

Download ``at25.zip`` from `the checkpoint page <https://github.com/bassamlab/assets/blob/main/sigmarl/checkpoints/at25.zip>`_. Unzip it, then copy the extracted ``at25`` folder into the ``checkpoints`` folder at the root of the SigmaRL repository.

The resulting structure should be:

.. code:: text

   root/checkpoints/at25/

Then run the same evaluation and aggregation scripts described above.
