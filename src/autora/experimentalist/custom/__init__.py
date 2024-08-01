"""
Example Experimentalist
"""
import numpy as np
import pandas as pd

from typing import Union, List


def sample(
        conditions: Union[pd.DataFrame, np.ndarray],
        models: List,
        reference_conditions: Union[pd.DataFrame, np.ndarray],
        num_samples: int = 1) -> pd.DataFrame:
    """
    Samples new conditions to be applied to the next iteration of the experiment. Uses information from previous
    conditions, the current models. Conditions must be within the range provided by conditions.

    Args:
        conditions: The pool to sample from.
            Attention: `conditions` is a field of the standard state
        models: The sampler might use output from the theorist.
            Attention: `models` is a field of the standard state
        reference_conditions: The sampler might use reference conditons
        num_samples: number of experimental conditions to select

    Returns:
        (pd.DataFrame) Sampled pool of experimental conditions

    *Optional*
    Examples:
        These examples add documentation and also work as tests
        >>> example_sampler([1, 2, 3, 4])
        1
        >>> example_sampler(range(3, 10))
        3

    """
    # Naive Random sampling for now
    new_conditions = conditions.sample(num_samples)

    return new_conditions


def echo():
    """
    Simple function that prints "Hi" to verify successful installation.

    #TODO: DELETE IF RELEASED
    :return:
    """
    print("custom-experimentalist has been installed succesfully. ")