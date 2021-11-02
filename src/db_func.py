import pandas as pd

def set(key, value):
    """Sets value associated with a key. No return value"""
    new_data = pd.DataFrame({
        'Trains': key,
        'Times': [value]
    })
    new_data.to_csv('Transit-Info.csv', mode='a', index=False, header=False)

def fetch(key):
    """Retrieve object set at a key. Returns object, else None"""
    data = pd.read_csv('Transit-Info.csv', header = 0, index_col=0, squeeze=True).to_dict()
    if key in data:
        return data[key]
    return None

def keys():
    """Returns list of all keys in database, else None"""
    data = pd.read_csv('Transit-Info.csv', header = 0, index_col=0, squeeze=True).to_dict()
    if data.keys():
        return list(data.keys())
    return None
