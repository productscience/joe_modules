"""
Simple tools for blending colour
"""

def hex_to_rgb(col):
    """
    Accepts colors as css strings in the form #FFFFFF or FFFFFF and converts to [r,g,b]
    
    >>> print hex_to_rgb("#FFFFFF")
    [255, 255, 255]
    >>> print hex_to_rgb("808080")
    [128, 128, 128]
    """
    col = col.strip('#') + "000000"
    return [int(col[0:2],16),int(col[2:4],16),int(col[4:6],16)]


def rgb_to_hex(rgb, leader="#"):
    """
    Accepts rgb as a list [r,g,b] and returns css style color including #
    
    >>> print rgb_to_hex([255,255,255])
    #ffffff
    
    """
    return leader+"".join([hex(channel)[2:].zfill(2) for channel in rgb])


def blend(bg, fg, alpha):
    """
    Accepts all colours as css strings in the form #FFFFFF or FFFFFF.
    outputs a color in the same form.
    
    >>> print blend('#000000','#FFFFFF',0.5)
    #7f7f7f
    
    >>> print blend('8b0f84','8ffbff',.4)
    #8c6db5
    """
    bg = hex_to_rgb(bg)
    fg = hex_to_rgb(fg)
    
    #out = alpha * new + (1 - alpha) * old
    
    return rgb_to_hex([ int(alpha * new + (1.0 - alpha) * old) for old,new in zip(bg,fg) ])


#####################################################################################

if __name__ == "__main__":
    import doctest
    (errors,tests) = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if not errors:
        print "All %d tests passed okay." % (tests)
