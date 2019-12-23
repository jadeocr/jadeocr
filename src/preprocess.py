#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import h5py

import utils

# if len(sys.argv) != 3:
#     print('Usage: %s trn_dirpath tst_dirpath' % sys.argv[0])
#     sys.exit(1)
#
# trn_dirpath = sys.argv[1]
dirpath = "../model_input"

with h5py.File('input.hdf5', 'w') as f:
    for i in (dirpath):
        print('Converting \'%s\'...' % i)
        grp = f.create_group(i)
        dset_bitmap  = grp.create_dataset('bitmap',  (64, 64), dtype='uint8')

        for j, (bitmap) in enumerate(utils.read_gnt_in_directory(dirpath)):
            dset_bitmap[j]  = utils.normalize_bitmap(bitmap) #fixed?
