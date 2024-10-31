def top_n (items,n):
    """Returns the top n items in the list, in descending order.

    Args:
        items (list): The list  to be returned.
        n (int): The number of items to return

    Returns:
        array: Top n items in the list, in descending order.
    """
    len_n = len(items)
    for i in range(n):
        for j in range(len_n - 1 - i):
            if items[j] > items[j + i]:
                items[j], items[j +1]= items[j + i], items[j]
    
    top_n = items[-n:]
    return top_n[::-1]
    