def check_safety(func):                             
    def wrapper():
        try:
            return func() 
        except Exception as e:
            return False
    return wrapper

def ensure_vals(glo, *args):
    for arg in args:
        if not arg in glo:
            glo[arg] = None