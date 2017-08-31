import pkg_resources

try:
    import lupa

    def from_lua(lua_code):
        """
        Use Lupa as a parser by actually running the code
        :param lua_code: the code to be executed
        :return:
        """

        fa_functions_path = pkg_resources.resource_filename('static', 'lua/fa_functions.lua')

        lua = lupa.LuaRuntime()
        # we don't care about all of the "internal" globals
        # especially not the ones that contain binary stuff
        # resulting in UnicodeDecodeError when we try to unfold them
        default_globals = dict(lua.globals()).keys()
        with open(fa_functions_path, 'r') as fp:
            lua.execute(fp.read())

        lua.execute(lua_code)

        def unfold_table(t):
            result = {}
            for k, v in t.items():
                if k not in default_globals:
                    if not lupa.lua_type(v):  # Already a python type
                        result[k] = v
                    elif lupa.lua_type(v) == 'table':
                        result[k] = dict(v)
            return result

        return unfold_table(lua.globals())

except ImportError as e:
    print("Ignoring lupa import error: %s" % e)
    lupa = None


    def from_lua(input):
        raise Exception("Can't parse lua code in this environment")
