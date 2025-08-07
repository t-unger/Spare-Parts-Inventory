import pandas as pd
import numpy as np
import state_space_setup as sss


def generate_sS_policy(s, S, max_parts):
    """
    Input: s (int): The inventory threshold - if the current inventory level
                    falls to or below this value, an order is placed.
           S (int): The order-up-to level when an order is placed.
           max_parts (int): The maximum number of parts in the inventory.
    Output: policy_df (pd.DataFrame): DataFrame representing the policy for each state.

    This function generates an (s, S) policy in terms of the inventory position.
    """
    state_space = sss.get_state_space(max_parts)
    state_tuples = list(map(tuple, state_space))
    inventory_position_col = list(map(sum, state_space))

    # create a dataframe with states as tuples
    policy_df = pd.DataFrame({
        'State': state_tuples,
        'IP': inventory_position_col
    })

    # add a column with corresponding actions
    policy_df['Order_size'] = np.where(policy_df['IP'] <= s, S - policy_df['IP'], 0)

    # drop the inventory position column
    policy_df.drop('IP', axis=1, inplace=True)

    return policy_df


def generate_sQ_policy(s, Q, max_parts):
    """
    Input: s (int): The inventory threshold - if the current inventory level
                    falls to or below this value, an order is placed.
           Q (int): The fixed order quantity.
           max_parts (int): The maximum number of parts in the inventory.
    Output: policy_df (pd.DataFrame): DataFrame representing the policy for each state.

    This function generates an (s, Q) policy in terms of the inventory position.
    """
    state_space = sss.get_state_space(max_parts)
    state_tuples = list(map(tuple, state_space))
    inventory_position_col = list(map(sum, state_space))

    # create a dataframe with states as tuples
    policy_df = pd.DataFrame({
        'State': state_tuples,
        'IP': inventory_position_col
    })

    # add a column with corresponding actions
    policy_df['Order_size'] = np.where(policy_df['IP'] <= s, Q, 0)

    # drop the inventory position column
    policy_df.drop('IP', axis=1, inplace=True)

    return policy_df
