def normalize(name):    
    return name[0].upper() + reduce(lambda l,c: l+c.lower(), name)[1:]
    # Regular way to do:
    # return name.lower().capitalize()

if __name__ == '__main__':
    L1 = ['adam', 'LISA', 'barT']
    print 'Imput:     ', L1
    print 'Normalized:', list(map(normalize, L1))
