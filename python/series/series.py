def slices(series, length):
    if length <= 0 or length > len(series):
        raise ValueError('Invlid length value')
    sublists = []
    for i in range(len(series)-length+1):
        sublists.append(series[i:length+i])
    return sublists
