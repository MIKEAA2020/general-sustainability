from .cli import selftest
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(selftest())
    print("usage: python3 -m viacert selftest")
    raise SystemExit(2)
