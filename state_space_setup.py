import numpy as np


def get_state_space(max_parts):
    """
    Input: max_parts (int): The maximum number of parts in the inventory.
    Output: state_sp (np.array): 2D array representing the state space of the model.

    This function generates the state space for our model. States are represented as np.arrays of length 2,
    where the first element is the inventory level and the second element is the number of parts ordered.
    The state space includes all combinations of inventory levels from 0 to max_parts and parts ordered
    from 0 to max_parts - current inventory level.
    """
    states = [(i, j) for i in range(max_parts + 1)
              for j in range(max_parts + 1 - i)]

    state_sp = np.array(states)
    return state_sp


def get_index(i, j, max_parts):
    return int(i * (max_parts + 1 - (i - 1) / 2) + j)


def get_action_space(state, max_parts):
    """
    Input: state (np.array): The current state of the system.
           max_parts (int): The maximum number of parts in the inventory & machines.
    Output: action_sp (np.array): 1D array representing the action space for the given state.

    This function generates the action space for a given state. Actions are represented as integers
    indicating the number of parts to order, ranging from 0 to (max_parts - current inventory level 
    - currently ordered parts).
    """
    actions = np.arange(0, max_parts + 1 - state[0] - state[1])
    return actions
