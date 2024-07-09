# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _stag_internal
else:
    import _stag_internal

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

class TupleMM(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, arg2, arg3):
        _stag_internal.TupleMM_swiginit(self, _stag_internal.new_TupleMM(arg2, arg3))

    def get0(self):
        return _stag_internal.TupleMM_get0(self)

    def get1(self):
        return _stag_internal.TupleMM_get1(self)

    def set0(self, val):
        return _stag_internal.TupleMM_set0(self, val)

    def set1(self, val):
        return _stag_internal.TupleMM_set1(self, val)

    def __len__(self):
        return _stag_internal.TupleMM___len__(self)

    #[7]
    def __getitem__(self, n):
        if n >= len(self): raise IndexError()
        return getattr(self, 'get%d' % n)()
    def __setitem__(self, n, val):
        if n >= len(self): raise IndexError()
        getattr(self, 'set%d' % n)(val)

    __swig_destroy__ = _stag_internal.delete_TupleMM

# Register TupleMM in _stag_internal:
_stag_internal.TupleMM_swigregister(TupleMM)
class Tupleii(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, arg2, arg3):
        _stag_internal.Tupleii_swiginit(self, _stag_internal.new_Tupleii(arg2, arg3))

    def get0(self):
        return _stag_internal.Tupleii_get0(self)

    def get1(self):
        return _stag_internal.Tupleii_get1(self)

    def set0(self, val):
        return _stag_internal.Tupleii_set0(self, val)

    def set1(self, val):
        return _stag_internal.Tupleii_set1(self, val)

    def __len__(self):
        return _stag_internal.Tupleii___len__(self)

    #[7]
    def __getitem__(self, n):
        if n >= len(self): raise IndexError()
        return getattr(self, 'get%d' % n)()
    def __setitem__(self, n, val):
        if n >= len(self): raise IndexError()
        getattr(self, 'set%d' % n)(val)

    __swig_destroy__ = _stag_internal.delete_Tupleii

# Register Tupleii in _stag_internal:
_stag_internal.Tupleii_swigregister(Tupleii)
class TupleEigensystem(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, arg2, arg3):
        _stag_internal.TupleEigensystem_swiginit(self, _stag_internal.new_TupleEigensystem(arg2, arg3))

    def get0(self):
        return _stag_internal.TupleEigensystem_get0(self)

    def get1(self):
        return _stag_internal.TupleEigensystem_get1(self)

    def set0(self, val):
        return _stag_internal.TupleEigensystem_set0(self, val)

    def set1(self, val):
        return _stag_internal.TupleEigensystem_set1(self, val)

    def __len__(self):
        return _stag_internal.TupleEigensystem___len__(self)

    #[7]
    def __getitem__(self, n):
        if n >= len(self): raise IndexError()
        return getattr(self, 'get%d' % n)()
    def __setitem__(self, n, val):
        if n >= len(self): raise IndexError()
        getattr(self, 'set%d' % n)(val)

    __swig_destroy__ = _stag_internal.delete_TupleEigensystem

# Register TupleEigensystem in _stag_internal:
_stag_internal.TupleEigensystem_swigregister(TupleEigensystem)
class edge(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    v1 = property(_stag_internal.edge_v1_get, _stag_internal.edge_v1_set)
    v2 = property(_stag_internal.edge_v2_get, _stag_internal.edge_v2_set)
    weight = property(_stag_internal.edge_weight_get, _stag_internal.edge_weight_set)

    def __init__(self):
        _stag_internal.edge_swiginit(self, _stag_internal.new_edge())
    __swig_destroy__ = _stag_internal.delete_edge

# Register edge in _stag_internal:
_stag_internal.edge_swigregister(edge)
cvar = _stag_internal.cvar
VERSION_MAJOR = cvar.VERSION_MAJOR
VERSION_MINOR = cvar.VERSION_MINOR
VERSION_PATCH = cvar.VERSION_PATCH

class LocalGraph(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def degree(self, v):
        return _stag_internal.LocalGraph_degree(self, v)

    def degree_unweighted(self, v):
        return _stag_internal.LocalGraph_degree_unweighted(self, v)

    def neighbors(self, v):
        return _stag_internal.LocalGraph_neighbors(self, v)

    def neighbors_unweighted(self, v):
        return _stag_internal.LocalGraph_neighbors_unweighted(self, v)

    def degrees(self, vertices):
        return _stag_internal.LocalGraph_degrees(self, vertices)

    def degrees_unweighted(self, vertices):
        return _stag_internal.LocalGraph_degrees_unweighted(self, vertices)

    def vertex_exists(self, v):
        return _stag_internal.LocalGraph_vertex_exists(self, v)
    __swig_destroy__ = _stag_internal.delete_LocalGraph

    def __init__(self):
        if self.__class__ == LocalGraph:
            _self = None
        else:
            _self = self
        _stag_internal.LocalGraph_swiginit(self, _stag_internal.new_LocalGraph(_self, ))
    def __disown__(self):
        self.this.disown()
        _stag_internal.disown_LocalGraph(self)
        return weakref.proxy(self)

# Register LocalGraph in _stag_internal:
_stag_internal.LocalGraph_swigregister(LocalGraph)
class Graph(LocalGraph):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _stag_internal.Graph_swiginit(self, _stag_internal.new_Graph(*args))

    def adjacency(self):
        return _stag_internal.Graph_adjacency(self)

    def laplacian(self):
        return _stag_internal.Graph_laplacian(self)

    def normalised_laplacian(self):
        return _stag_internal.Graph_normalised_laplacian(self)

    def signless_laplacian(self):
        return _stag_internal.Graph_signless_laplacian(self)

    def normalised_signless_laplacian(self):
        return _stag_internal.Graph_normalised_signless_laplacian(self)

    def degree_matrix(self):
        return _stag_internal.Graph_degree_matrix(self)

    def inverse_degree_matrix(self):
        return _stag_internal.Graph_inverse_degree_matrix(self)

    def lazy_random_walk_matrix(self):
        return _stag_internal.Graph_lazy_random_walk_matrix(self)

    def total_volume(self):
        return _stag_internal.Graph_total_volume(self)

    def average_degree(self):
        return _stag_internal.Graph_average_degree(self)

    def number_of_vertices(self):
        return _stag_internal.Graph_number_of_vertices(self)

    def number_of_edges(self):
        return _stag_internal.Graph_number_of_edges(self)

    def add_edge(self, i, j, w):
        return _stag_internal.Graph_add_edge(self, i, j, w)

    def remove_edge(self, i, j):
        return _stag_internal.Graph_remove_edge(self, i, j)

    def has_self_loops(self):
        return _stag_internal.Graph_has_self_loops(self)

    def is_connected(self):
        return _stag_internal.Graph_is_connected(self)

    def subgraph(self, vertices):
        return _stag_internal.Graph_subgraph(self, vertices)

    def disjoint_union(self, other):
        return _stag_internal.Graph_disjoint_union(self, other)

    def degree(self, v):
        return _stag_internal.Graph_degree(self, v)

    def degree_unweighted(self, v):
        return _stag_internal.Graph_degree_unweighted(self, v)

    def neighbors(self, v):
        return _stag_internal.Graph_neighbors(self, v)

    def neighbors_unweighted(self, v):
        return _stag_internal.Graph_neighbors_unweighted(self, v)

    def degrees(self, vertices):
        return _stag_internal.Graph_degrees(self, vertices)

    def degrees_unweighted(self, vertices):
        return _stag_internal.Graph_degrees_unweighted(self, vertices)

    def vertex_exists(self, v):
        return _stag_internal.Graph_vertex_exists(self, v)
    __swig_destroy__ = _stag_internal.delete_Graph

    def __eq__(self, other):
        return _stag_internal.Graph___eq__(self, other)

# Register Graph in _stag_internal:
_stag_internal.Graph_swigregister(Graph)
class AdjacencyListLocalGraph(LocalGraph):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, filename):
        _stag_internal.AdjacencyListLocalGraph_swiginit(self, _stag_internal.new_AdjacencyListLocalGraph(filename))

    def degree(self, v):
        return _stag_internal.AdjacencyListLocalGraph_degree(self, v)

    def degree_unweighted(self, v):
        return _stag_internal.AdjacencyListLocalGraph_degree_unweighted(self, v)

    def neighbors(self, v):
        return _stag_internal.AdjacencyListLocalGraph_neighbors(self, v)

    def neighbors_unweighted(self, v):
        return _stag_internal.AdjacencyListLocalGraph_neighbors_unweighted(self, v)

    def degrees(self, vertices):
        return _stag_internal.AdjacencyListLocalGraph_degrees(self, vertices)

    def degrees_unweighted(self, vertices):
        return _stag_internal.AdjacencyListLocalGraph_degrees_unweighted(self, vertices)

    def vertex_exists(self, v):
        return _stag_internal.AdjacencyListLocalGraph_vertex_exists(self, v)
    __swig_destroy__ = _stag_internal.delete_AdjacencyListLocalGraph

# Register AdjacencyListLocalGraph in _stag_internal:
_stag_internal.AdjacencyListLocalGraph_swigregister(AdjacencyListLocalGraph)

def cycle_graph(n):
    return _stag_internal.cycle_graph(n)

def complete_graph(n):
    return _stag_internal.complete_graph(n)

def barbell_graph(n):
    return _stag_internal.barbell_graph(n)

def star_graph(n):
    return _stag_internal.star_graph(n)

def identity_graph(n):
    return _stag_internal.identity_graph(n)

def __eq__(*args):
    return _stag_internal.__eq__(*args)

def __ne__(*args):
    return _stag_internal.__ne__(*args)

def __add__(lhs, rhs):
    return _stag_internal.__add__(lhs, rhs)

def sprsMatValues(matrix):
    return _stag_internal.sprsMatValues(matrix)

def sprsMatInnerIndices(matrix):
    return _stag_internal.sprsMatInnerIndices(matrix)

def sprsMatOuterStarts(matrix):
    return _stag_internal.sprsMatOuterStarts(matrix)

def sprsMatToVec(*args):
    return _stag_internal.sprsMatToVec(*args)

def sprsMatFromVectors(column_starts, row_indices, values):
    return _stag_internal.sprsMatFromVectors(column_starts, row_indices, values)

def isSymmetric(matrix):
    return _stag_internal.isSymmetric(matrix)

def safeGetline(_is, t):
    return _stag_internal.safeGetline(_is, t)

def getTempFilename():
    return _stag_internal.getTempFilename()

def openTempFile(os):
    return _stag_internal.openTempFile(os)

def spectral_cluster(graph, k):
    return _stag_internal.spectral_cluster(graph, k)

def cheeger_cut(graph):
    return _stag_internal.cheeger_cut(graph)

def local_cluster(graph, seed_vertex, target_volume):
    return _stag_internal.local_cluster(graph, seed_vertex, target_volume)

def local_cluster_acl(*args):
    return _stag_internal.local_cluster_acl(*args)

def approximate_pagerank(graph, seed_vector, alpha, epsilon):
    return _stag_internal.approximate_pagerank(graph, seed_vector, alpha, epsilon)

def sweep_set_conductance(*args):
    return _stag_internal.sweep_set_conductance(*args)

def connected_component(g, v):
    return _stag_internal.connected_component(g, v)

def connected_components(g):
    return _stag_internal.connected_components(g)

def adjusted_rand_index(gt_labels, labels):
    return _stag_internal.adjusted_rand_index(gt_labels, labels)

def mutual_information(gt_labels, labels):
    return _stag_internal.mutual_information(gt_labels, labels)

def normalised_mutual_information(gt_labels, labels):
    return _stag_internal.normalised_mutual_information(gt_labels, labels)

def conductance(graph, cluster):
    return _stag_internal.conductance(graph, cluster)

def symmetric_difference(S, T):
    return _stag_internal.symmetric_difference(S, T)

def approximate_similarity_graph(data, a):
    return _stag_internal.approximate_similarity_graph(data, a)

def similarity_graph(data, a):
    return _stag_internal.similarity_graph(data, a)

def load_edgelist(filename):
    return _stag_internal.load_edgelist(filename)

def save_edgelist(graph, filename):
    return _stag_internal.save_edgelist(graph, filename)

def parse_adjacencylist_content_line(line):
    return _stag_internal.parse_adjacencylist_content_line(line)

def sort_edgelist(filename):
    return _stag_internal.sort_edgelist(filename)

def copy_edgelist_duplicate_edges(infile, outfile):
    return _stag_internal.copy_edgelist_duplicate_edges(infile, outfile)

def load_adjacencylist(filename):
    return _stag_internal.load_adjacencylist(filename)

def save_adjacencylist(graph, filename):
    return _stag_internal.save_adjacencylist(graph, filename)

def edgelist_to_adjacencylist(edgelist_fname, adjacencylist_fname):
    return _stag_internal.edgelist_to_adjacencylist(edgelist_fname, adjacencylist_fname)

def adjacencylist_to_edgelist(adjacencylist_fname, edgelist_fname):
    return _stag_internal.adjacencylist_to_edgelist(adjacencylist_fname, edgelist_fname)

def get_global_rng():
    return _stag_internal.get_global_rng()

def create_rng():
    return _stag_internal.create_rng()

def sbm(*args):
    return _stag_internal.sbm(*args)

def general_sbm(*args):
    return _stag_internal.general_sbm(*args)

def general_sbm_edgelist(*args):
    return _stag_internal.general_sbm_edgelist(*args)

def erdos_renyi(*args):
    return _stag_internal.erdos_renyi(*args)

def sbm_gt_labels(n, k):
    return _stag_internal.sbm_gt_labels(n, k)

def general_sbm_gt_labels(cluster_sizes):
    return _stag_internal.general_sbm_gt_labels(cluster_sizes)
Largest = _stag_internal.Largest
Smallest = _stag_internal.Smallest
Adjacency = _stag_internal.Adjacency
Laplacian = _stag_internal.Laplacian
NormalisedLaplacian = _stag_internal.NormalisedLaplacian

def compute_eigensystem(g, mat, num_eigs, which):
    return _stag_internal.compute_eigensystem(g, mat, num_eigs, which)

def compute_eigenvectors(g, mat, num_eigs, which):
    return _stag_internal.compute_eigenvectors(g, mat, num_eigs, which)

def compute_eigenvalues(g, mat, num_eigs, which):
    return _stag_internal.compute_eigenvalues(g, mat, num_eigs, which)

def power_method(*args):
    return _stag_internal.power_method(*args)

def rayleigh_quotient(mat, vec):
    return _stag_internal.rayleigh_quotient(mat, vec)
class DataPoint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _stag_internal.delete_DataPoint

    def __init__(self, *args):
        _stag_internal.DataPoint_swiginit(self, _stag_internal.new_DataPoint(*args))

    def to_vector(self):
        return _stag_internal.DataPoint_to_vector(self)
    dimension = property(_stag_internal.DataPoint_dimension_get, _stag_internal.DataPoint_dimension_set)
    coordinates = property(_stag_internal.DataPoint_coordinates_get, _stag_internal.DataPoint_coordinates_set)

# Register DataPoint in _stag_internal:
_stag_internal.DataPoint_swigregister(DataPoint)

def load_matrix(filename):
    return _stag_internal.load_matrix(filename)

def save_matrix(data, filename):
    return _stag_internal.save_matrix(data, filename)

def matrix_to_datapoints(data):
    return _stag_internal.matrix_to_datapoints(data)

def gaussian_kernel(*args):
    return _stag_internal.gaussian_kernel(*args)
class CKNSGaussianKDEHashUnit(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, a, data, log_nmu, j, K2_constant, prob_offset):
        _stag_internal.CKNSGaussianKDEHashUnit_swiginit(self, _stag_internal.new_CKNSGaussianKDEHashUnit(a, data, log_nmu, j, K2_constant, prob_offset))

    def query(self, q):
        return _stag_internal.CKNSGaussianKDEHashUnit_query(self, q)
    __swig_destroy__ = _stag_internal.delete_CKNSGaussianKDEHashUnit

# Register CKNSGaussianKDEHashUnit in _stag_internal:
_stag_internal.CKNSGaussianKDEHashUnit_swigregister(CKNSGaussianKDEHashUnit)
class CKNSGaussianKDE(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _stag_internal.CKNSGaussianKDE_swiginit(self, _stag_internal.new_CKNSGaussianKDE(*args))

    def query(self, *args):
        return _stag_internal.CKNSGaussianKDE_query(self, *args)
    __swig_destroy__ = _stag_internal.delete_CKNSGaussianKDE

# Register CKNSGaussianKDE in _stag_internal:
_stag_internal.CKNSGaussianKDE_swigregister(CKNSGaussianKDE)
class ExactGaussianKDE(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _stag_internal.ExactGaussianKDE_swiginit(self, _stag_internal.new_ExactGaussianKDE(*args))

    def query(self, *args):
        return _stag_internal.ExactGaussianKDE_query(self, *args)

    def sample_neighbors(self, q, degree, rs):
        return _stag_internal.ExactGaussianKDE_sample_neighbors(self, q, degree, rs)
    __swig_destroy__ = _stag_internal.delete_ExactGaussianKDE

# Register ExactGaussianKDE in _stag_internal:
_stag_internal.ExactGaussianKDE_swigregister(ExactGaussianKDE)
LSH_PARAMETER_W = _stag_internal.LSH_PARAMETER_W
class LSHFunction(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, dimension):
        _stag_internal.LSHFunction_swiginit(self, _stag_internal.new_LSHFunction(dimension))

    def apply(self, point):
        return _stag_internal.LSHFunction_apply(self, point)

    @staticmethod
    def collision_probability(distance):
        return _stag_internal.LSHFunction_collision_probability(distance)
    __swig_destroy__ = _stag_internal.delete_LSHFunction

# Register LSHFunction in _stag_internal:
_stag_internal.LSHFunction_swigregister(LSHFunction)
class MultiLSHFunction(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, dimension, num_functions):
        _stag_internal.MultiLSHFunction_swiginit(self, _stag_internal.new_MultiLSHFunction(dimension, num_functions))

    def apply(self, point):
        return _stag_internal.MultiLSHFunction_apply(self, point)
    __swig_destroy__ = _stag_internal.delete_MultiLSHFunction

# Register MultiLSHFunction in _stag_internal:
_stag_internal.MultiLSHFunction_swigregister(MultiLSHFunction)
class E2LSH(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _stag_internal.E2LSH_swiginit(self, _stag_internal.new_E2LSH(*args))

    def get_near_neighbors(self, query):
        return _stag_internal.E2LSH_get_near_neighbors(self, query)

    @staticmethod
    def collision_probability(*args):
        return _stag_internal.E2LSH_collision_probability(*args)
    __swig_destroy__ = _stag_internal.delete_E2LSH

# Register E2LSH in _stag_internal:
_stag_internal.E2LSH_swigregister(E2LSH)
EPSILON = _stag_internal.EPSILON
class DenseMat(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _stag_internal.delete_DenseMat

    def get_rows(self):
        return _stag_internal.DenseMat_get_rows(self)

    def get_cols(self):
        return _stag_internal.DenseMat_get_cols(self)

    def __add__(self, other):
        return _stag_internal.DenseMat___add__(self, other)

    def __sub__(self, other):
        return _stag_internal.DenseMat___sub__(self, other)

    def __mul__(self, other):
        return _stag_internal.DenseMat___mul__(self, other)

    def __mulfloat__(self, other):
        return _stag_internal.DenseMat___mulfloat__(self, other)

    def __mulint__(self, other):
        return _stag_internal.DenseMat___mulint__(self, other)

    def __neg__(self):
        return _stag_internal.DenseMat___neg__(self)

    def __truedivfloat__(self, other):
        return _stag_internal.DenseMat___truedivfloat__(self, other)

    def __truedivint__(self, other):
        return _stag_internal.DenseMat___truedivint__(self, other)

    def __transpose__(self):
        return _stag_internal.DenseMat___transpose__(self)

    def __init__(self):
        _stag_internal.DenseMat_swiginit(self, _stag_internal.new_DenseMat())

# Register DenseMat in _stag_internal:
_stag_internal.DenseMat_swigregister(DenseMat)
class SprsMat(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _stag_internal.delete_SprsMat

    def get_rows(self):
        return _stag_internal.SprsMat_get_rows(self)

    def get_cols(self):
        return _stag_internal.SprsMat_get_cols(self)

    def __add__(self, other):
        return _stag_internal.SprsMat___add__(self, other)

    def __sub__(self, other):
        return _stag_internal.SprsMat___sub__(self, other)

    def __mul__(self, other):
        return _stag_internal.SprsMat___mul__(self, other)

    def __mulfloat__(self, other):
        return _stag_internal.SprsMat___mulfloat__(self, other)

    def __mulint__(self, other):
        return _stag_internal.SprsMat___mulint__(self, other)

    def __neg__(self):
        return _stag_internal.SprsMat___neg__(self)

    def __truedivfloat__(self, other):
        return _stag_internal.SprsMat___truedivfloat__(self, other)

    def __truedivint__(self, other):
        return _stag_internal.SprsMat___truedivint__(self, other)

    def __transpose__(self):
        return _stag_internal.SprsMat___transpose__(self)

    def __init__(self):
        _stag_internal.SprsMat_swiginit(self, _stag_internal.new_SprsMat())

# Register SprsMat in _stag_internal:
_stag_internal.SprsMat_swigregister(SprsMat)

def sprsMatFromVectorsDims(rows, cols, column_starts, row_indices, values):
    return _stag_internal.sprsMatFromVectorsDims(rows, cols, column_starts, row_indices, values)

def denseMatFromNdarray(mat):
    return _stag_internal.denseMatFromNdarray(mat)

def ndArrayFromDenseMat(mat):
    return _stag_internal.ndArrayFromDenseMat(mat)
VERSION = _stag_internal.VERSION

