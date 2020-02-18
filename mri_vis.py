import logging
import numpy as np
import matplotlib.pyplot as plt

def display_slice_comparison(image1, image2, file_path, view):
    slice1 = get_slice(image1, view)
    slice2 = get_slice(image2, view)

    plt.subplot(1, 2, 1)
    plt.imshow(slice1, cmap="gray", aspect='auto') #, aspect=0.15
    plt.title('Image1')
    plt.subplot(1, 2, 2)
    plt.imshow(slice2, cmap="gray", aspect='auto') #, aspect=0.15
    plt.title('Image2')
    plt.suptitle(file_path)
    plt.show()

def get_slice(image3d, view, slice_ind=None):
    # Display slice for visual assistance
    view_dict = {
        'coronal': 0,
        'transverse': 1,
        'sagittal': 2
    }

    if slice_ind is None:
        n = image3d.shape[view_dict[view]]
        slice_ind = int((n - 1) / 2)

    if view is 'coronal':
        im_slice = image3d[slice_ind, :, :]
    elif view is 'transverse':
        im_slice = image3d[:, slice_ind, :]
    elif view is 'sagittal':
        im_slice = np.transpose(image3d[:, :, slice_ind])

    return im_slice

class IndexTracker(object):
    def __init__(self, ax, X, view):
        self.ax = ax
        ax.set_title('Use scroll wheel to navigate images')
        

        self.X = X
        self.view = view
        rows, cols, self.slices = X.shape
        self.ind = self.slices//2

        self.im = ax.imshow(get_slice(self.X, self.view, self.ind))
        self.update()

    def onscroll(self, event):
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()

    def update(self):
        self.im.set_data(get_slice(self.X, self.view, self.ind))
        self.ax.set_ylabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()

def display_slices(image3d, view):
    fig, ax = plt.subplots(1, 1)
    tracker = IndexTracker(ax, image3d, view)
    fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
    plt.show()