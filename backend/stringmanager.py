
def string2hex(s):
    if s == None:
        return None
    result = ''
    for c in s:
        result = "%s%0.2X" % (result, ord(c))
    return result
        





