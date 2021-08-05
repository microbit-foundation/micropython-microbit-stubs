# Script to dump symbols from a micro:bit (V2).
# The list is used to check the completeness of the type stubs.
# Largely the same as https://github.com/microbit-foundation/python-editor/blob/master/micropython/microbit-api-instropection.py

modules = [
    # Added by Matt. We also need stubs for the u-prefixed versions noted below.
    "antigravity",
    "builtins",
    "love",
    "this",
    "errno",  # uerrno
    "array",  # uarray
    "audio",
    "collections",  # ucollections
    "gc",
    "machine",
    "math",
    "microbit",
    "micropython",
    "music",
    "neopixel",
    "os",  # oddly, no uos
    "radio",
    "random",  # urandom
    "speech",
    "struct",  # ustruct
    "sys",  # usys
    "time",  # utime
]


def nested_print(d, indent=0):
    for key in sorted(d.keys()):
        value = d[key]
        print("{}{}".format("\t" * indent, key))
        new_inden = indent + 1
        if isinstance(value, dict):
            nested_print(value, new_inden)
        elif value:
            print("{}{}".format("\t" * new_inden, value))


def autocomplete_print(d, indent=0):
    # Do we have more dicts inside?
    nested_dict = False
    for value in d.values():
        if value:
            nested_dict = True
    if not nested_dict:
        # Just print as a list in a single line
        print(repr(sorted(list(d.keys()))).replace("'", '"'), sep=", ", end=",\n")
    else:
        # At least one entry is a dictionary, so the others have value "[]"
        print("{{\n".format(), end="")
        for key, value in sorted(d.items()):
            new_indent = indent + 1
            if isinstance(value, dict):
                print('{}"{}": '.format("\t" * new_indent, key), end="")
                autocomplete_print(value, new_indent)
            else:
                # We expect all non dictionaries to be None or falsy
                print('{}"{}": "",'.format("\t" * new_indent, key))
        print("\n{}}},".format("\t" * indent))


def get_api(module, module_import_str):
    children = dir(module)
    # print('\n{}'.format(module_import_str))
    # print('\t{}'.format(module))
    # print('\t{}'.format(children))
    api_dict = {}
    for child_str in children:
        # print(gc.mem_free())
        import gc

        gc.collect()
        full_import_str = "{}.{}".format(module_import_str, child_str)
        child = eval(full_import_str)
        # Ignore all dunder methods and attributes
        if child_str.startswith("_"):
            pass
        # Avoid infinite loops if child is parent or an instance of the parent
        elif repr(module).startswith("<class ") and isinstance(child, module):
            api_dict[child_str] = None
        elif module == child:
            pass
        # Stop at functions and basic types
        elif (
            repr(child) in ("<function>", "<bound_method>")
            or isinstance(child, list)
            or isinstance(child, tuple)
            or isinstance(child, str)
            or isinstance(child, int)
        ):
            api_dict[child_str] = None
        else:
            # Anything else (classes, modules) has children for introspection
            gc.collect()
            api_dict[child_str] = get_api(child, full_import_str)
            gc.collect()
    return api_dict


def main():
    # We have more memory in V2 so we'll store all the API dictionary in memory
    # and print in multiple formats
    op = {}
    for module_name in modules:
        exec("import {}".format(module_name))
        op[module_name] = get_api(eval(module_name), module_name)
        exec("del {}".format(module_name))
        import gc

        gc.collect()
    # nested_print(op)


main()
