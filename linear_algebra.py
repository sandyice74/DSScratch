# Chapter 4 Linear Algebra
# Vector
from functools import reduce, partial


def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]


def vectore_substract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


def vector_sum(vectors):
    return reduce(vector_add, vectors)


vector_sum = partial(reduce, vector_add)


def scalar_multiply(c, v):
    """c is a number v is a vector"""
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v, w):
    """v1*w1+ v2*w2+...+v_n*wn"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """v1*v1+v2*v2+....vn*vn"""
    return dot(v, v)


def squared_distance(v, w):
    """(v1-w1)**2 + ...(vn-wn)**2"""
    return sum_of_squares(vectore_substract(v, w))


# Matrices
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A, i):
    return A[i]


def get_column(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows * num_cols matrix whose
    (i,j)th entry is entry_fn(i,j)"""
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]


def is_diagonal(i, j):
    return 1 if i == j else 0


identity_matrix = make_matrix(5, 5, is_diagonal)
print (identity_matrix)
