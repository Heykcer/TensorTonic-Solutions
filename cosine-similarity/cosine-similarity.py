import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dot=np.dot(np.asarray(a,dtype=float),np.asarray(b,dtype=float))
    mod_a=np.linalg.norm(np.asarray(a,dtype=float))
    mod_b=np.linalg.norm(np.asarray(b,dtype=float))
    if mod_a == 0 or mod_b ==0:
        return 0.0
    return float(dot/(mod_a*mod_b))
    pass