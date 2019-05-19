#!/usr/bin/python3


class Attribute:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __call__(self, world=None):
        if world is None:
            return self.val
        else:
            return True if world[self.name].val == self.val else False
    
    


class World:

    def __init__(self, base=None):
        props = {}
        if base is not None:
            for p in base.props:
                try:
                    getattr(base, p)
                    setattr(self, p)
                except AttributeError as e:
                    print("something went wrong: {}".format(e))


    def __getitem__(self, key):
        return self.props[key]

        

