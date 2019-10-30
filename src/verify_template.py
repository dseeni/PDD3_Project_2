# # ----------------------------------------------------------------------------
# Project 1
# In this project our goal is to validate one dictionary structure against a
# template dictionary.
#
# A typical example of this might be working with JSON data inputs in an API.
# You are trying to validate this received JSON against some kind of template
# to make sure the received JSON conforms to that template (i.e. all the keys
# and structure are identical - value types being important, but not the value
# itself - so just the structure, and the data type of the values).
#
# To keep things simple we'll assume that values can be either single values
# (like an integer, string, etc), or a dictionary, itself only containing single
# values or other dictionaries, recursively. In other words, we're not going to
# deal with lists as possible values. Also, to keep things simple, we'll assume
# that all keys are required, and that no extra keys are permitted.
#
# In practice we would not have these simplifying assumptions, and although we
# could definitely write this ourselves, there are many 3rd party libraries that
# already exist to do this (such as jsonschema, marshmallow, and many more, some
# of which I'll cover lightly in some later videos.)
#
# For example you might have this template:
# # ----------------------------------------------------------------------------


from src.constants import *

# try set containtment < > <= >= etc with sets, using keys/item views?


def verify_dict(template, sample):
    if len(template.keys()) and len(sample.keys()) > 1:
        template_keys = {*template.keys()}
        sample_keys = {*sample.keys()}
    else:
        template_keys = template.keys()
        sample_keys = sample.keys()
    # at each depth level, check against extra keys
    try:
        assert len(template_keys) == len(sample_keys)
    except AssertionError as a:
        print('Unexpected Key(s) Found:', template_keys ^ sample_keys)
        raise a
    # if we have non dictionary keys present...(we're in the deepest branches)
    for key in template_keys:
        if isinstance(template[key], dict):
            verify_dict(template[key], sample[key])
        else:
            try:
                assert isinstance(sample[key], template[key])
            except AssertionError as a:
                print(sample.get(key), type(sample.get(key)), 'does not match',
                      template.get(key))
                raise a
    return True


print(verify_dict(template, rodney))
