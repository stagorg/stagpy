# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

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
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
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

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _stag_internal.delete_SwigPyIterator

    def value(self):
        return _stag_internal.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _stag_internal.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _stag_internal.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _stag_internal.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _stag_internal.SwigPyIterator_equal(self, x)

    def copy(self):
        return _stag_internal.SwigPyIterator_copy(self)

    def next(self):
        return _stag_internal.SwigPyIterator_next(self)

    def __next__(self):
        return _stag_internal.SwigPyIterator___next__(self)

    def previous(self):
        return _stag_internal.SwigPyIterator_previous(self)

    def advance(self, n):
        return _stag_internal.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _stag_internal.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _stag_internal.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _stag_internal.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _stag_internal.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _stag_internal.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _stag_internal.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _stag_internal:
_stag_internal.SwigPyIterator_swigregister(SwigPyIterator)

class vectori(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _stag_internal.vectori_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _stag_internal.vectori___nonzero__(self)

    def __bool__(self):
        return _stag_internal.vectori___bool__(self)

    def __len__(self):
        return _stag_internal.vectori___len__(self)

    def __getslice__(self, i, j):
        return _stag_internal.vectori___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _stag_internal.vectori___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _stag_internal.vectori___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _stag_internal.vectori___delitem__(self, *args)

    def __getitem__(self, *args):
        return _stag_internal.vectori___getitem__(self, *args)

    def __setitem__(self, *args):
        return _stag_internal.vectori___setitem__(self, *args)

    def pop(self):
        return _stag_internal.vectori_pop(self)

    def append(self, x):
        return _stag_internal.vectori_append(self, x)

    def empty(self):
        return _stag_internal.vectori_empty(self)

    def size(self):
        return _stag_internal.vectori_size(self)

    def swap(self, v):
        return _stag_internal.vectori_swap(self, v)

    def begin(self):
        return _stag_internal.vectori_begin(self)

    def end(self):
        return _stag_internal.vectori_end(self)

    def rbegin(self):
        return _stag_internal.vectori_rbegin(self)

    def rend(self):
        return _stag_internal.vectori_rend(self)

    def clear(self):
        return _stag_internal.vectori_clear(self)

    def get_allocator(self):
        return _stag_internal.vectori_get_allocator(self)

    def pop_back(self):
        return _stag_internal.vectori_pop_back(self)

    def erase(self, *args):
        return _stag_internal.vectori_erase(self, *args)

    def __init__(self, *args):
        _stag_internal.vectori_swiginit(self, _stag_internal.new_vectori(*args))

    def push_back(self, x):
        return _stag_internal.vectori_push_back(self, x)

    def front(self):
        return _stag_internal.vectori_front(self)

    def back(self):
        return _stag_internal.vectori_back(self)

    def assign(self, n, x):
        return _stag_internal.vectori_assign(self, n, x)

    def resize(self, *args):
        return _stag_internal.vectori_resize(self, *args)

    def insert(self, *args):
        return _stag_internal.vectori_insert(self, *args)

    def reserve(self, n):
        return _stag_internal.vectori_reserve(self, n)

    def capacity(self):
        return _stag_internal.vectori_capacity(self)
    __swig_destroy__ = _stag_internal.delete_vectori

# Register vectori in _stag_internal:
_stag_internal.vectori_swigregister(vectori)

class vectorl(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _stag_internal.vectorl_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _stag_internal.vectorl___nonzero__(self)

    def __bool__(self):
        return _stag_internal.vectorl___bool__(self)

    def __len__(self):
        return _stag_internal.vectorl___len__(self)

    def __getslice__(self, i, j):
        return _stag_internal.vectorl___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _stag_internal.vectorl___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _stag_internal.vectorl___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _stag_internal.vectorl___delitem__(self, *args)

    def __getitem__(self, *args):
        return _stag_internal.vectorl___getitem__(self, *args)

    def __setitem__(self, *args):
        return _stag_internal.vectorl___setitem__(self, *args)

    def pop(self):
        return _stag_internal.vectorl_pop(self)

    def append(self, x):
        return _stag_internal.vectorl_append(self, x)

    def empty(self):
        return _stag_internal.vectorl_empty(self)

    def size(self):
        return _stag_internal.vectorl_size(self)

    def swap(self, v):
        return _stag_internal.vectorl_swap(self, v)

    def begin(self):
        return _stag_internal.vectorl_begin(self)

    def end(self):
        return _stag_internal.vectorl_end(self)

    def rbegin(self):
        return _stag_internal.vectorl_rbegin(self)

    def rend(self):
        return _stag_internal.vectorl_rend(self)

    def clear(self):
        return _stag_internal.vectorl_clear(self)

    def get_allocator(self):
        return _stag_internal.vectorl_get_allocator(self)

    def pop_back(self):
        return _stag_internal.vectorl_pop_back(self)

    def erase(self, *args):
        return _stag_internal.vectorl_erase(self, *args)

    def __init__(self, *args):
        _stag_internal.vectorl_swiginit(self, _stag_internal.new_vectorl(*args))

    def push_back(self, x):
        return _stag_internal.vectorl_push_back(self, x)

    def front(self):
        return _stag_internal.vectorl_front(self)

    def back(self):
        return _stag_internal.vectorl_back(self)

    def assign(self, n, x):
        return _stag_internal.vectorl_assign(self, n, x)

    def resize(self, *args):
        return _stag_internal.vectorl_resize(self, *args)

    def insert(self, *args):
        return _stag_internal.vectorl_insert(self, *args)

    def reserve(self, n):
        return _stag_internal.vectorl_reserve(self, n)

    def capacity(self):
        return _stag_internal.vectorl_capacity(self)
    __swig_destroy__ = _stag_internal.delete_vectorl

# Register vectorl in _stag_internal:
_stag_internal.vectorl_swigregister(vectorl)

class vectord(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _stag_internal.vectord_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _stag_internal.vectord___nonzero__(self)

    def __bool__(self):
        return _stag_internal.vectord___bool__(self)

    def __len__(self):
        return _stag_internal.vectord___len__(self)

    def __getslice__(self, i, j):
        return _stag_internal.vectord___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _stag_internal.vectord___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _stag_internal.vectord___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _stag_internal.vectord___delitem__(self, *args)

    def __getitem__(self, *args):
        return _stag_internal.vectord___getitem__(self, *args)

    def __setitem__(self, *args):
        return _stag_internal.vectord___setitem__(self, *args)

    def pop(self):
        return _stag_internal.vectord_pop(self)

    def append(self, x):
        return _stag_internal.vectord_append(self, x)

    def empty(self):
        return _stag_internal.vectord_empty(self)

    def size(self):
        return _stag_internal.vectord_size(self)

    def swap(self, v):
        return _stag_internal.vectord_swap(self, v)

    def begin(self):
        return _stag_internal.vectord_begin(self)

    def end(self):
        return _stag_internal.vectord_end(self)

    def rbegin(self):
        return _stag_internal.vectord_rbegin(self)

    def rend(self):
        return _stag_internal.vectord_rend(self)

    def clear(self):
        return _stag_internal.vectord_clear(self)

    def get_allocator(self):
        return _stag_internal.vectord_get_allocator(self)

    def pop_back(self):
        return _stag_internal.vectord_pop_back(self)

    def erase(self, *args):
        return _stag_internal.vectord_erase(self, *args)

    def __init__(self, *args):
        _stag_internal.vectord_swiginit(self, _stag_internal.new_vectord(*args))

    def push_back(self, x):
        return _stag_internal.vectord_push_back(self, x)

    def front(self):
        return _stag_internal.vectord_front(self)

    def back(self):
        return _stag_internal.vectord_back(self)

    def assign(self, n, x):
        return _stag_internal.vectord_assign(self, n, x)

    def resize(self, *args):
        return _stag_internal.vectord_resize(self, *args)

    def insert(self, *args):
        return _stag_internal.vectord_insert(self, *args)

    def reserve(self, n):
        return _stag_internal.vectord_reserve(self, n)

    def capacity(self):
        return _stag_internal.vectord_capacity(self)
    __swig_destroy__ = _stag_internal.delete_vectord

# Register vectord in _stag_internal:
_stag_internal.vectord_swigregister(vectord)

class vectore(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _stag_internal.vectore_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _stag_internal.vectore___nonzero__(self)

    def __bool__(self):
        return _stag_internal.vectore___bool__(self)

    def __len__(self):
        return _stag_internal.vectore___len__(self)

    def __getslice__(self, i, j):
        return _stag_internal.vectore___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _stag_internal.vectore___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _stag_internal.vectore___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _stag_internal.vectore___delitem__(self, *args)

    def __getitem__(self, *args):
        return _stag_internal.vectore___getitem__(self, *args)

    def __setitem__(self, *args):
        return _stag_internal.vectore___setitem__(self, *args)

    def pop(self):
        return _stag_internal.vectore_pop(self)

    def append(self, x):
        return _stag_internal.vectore_append(self, x)

    def empty(self):
        return _stag_internal.vectore_empty(self)

    def size(self):
        return _stag_internal.vectore_size(self)

    def swap(self, v):
        return _stag_internal.vectore_swap(self, v)

    def begin(self):
        return _stag_internal.vectore_begin(self)

    def end(self):
        return _stag_internal.vectore_end(self)

    def rbegin(self):
        return _stag_internal.vectore_rbegin(self)

    def rend(self):
        return _stag_internal.vectore_rend(self)

    def clear(self):
        return _stag_internal.vectore_clear(self)

    def get_allocator(self):
        return _stag_internal.vectore_get_allocator(self)

    def pop_back(self):
        return _stag_internal.vectore_pop_back(self)

    def erase(self, *args):
        return _stag_internal.vectore_erase(self, *args)

    def __init__(self, *args):
        _stag_internal.vectore_swiginit(self, _stag_internal.new_vectore(*args))

    def push_back(self, x):
        return _stag_internal.vectore_push_back(self, x)

    def front(self):
        return _stag_internal.vectore_front(self)

    def back(self):
        return _stag_internal.vectore_back(self)

    def assign(self, n, x):
        return _stag_internal.vectore_assign(self, n, x)

    def resize(self, *args):
        return _stag_internal.vectore_resize(self, *args)

    def insert(self, *args):
        return _stag_internal.vectore_insert(self, *args)

    def reserve(self, n):
        return _stag_internal.vectore_reserve(self, n)

    def capacity(self):
        return _stag_internal.vectore_capacity(self)
    __swig_destroy__ = _stag_internal.delete_vectore

# Register vectore in _stag_internal:
_stag_internal.vectore_swigregister(vectore)

class vectorvecl(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _stag_internal.vectorvecl_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _stag_internal.vectorvecl___nonzero__(self)

    def __bool__(self):
        return _stag_internal.vectorvecl___bool__(self)

    def __len__(self):
        return _stag_internal.vectorvecl___len__(self)

    def __getslice__(self, i, j):
        return _stag_internal.vectorvecl___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _stag_internal.vectorvecl___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _stag_internal.vectorvecl___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _stag_internal.vectorvecl___delitem__(self, *args)

    def __getitem__(self, *args):
        return _stag_internal.vectorvecl___getitem__(self, *args)

    def __setitem__(self, *args):
        return _stag_internal.vectorvecl___setitem__(self, *args)

    def pop(self):
        return _stag_internal.vectorvecl_pop(self)

    def append(self, x):
        return _stag_internal.vectorvecl_append(self, x)

    def empty(self):
        return _stag_internal.vectorvecl_empty(self)

    def size(self):
        return _stag_internal.vectorvecl_size(self)

    def swap(self, v):
        return _stag_internal.vectorvecl_swap(self, v)

    def begin(self):
        return _stag_internal.vectorvecl_begin(self)

    def end(self):
        return _stag_internal.vectorvecl_end(self)

    def rbegin(self):
        return _stag_internal.vectorvecl_rbegin(self)

    def rend(self):
        return _stag_internal.vectorvecl_rend(self)

    def clear(self):
        return _stag_internal.vectorvecl_clear(self)

    def get_allocator(self):
        return _stag_internal.vectorvecl_get_allocator(self)

    def pop_back(self):
        return _stag_internal.vectorvecl_pop_back(self)

    def erase(self, *args):
        return _stag_internal.vectorvecl_erase(self, *args)

    def __init__(self, *args):
        _stag_internal.vectorvecl_swiginit(self, _stag_internal.new_vectorvecl(*args))

    def push_back(self, x):
        return _stag_internal.vectorvecl_push_back(self, x)

    def front(self):
        return _stag_internal.vectorvecl_front(self)

    def back(self):
        return _stag_internal.vectorvecl_back(self)

    def assign(self, n, x):
        return _stag_internal.vectorvecl_assign(self, n, x)

    def resize(self, *args):
        return _stag_internal.vectorvecl_resize(self, *args)

    def insert(self, *args):
        return _stag_internal.vectorvecl_insert(self, *args)

    def reserve(self, n):
        return _stag_internal.vectorvecl_reserve(self, n)

    def capacity(self):
        return _stag_internal.vectorvecl_capacity(self)
    __swig_destroy__ = _stag_internal.delete_vectorvecl

# Register vectorvecl in _stag_internal:
_stag_internal.vectorvecl_swigregister(vectorvecl)

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

EPSILON = _stag_internal.EPSILON
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

def compute_eigensystem(*args):
    return _stag_internal.compute_eigensystem(*args)

def compute_eigenvalues(*args):
    return _stag_internal.compute_eigenvalues(*args)

def compute_eigenvectors(*args):
    return _stag_internal.compute_eigenvectors(*args)

def power_method(*args):
    return _stag_internal.power_method(*args)

def rayleigh_quotient(mat, vec):
    return _stag_internal.rayleigh_quotient(mat, vec)
class SprsMat(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _stag_internal.delete_SprsMat

    def __add__(self, other):
        return _stag_internal.SprsMat___add__(self, other)

    def __sub__(self, other):
        return _stag_internal.SprsMat___sub__(self, other)

    def __mul__(self, *args):
        return _stag_internal.SprsMat___mul__(self, *args)

    def __neg__(self):
        return _stag_internal.SprsMat___neg__(self)

    def __init__(self):
        _stag_internal.SprsMat_swiginit(self, _stag_internal.new_SprsMat())

# Register SprsMat in _stag_internal:
_stag_internal.SprsMat_swigregister(SprsMat)

VERSION = _stag_internal.VERSION


