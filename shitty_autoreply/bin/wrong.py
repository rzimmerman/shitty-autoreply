

def main():
    import sys
    from shitty_autoreply import wrong_name

    try:
        print wrong_name(sys.argv[1])
    except IndexError:
        print 'Supply a name.'
        return 1
