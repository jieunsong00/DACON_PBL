def check_safety(func):                             
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs) 
        except Exception as e:
            return False
    return wrapper

def ensure_vals(glo, *args):
    for arg in args:
        if not arg in glo:
            glo[arg] = None