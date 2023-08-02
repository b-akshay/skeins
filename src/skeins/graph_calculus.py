"""
Implements graph calculus, as described in: 
- https://akshay.bio/variable-expectations/graph-calculus/
"""


import numpy as np, scipy


def symmetric_part(A):
    """ Returns the symmetrized version of the input matrix. """
    return 0.5*(A + A.T)

def asymmetric_part(A):
    """ Returns the anti-symmetrized version of the input matrix. """
    return 0.5*(A - A.T)

def grad_op_graph(fn, adj_mat):
    """
    Gradient of a function on a (n x n) graph.
    Args: 
        fn: A function on vertices (n-dimensional vector)
        adj_mat: (n x n) Adjacency matrix of graph
    Returns:
        Matrix ((n x n) directed graph) of gradients on edges.
    """
    return adj_mat.multiply(fn) - adj_mat.multiply(fn).T


def compute_transitions_asym(adj_mat):
    W = symmetric_part(adj_mat)
    recip = np.reciprocal(np.asarray(W.sum(axis=0)).astype(np.float64))
    recip[np.isinf(recip)] = 0
    return scipy.sparse.spdiags(recip, 0, W.shape[0], W.shape[0]).dot(W)

def laplacian_op_graph(adj_mat, normalize=True):
    """
    Laplacian of a function over graph vertices.
    
    Args:
        adj_mat: adjacency matrix for data kNN graph.
        normalize: Whether to degree-normalize the Laplacian matrix. 
    Returns: 
        Laplacian matrix (V x V).
    """
    if not normalize:
        lapmat = scipy.sparse.diags(np.ravel(adj_mat.sum(axis=0))) - adj_mat
    else:
        lapmat = scipy.sparse.identity(adj_mat.shape[0]) - compute_transitions_asym(adj_mat)
    return lapmat

def div_op_graph(field_mat, adj_mat):
    """
    Divergence of a function in a neighborhood on the data manifold. 
    Args:
        field_mat: a vector field (function on edges, i.e. (V x V) matrix-valued)
        adj_mat: adjacency matrix for data kNN graph.
    Returns: 
        Array of vertex-wise divergence values.
    """
    trans_mat = compute_transitions_asym(adj_mat)
    return np.ravel(trans_mat.multiply(asymmetric_part(field_mat)).sum(axis=1))

def curl_op_graph(field_mat, adj_mat):
    """
    Curl of a function on edges of a (cell x cell) graph.
    Args: 
        field_mat: a vector field (function on edges, i.e. (V x V) matrix-valued)
        adj_mat: (cell x cell) Adjacency matrix of graph
    Returns:
        Matrix of curl associated with each edge.
    """
    np.reciprocal(adj_mat.data, out=adj_mat.data)
    return adj_mat.multiply(symmetric_part(field_mat))


def helmholtz(
    field_mat, 
    adj_mat, 
    given_divergence=None
):
    """
    Compute Helmholtz decomposition of input edge function on graph.
    Args:
        adj_mat: adjacency matrix for data kNN graph.
        field_mat: a vector field (function over edges, i.e. matrix-valued)
        given_divergence: a given divergence function over vertices. 
            Replaces the use of field_mat if the source/sink info is known.
    Returns: 
        Pair of (vertex potential P, edge potential S) such that
        field_mat = - ∇P + S + U
        where U is a "harmonic" edge flow which is divergence-free, and 0 when field_mat is symmetric.
    """
    laplacian_op = laplacian_op_graph(adj_mat)
    if given_divergence is not None:
        sympart = scipy.sparse.csr_matrix(adj_mat.shape)
        potential = scipy.sparse.linalg.lsmr(
            laplacian_op, 
            given_divergence
        )
    else:
        sympart = symmetric_part(field_mat)
        potential = scipy.sparse.linalg.lsmr(
            laplacian_op, 
            div_op_graph(field_mat, adj_mat)
        )
    return (potential[0], sympart)



