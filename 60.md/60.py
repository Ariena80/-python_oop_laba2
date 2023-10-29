class Store:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        keys = key.split('.')
        current = self.data
        for k in keys:
            if k in current:
                current = current[k]
            else:
                return None
        return current

    def modify(self, key, new_value):
        keys = key.split('.')
        current = self.data
        for k in keys[:-1]:
            if k in current:
                current = current[k]
            else:
                return
        if keys[-1] in current:
            current[keys[-1]] = new_value

    def delete(self, key):
        keys = key.split('.')
        current = self.data
        for k in keys[:-1]:
            if k in current:
                current = current[k]
            else:
                return
        if keys[-1] in current:
            del current[keys[-1]]

#Пример
store = Store()
store.set('key', {'a': 1, 'b': 2, 'c': 3})
res = store.get('key')
print(res)  # Output: {'a': 1, 'b': 2, 'c': 3}
res = store.get('key.a')
print(res)  # Output: 1
res = store.get('key.b')
print(res)  # Output: 2

store.modify('key.b', 4)
res = store.get('key.b')
print(res)  # Output: 4

store.delete('key.c')
res = store.get('key')
print(res)  