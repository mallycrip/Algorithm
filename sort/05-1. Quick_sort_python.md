def quick_sort(collection: list):
    if len(collection) < 2:
        return collection

    pivot = collection.pop()
    lesser = []
    greater = []

    for i in collection:
        if i > pivot:
            greater.append(i)
        else:
            lesser.append(i)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)
