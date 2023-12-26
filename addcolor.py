from matplotlib import colors
from matplotlib._color_data import BASE_COLORS, TABLEAU_COLORS, CSS4_COLORS, XKCD_COLORS
colors._colors_full_map = {}

class _ColorMapping(dict):
    def __init__(self, mapping):
        super().__init__(mapping)
        self.cache = {}

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.cache.clear()

    def __delitem__(self, key):
        super().__delitem__(key)
        self.cache.clear()

colors._colors_full_map = {}
# Set by reverse priority order.
colors._colors_full_map.update(XKCD_COLORS)
colors._colors_full_map.update({'add':'#121212'})
colors._colors_full_map.update({k.replace('grey', 'gray'): v
                         for k, v in XKCD_COLORS.items()
                         if 'grey' in k})
colors._colors_full_map.update(CSS4_COLORS)
colors._colors_full_map.update(TABLEAU_COLORS)
colors._colors_full_map.update({k.replace('gray', 'grey'): v
                         for k, v in TABLEAU_COLORS.items()
                         if 'gray' in k})
colors._colors_full_map.update(BASE_COLORS)
colors._colors_full_map = _ColorMapping(colors._colors_full_map)