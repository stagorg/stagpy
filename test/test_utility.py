"""
Tests for utility functions in the library.
"""
import pytest
import numpy as np
import scipy.sparse
from context import stag
import stag.stag_internal
import stag.cluster
import stag.utility


def test_numpy_data_types():
    np_vec = np.asarray([1, 2, 3], dtype=np.int64)

    # This should not throw an error.
    stag_vec = stag.stag_internal.vectorl(np_vec)

    np_vec_2 = np.asarray([2, 3, 4], dtype=np.int64)
    sym_diff = stag.cluster.symmetric_difference(np_vec, np_vec_2)
    assert set(sym_diff) == {1, 4}


def test_add_sprsmat():
    mat1 = scipy.sparse.csc_matrix([[0, 1, 0, 1],
                                    [1, 0, 1, 0],
                                    [0, 1, 0, 1],
                                    [1, 0, 1, 0]])
    mat2 = scipy.sparse.csc_matrix([[2, 0, 1, 1],
                                    [0, 2, 0, 0],
                                    [0, 0, 2, 0],
                                    [1, 1, 0, 2]])
    sprsmat1 = stag.utility.SprsMat(mat1)
    sprsmat2 = stag.utility.SprsMat(mat2)
    mat3 = (sprsmat1 + sprsmat2).to_scipy()

    expected_mat = scipy.sparse.csc_matrix([[2, 1, 1, 2],
                                            [1, 2, 1, 0],
                                            [0, 1, 2, 1],
                                            [2, 1, 1, 2]])
    mat_diff = mat3 - expected_mat
    assert(np.all(mat_diff.todense() == pytest.approx(0)))

    # Test the compound addition operator
    sprsmat1 += sprsmat2
    mat_diff = sprsmat1.to_scipy() - expected_mat
    assert(np.all(mat_diff.todense() == pytest.approx(0)))


def test_sub_sprsmat():
    mat1 = scipy.sparse.csc_matrix([[0, 1, 0, 1],
                                    [1, 0, 1, 0],
                                    [0, 1, 0, 1],
                                    [1, 0, 1, 0]])
    mat2 = scipy.sparse.csc_matrix([[2, 0, 1, 1],
                                    [0, 2, 0, 0],
                                    [0, 0, 2, 0],
                                    [1, 1, 0, 2]])
    sprsmat1 = stag.utility.SprsMat(mat1)
    sprsmat2 = stag.utility.SprsMat(mat2)
    mat3 = (sprsmat1 - sprsmat2).to_scipy()

    expected_mat = scipy.sparse.csc_matrix([[-2, 1, -1, 0],
                                            [1, -2, 1, 0],
                                            [0, 1, -2, 1],
                                            [0, -1, 1, -2]])
    mat_diff = (mat3 - expected_mat)
    assert(np.all(mat_diff.todense() == pytest.approx(0)))

    # Test the compound subtraction operator
    sprsmat1 -= sprsmat2
    mat_diff = sprsmat1.to_scipy() - expected_mat
    assert(np.all(mat_diff.todense() == pytest.approx(0)))


def test_unary_negation_sprsmat():
    mat1 = scipy.sparse.csc_matrix([[0, 1, 0, 1],
                                    [1, 0, 1, 0],
                                    [0, 1, 0, 1],
                                    [1, 0, 1, 0]])
    sprsmat1 = stag.utility.SprsMat(mat1)
    mat2 = (-sprsmat1).to_scipy()

    expected_mat = scipy.sparse.csc_matrix([[0, -1, 0, -1],
                                            [-1, 0, -1, 0],
                                            [0, -1, 0, -1],
                                            [-1, 0, -1, 0]])
    mat_diff = (mat2 - expected_mat)
    assert(np.all(mat_diff.todense() == pytest.approx(0)))


def test_scalar_mul_sprsmat():
    mat1 = scipy.sparse.csc_matrix([[0, 1, 0, 1],
                                    [1, 0, 1, 0],
                                    [0, 1, 0, 1],
                                    [1, 0, 1, 0]])
    sprsmat1 = stag.utility.SprsMat(mat1)
    mat2 = (2 * sprsmat1).to_scipy()

    expected_mat = scipy.sparse.csc_matrix([[0, 2, 0, 2],
                                            [2, 0, 2, 0],
                                            [0, 2, 0, 2],
                                            [2, 0, 2, 0]])
    mat_diff = (mat2 - expected_mat)
    assert(np.all(mat_diff.todense() == pytest.approx(0)))

    mat2 = (sprsmat1 * 2).to_scipy()
    mat_diff = (mat2 - expected_mat)
    assert(np.all(mat_diff.todense() == pytest.approx(0)))

    sprsmat1 *= 2
    mat_diff = (sprsmat1.to_scipy() - expected_mat)
    assert(np.all(mat_diff.todense() == pytest.approx(0)))


def test_scalar_div_sprsmat():
    mat1 = scipy.sparse.csc_matrix([[0, 2, 0, 2],
                                    [2, 0, 2, 0],
                                    [0, 2, 0, 2],
                                    [2, 0, 2, 0]])
    sprsmat1 = stag.utility.SprsMat(mat1)
    mat2 = (sprsmat1 / 2).to_scipy()

    expected_mat = scipy.sparse.csc_matrix([[0, 1, 0, 1],
                                            [1, 0, 1, 0],
                                            [0, 1, 0, 1],
                                            [1, 0, 1, 0]])
    mat_diff = (mat2 - expected_mat)
    assert(np.all(mat_diff.todense() == pytest.approx(0)))

    sprsmat1 /= 2
    mat_diff = sprsmat1.to_scipy() - expected_mat
    assert(np.all(mat_diff.todense() == pytest.approx(0)))
