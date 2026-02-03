from collections import defaultdict


# Source - https://stackoverflow.com/a/2912455
# Posted by Jochen Ritzel, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-03, License - CC BY-SA 3.0
class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret
