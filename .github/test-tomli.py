HAVE_TOMLLIB = True
try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        HAVE_TOMLLIB = False

if not HAVE_TOMLLIB:
    raise Exception("Not found tomli")
else:
    print("Tomli found, no problem")
