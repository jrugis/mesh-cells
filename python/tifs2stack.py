# -*- coding: utf-8 -*-################################################################################# 14.11.19# J.rugis################################################################################import stack_utils as sufrom skimage import io    ################################################################################ GLOBAL CONSTANTS###############################################################################IMAGE_STACK = '*.tif'STACK_OUT_FILE = 'stack.tif'################################################################################ MAIN PROGRAM###############################################################################A = su.get_tifs(IMAGE_STACK)io.imsave(STACK_OUT_FILE, A)###############################################################################