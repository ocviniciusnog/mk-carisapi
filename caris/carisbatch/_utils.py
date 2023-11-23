
def ensure_iterable(items):
    if isinstance(items, str) or not hasattr(items, '__iter__'):
        items = [items]
    return items
    
class Dispatcher:
    def __init__(self):
        self.handlers = {}

    def register(self, type, handler):
        self.handlers[type] = handler

    def dispatch(self, type, *args, **kwargs):
        if type in self.handlers:
            return self.handlers[type](*args, **kwargs)
        else:
            raise ValueError("No handler registered for command: " + str(type))
