# Spare Parts Inventory Management

## Overview
This repository presents a Python-based solution for optimizing spare parts inventory management using dynamic programming techniques, specifically value iteration. The model addresses the complexities of spare parts inventory systems, incorporating factors like lead times, demand variability, and downtime costs.

## Features

- **Value Iteration Implementation:** Utilizes dynamic programming to compute optimal inventory policies.
- **Scenario Simulation:** Includes scripts to simulate various inventory scenarios and assess policy performance.
- **Cost Analysis:** Models different cost structures, including downtime costs based on expected downtime length.
- **Policy Visualization:** Generates plots to visualize optimal policies under varying parameters.

## Notes

The cost and transition matrices are stored as large NumPy arrays and are not included in this repository. The main optimization script (Main_Optimisation_Script.ipynb) will run without them, but to execute most of the other scripts, you will first need to run the optimization to generate these matrices locally.