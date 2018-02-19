#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hbp_human_atlas as atlas
import analysispyjugex
#import hbp_human_atlas_from_metadata

genelist = ['ADRA2A', 'AVPR1B', 'CHRM2', 'CNR1', 'CREB1', 'CRH', 'CRHR1', 'CRHR2', 'GAD2', 'HTR1A', 'HTR1B', 'HTR1D', 'HTR2A', 'HTR3A', 'HTR5A', 'MAOA', 'PDE1A', 'SLC6A2', 'SLC6A4', 'SST', 'TAC1', 'TPH1', 'GPR50', 'CUX2', 'TPH2']
#genelist = ['ADRA2A', 'AVPR1B', 'CHRM2']
roi1 = atlas.jubrain.probability_map('FP1', atlas.MNI152)
roi2 = atlas.jubrain.probability_map('FP2', atlas.MNI152)
jugex = analysispyjugex.Analysis(gene_cache_dir='.pyjugex', verbose=True)
#jugex = analysispyjugex.Analysis(gene_cache_dir='.pyjugex', single_probe_mode = True, verbose=True)
result = jugex.DifferentialAnalysis(genelist, roi1, roi2)
if len([id for id in result if result[id] < .05]) > 0:
    print('Differentially expressed genes/probes are : ')
    print([id for id in result if result[id] < .05])
else:
    print('There are no differentially expressed genes/probes in the given regions')
