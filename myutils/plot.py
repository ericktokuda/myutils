import matplotlib.pyplot as plt
import numpy as np


##########################################################
def export_all_axis(ax, fig, labels, outdir, pad=0.3, prefix='', fmt='pdf'):
    n = ax.shape[0]*ax.shape[1]
    for k in range(n):
        i = k // ax.shape[1]
        j = k  % ax.shape[1]
        ax[i, j].set_title('')

    for k in range(n):
        i = k // ax.shape[1]
        j = k  % ax.shape[1]
        coordsys = fig.dpi_scale_trans.inverted()
        extent = ax[i, j].get_window_extent().transformed(coordsys)
        x0, y0, x1, y1 = extent.extents

        if isinstance(pad, list):
            x0 -= pad[0]; y0 -= pad[1]; x1 += pad[2]; y1 += pad[3];
        else:
            x0 -= pad; y0 -= pad; x1 += pad; y1 += pad;

        bbox =  matplotlib.transforms.Bbox.from_extents(x0, y0, x1, y1)
        fig.savefig(pjoin(outdir, prefix + labels[k] + '.' + fmt),
                      bbox_inches=bbox)
                                                                                      
##########################################################
def hex2rgb(hexcolours, normalize=False, alpha=None):
    n = len(hexcolours)
    rgbcolours = np.zeros((n, 3), dtype=float)
    
    for i, h in enumerate(hexcolours):
        rgbcolours[i, :] = np.array([int(h.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)])

    if alpha != None:
        rgbcolours = np.concatenate([rgbcolours, np.ones((n, 1))*alpha], axis=1)

    if normalize:
        rgbcolours[:, :3] = rgbcolours[:, :3] / 255

    return rgbcolours