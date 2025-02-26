import traceback
def opt_setter(d, key, value):
    if len(key) == 1:
        original_value = d.get(key[0])
        d[key[0]] = value
        print(f'Value {key[0]} set from {original_value} as {value}!')
        return
    return opt_setter(d[key[0]], key[1:], value)



def key_dealer(s):
    '''Insert s without opt_'''
    return s.split('__')


def extract_parser(unparsed, d):
    if unparsed == []:
        return
    assert unparsed[0][:2] == '--'
    try:
        value = eval(unparsed[1])
    except:
        value = str(unparsed[1])
    k = key_dealer(unparsed[0][2:])
    print(f'## Set opt {k} as {value}...')
    try:
        opt_setter(d, k, value)
    except:
        print(f'## Set opt {k} as {value} FAILED...')
        traceback.print_exc()
    return extract_parser(unparsed[2:], d)
