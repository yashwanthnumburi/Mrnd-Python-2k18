__author__ = 'Kalyan'

notes = '''
 Scopes and namespaces govern the accessibility rules and lifetime of python variables.

 Namespaces is a mapping of names to objects. Each python block creates a new namespace. The 3 main
 python blocks are modules (files), functions and classes.

 An object can have many names in the same namespace
 An object can have names in different namespaces.

 Scope is a textual area in which a variable can be directly accessible by its name.

 Variable which are bound (created) in a block are called local variables in that block
 Variables which are scoped to the the whole file (module) are called global
 Variables which are scoped to outer functions (in case of nested functions) are called non-local or free.
 
 Pre-lesson reading material: http://effbot.org/zone/python-objects.htm
'''

""""""
import inspect
import symtable

from placeholders import*

count = 10

#used to by pass any local shadow variables.
def get_global_count():
    return count

def test_scope_basic():
    local_names = get_locals(test_scope_basic)

    value = count

    assert True == ('value' in local_names)
    assert False== ('value' in global_names)

    assert True == ('count' in local_names)
    assert False == ('count' in global_names)

    assert 10 == value


def test_scope_undefined_variable():
    local_names = get_locals(test_scope_undefined_variable)

    try:
        my_name = name  #name variable is not in local or  global scope
    except  : # fill up the exception
        pass

    assert True == ('my_name' in local_names)
    assert False == ('name' in local_names)
    assert True == ('name' in global_names)

def test_variable_shadow():
    local_names = get_locals(test_variable_shadow)
    count = 20

    assert __ == ('count' in local_names)
    assert __ == ('count' in global_names)

    assert __ == count
    assert __ == get_global_count()

def test_global_write():
    local_names = get_locals(test_global_write)

    global count # declare that we want to use the read/write to global count
    count = 30

    try:
        assert __ == ('count' in local_names)
        assert __ == ('count' in global_names)

        assert __ == count
        assert __ == get_global_count()
    finally:
        count = 10 #reset to original value

def test_scope_is_bound_at_definition_time():
    local_names = get_locals(test_scope_is_bound_at_definition_time)

    assert __ == ('count' in local_names)
    assert __ == ('count' in global_names)

    try:
        value = count
        count = 30
    except __: # what happens when you read a variable before initializing it?
        #print ex #uncomment after you fill up above
        assert __
    finally:
        count = 20

    assert __ == count
    assert __ == get_global_count()


def test_scope_writing_globals():
    local_names = get_locals(test_scope_writing_globals)

    assert __ == ('count' in local_names)
    assert __ == ('count' in global_names)

    global count

    try:
        count = 40
        assert __ == count
        assert __ == get_global_count()
    finally:
        count = 10

    assert __ == get_global_count()

notes_2 = """
Read up on names and scopes sections here (skip the portion on classes for now):

http://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
https://docs.python.org/3/reference/executionmodel.html#naming
"""


three_things_i_learnt = """
-
-
-
"""

#helper functions which get the variables in locals and globals using the compiler's symbol tables.
def get_locals(func):
    source = inspect.getsource(func)
    top = symtable.symtable(source, "<string>", "exec")
    func = top.get_children()[0]  #since we are passing only the func code.
    return func.get_locals()

def get_globals():
    module = inspect.getmodule(get_globals)
    source = inspect.getsource(module)
    top = symtable.symtable(source, "<string>", "exec")
    return top.get_identifiers()

global_names = get_globals()