# In this kata you parse RGB colors represented by strings. The formats are primarily used in HTML and CSS. Your task is to implement a function which takes a color as a string and returns the parsed color as a map (see Examples).
#
# Input:
#
# The input string represents one of the following:
#
# 6-digit hexadecimal - "#RRGGBB"
# e.g. "#012345", "#789abc", "#FFA077"
# Each pair of digits represents a value of the channel in hexadecimal: 00 to FF
# 3-digit hexadecimal - "#RGB"
# e.g. "#012", "#aaa", "#F5A"
# Each digit represents a value 0 to F which translates to 2-digit hexadecimal: 0->00, 1->11, 2->22, and so on.
# Preset color name
# e.g. "red", "BLUE", "LimeGreen"
# You have to use the predefined map PRESET_COLORS (JavaScript, Python, Ruby), presetColors (Java, C#, Haskell), or preset-colors (Clojure). The keys are the names of preset colors in lower-case and the values are the corresponding colors in 6-digit hexadecimal (same as 1. "#RRGGBB").
# Examples:
#
# parse_html_color('#80FFA0')   # => {'r': 128, 'g': 255, 'b': 160}
# parse_html_color('#3B7')      # => {'r': 51,  'g': 187, 'b': 119}
# parse_html_color('LimeGreen') # => {'r': 50,  'g': 205, 'b': 50 }


class test:
    def assert_equals(a, b, c):
        print(a == b)


PRESET_COLORS = {'lightgrey': '#d3d3d3', 'darkolivegreen': '#556b2f', 'ghostwhite': '#f8f8ff', 'red': '#ff0000', 'darkviolet': '#9400d3', 'tomato': '#ff6347', 'palevioletred': '#db7093', 'lawngreen': '#7cfc00', 'sandybrown': '#f4a460', 'ivory': '#fffff0', 'slateblue': '#6a5acd', 'rebeccapurple': '#663399', 'saddlebrown': '#8b4513', 'olive': '#808000', 'oldlace': '#fdf5e6', 'mediumorchid': '#ba55d3', 'indigo': '#4b0082', 'skyblue': '#87ceeb', 'linen': '#faf0e6', 'salmon': '#fa8072', 'brown': '#a52a2a', 'blue': '#0000ff', 'papayawhip': '#ffefd5', 'darkslateblue': '#483d8b', 'lightseagreen': '#20b2aa', 'plum': '#dda0dd', 'limegreen': '#32cd32', 'green': '#008000', 'chocolate': '#d2691e', 'darkgreen': '#006400', 'lime': '#00ff00', 'deeppink': '#ff1493', 'snow': '#fffafa', 'darkgrey': '#a9a9a9', 'khaki': '#f0e68c', 'darkturquoise': '#00ced1', 'azure': '#f0ffff', 'maroon': '#800000', 'lightslategrey': '#778899', 'darkseagreen': '#8fbc8f', 'turquoise': '#40e0d0', 'midnightblue': '#191970', 'goldenrod': '#daa520', 'purple': '#800080', 'coral': '#ff7f50', 'white': '#ffffff', 'powderblue': '#b0e0e6', 'peru': '#cd853f', 'darkmagenta': '#8b008b', 'peachpuff': '#ffdab9', 'yellow': '#ffff00', 'mediumslateblue': '#7b68ee', 'steelblue': '#4682b4', 'darkorange': '#ff8c00', 'dimgray': '#696969', 'violet': '#ee82ee', 'slategrey': '#708090', 'firebrick': '#b22222', 'darkorchid': '#9932cc', 'lightyellow': '#ffffe0', 'slategray': '#708090', 'fuchsia': '#ff00ff', 'dimgrey': '#696969', 'cornflowerblue': '#6495ed', 'magenta': '#ff00ff', 'aliceblue': '#f0f8ff', 'honeydew': '#f0fff0', 'lightsteelblue': '#b0c4de', 'cornsilk': '#fff8dc', 'lightskyblue': '#87cefa', 'darkkhaki': '#bdb76b', 'aqua': '#00ffff', 'lightpink': '#ffb6c1', 'lightcoral': '#f08080', 'seagreen': '#2e8b57',
                 'mediumvioletred': '#c71585', 'grey': '#808080', 'springgreen': '#00ff7f', 'moccasin': '#ffe4b5', 'palegreen': '#98fb98', 'rosybrown': '#bc8f8f', 'blanchedalmond': '#ffebcd', 'whitesmoke': '#f5f5f5', 'darkslategray': '#2f4f4f', 'lightsalmon': '#ffa07a', 'teal': '#008080', 'bisque': '#ffe4c4', 'forestgreen': '#228b22', 'lightgray': '#d3d3d3', 'lavender': '#e6e6fa', 'sienna': '#a0522d', 'mintcream': '#f5fffa', 'wheat': '#f5deb3', 'orchid': '#da70d6', 'mediumseagreen': '#3cb371', 'lightcyan': '#e0ffff', 'lavenderblush': '#fff0f5', 'dodgerblue': '#1e90ff', 'indianred': '#cd5c5c', 'gray': '#808080', 'antiquewhite': '#faebd7', 'darkcyan': '#008b8b', 'cyan': '#00ffff', 'floralwhite': '#fffaf0', 'crimson': '#dc143c', 'burlywood': '#deb887', 'navajowhite': '#ffdead', 'darkblue': '#00008b', 'silver': '#c0c0c0', 'orange': '#ffa500', 'lightgoldenrodyellow': '#fafad2', 'tan': '#d2b48c', 'yellowgreen': '#9acd32', 'lightblue': '#add8e6', 'paleturquoise': '#afeeee', 'royalblue': '#4169e1', 'deepskyblue': '#00bfff', 'aquamarine': '#7fffd4', 'darkslategrey': '#2f4f4f', 'beige': '#f5f5dc', 'hotpink': '#ff69b4', 'navy': '#000080', 'mediumturquoise': '#48d1cc', 'lightgreen': '#90ee90', 'thistle': '#d8bfd8', 'olivedrab': '#6b8e23', 'darkgray': '#a9a9a9', 'blueviolet': '#8a2be2', 'darksalmon': '#e9967a', 'darkred': '#8b0000', 'cadetblue': '#5f9ea0', 'pink': '#ffc0cb', 'gainsboro': '#dcdcdc', 'mistyrose': '#ffe4e1', 'orangered': '#ff4500', 'mediumblue': '#0000cd', 'black': '#000000', 'lightslategray': '#778899', 'greenyellow': '#adff2f', 'seashell': '#fff5ee', 'darkgoldenrod': '#b8860b', 'mediumaquamarine': '#66cdaa', 'lemonchiffon': '#fffacd', 'gold': '#ffd700', 'palegoldenrod': '#eee8aa', 'mediumpurple': '#9370db', 'mediumspringgreen': '#00fa9a', 'chartreuse': '#7fff00'}


def parse_html_color(color):
    color = PRESET_COLORS.get(color.lower(), color)
    if 7 == len(color):
        r, g, b = (int(color[i:i + 2], 16) for i in range(1, 6, 2))
    else:
        r, g, b = (int(color[i] * 2, 16) for i in range(1, 4))
    return dict(zip("rgb", (r, g, b)))


# def parse_html_color(color):
#     color = PRESET_COLORS.get(color.lower(), color)
#     if len(color) == 7:
#         r, g, b = (int(color[i:i + 2], 16) for i in range(1, 7, 2))
#     else:
#         r, g, b = (int(color[i + 1] * 2, 16) for i in range(3))
#     return dict(zip("rgb", (r, g, b)))


def should_parse(color, expected):
    """Helper function to test the parse_html_color function.

    Arguments:
        color: the color string to parse
        expected: the expected result of parsing
    """
    message = 'color="{0}"'.format(color)
    try:
        actual = parse_html_color(color)
    except:
        print(message)
        raise
    else:
        test.assert_equals(actual, expected, message)


should_parse('#80FFA0',   {'r': 128, 'g': 255, 'b': 160})
should_parse('#3B7',      {'r': 51,  'g': 187, 'b': 119})
should_parse('LimeGreen', {'r': 50,  'g': 205, 'b': 50})
