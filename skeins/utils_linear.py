"""
Linear algebra utilities.
"""


import numpy as np, scipy, sklearn
from scipy._lib._util import check_random_state, rng_integers
from scipy.sparse import csc_matrix


def linear_dim_reduction(target_dim, source_dim, mode='sparse_rp'):
    """Dimensionality reduction using oblivious random projection and sketching.

    Parameters
    ----------
    target_dim : int
        The target dimensionality.
    source_dim : int
        The source dimensionality.
    mode : str
        The mode of dimensionality reduction. One of `['dense_rp', 'sparse_rp', 'cwt']`. 
        Defaults to `'sparse_rp'`.
    
    Returns
    -------
    S : (target_dim, source_dim) sparse matrix
        The matrix S which represents the dimensionality reduction.
    
    Notes
    -----
    [1]__ describes dense Gaussian projections.
    [2]__ describes very sparse projections.
    [3]__ describes Clarkson-Woodruff sketching ("subspace embedding").

    References
    ----------
    .. [1] Sanjoy Dasgupta, Anupam Gupta, An elementary proof of a theorem of Johnson and Lindenstrauss, Random Structures and Algorithms 22 (1) (2003) 60–65.
    .. [2] Ping Li, Trevor Hastie, Kenneth Church, Very sparse random projections, In Proceedings of the 12th ACM SIGKDD international conference on Knowledge discovery and data mining, pp. 287-296.
    .. [3] Kenneth Clarkson, David Woodruff, Journal of the ACM (JACM) 63 (6): 1–45.
    """
    if mode == 'dense_rp':
        return sklearn.random_projection._gaussian_random_matrix(
            n_components=target_dim, n_features=source_dim, random_state=None).transpose()
    elif mode == 'sparse_rp':
        return sklearn.random_projection._sparse_random_matrix(
            n_components=target_dim, n_features=source_dim, density='auto', random_state=None).transpose()
    elif mode == 'cwt':
        return cwt_matrix(target_dim, source_dim)
    else:
        raise ValueError('Unknown mode of dimensionality reduction.')


def cwt_matrix(n_rows, n_columns, seed=None):
    """
    Generate a matrix S which represents a Clarkson-Woodruff transform.

    Given the desired size of matrix, the method returns a matrix S of size
    (n_rows, n_columns) where each column has all the entries set to 0
    except for one position which has been randomly set to +1 or -1 with
    equal probability.

    Parameters
    ----------
    n_rows : int
        Number of rows of S
    n_columns : int
        Number of columns of S
    seed : {None, int, `numpy.random.Generator`, `numpy.random.RandomState`}, optional

    Returns
    -------
    S : (n_rows, n_columns) csc_matrix
        The returned matrix has ``n_columns`` nonzero entries.

    Notes
    -----
    Given a matrix A, with high probability,
    .. math:: 
    
            \|SA\| = (1 \pm \epsilon)\|A\|

    where the error epsilon is related to the size of S.

    Code here is from https://github.com/scipy/scipy/blob/v1.11.2/scipy/linalg/_sketches.py
    """
    rng = check_random_state(seed)
    rows = rng_integers(rng, 0, n_rows, n_columns)
    cols = np.arange(n_columns+1)
    signs = rng.choice([1, -1], n_columns)
    S = csc_matrix((signs, rows, cols),shape=(n_rows, n_columns))
    return S