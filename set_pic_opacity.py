from PIL import ImageEnhance


def reduce_opacity(wm_pic, opacity):
    """Returns an image with reduced opacity."""
    assert opacity >= 0 and opacity <= 1
    if wm_pic.mode != 'RGBA':
        wm_pic = wm_pic.convert('RGBA')
    else:
        wm_pic = wm_pic.copy()
    alpha = wm_pic.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    wm_pic.putalpha(alpha)
    return wm_pic