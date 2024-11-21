
def mad(data):
    """ 
    Calculates the Mean Absolute Deviation (MAD) from a sample. MAD is the mean absolute deviation from the 
    sample median.

    Naive Implementation

    Developer Notes: QuickSort implementation possible

    Args:
        data (list/iterable): A list or iterable of int or float for which a MAD calculation is desired

    Returns:
        int/float: Mean Average Deviation 
    """
    if not (isinstance(data, int) or isinstance(data, int) or isinstance(data, list) or isinstance(data, tuple)): 
        raise ValueError("Data supplied has to be a int, float, or iterable (tuple or list).")
        
    # Invalid input
    if len(data) == 0:
        raise ValueError("Data cannot be empty.")

    # Median Calculation
    sorted_data = sorted(data)
    n = len(sorted_data)
    # Odd length input elements
    if n % 2 == 1:
        median = sorted_data[n // 2]
    # Even length input element (mean of 2)
    else:
        median = (sorted_data[(n // 2) - 1] + sorted_data[n // 2]) / 2
    
    # Calculation deviation from median
    absolute_deviations = [abs(x - median) for x in data]
    
    # Final mad calculation 
    mad_value = sum(absolute_deviations) / n
    
    return mad_value
