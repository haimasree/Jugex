#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Inpython2
import nibabel as nib
import requests
import tempfile
import os

dictionaryimages = {}

dictionaryimages['FP1'] = 'https://hbp-unic.fz-juelich.de:7112/UFTP/rest/access/JUDAC/2f054eee-7fa5-4ed3-b046-2ddc1315fe9c/ba10m_l_N10_nlin2Stdicbm152casym.nii.gz'
dictionaryimages['FP2'] = 'https://hbp-unic.fz-juelich.de:7112/UFTP/rest/access/JUDAC/2f054eee-7fa5-4ed3-b046-2ddc1315fe9c/ba10p_l_N10_nlin2Stdicbm152casym.nii.gz'
#dictionaryimages['FP1'] = 'http://neuroglancer.humanbrainproject.org/precomputed/JuBrain/v2.2c/PMaps/FrontalPole_Fp1.nii'
#dictionaryimages['FP2'] = 'http://neuroglancer.humanbrainproject.org/precomputed/JuBrain/v2.2c/PMaps/FrontalPole_Fp2.nii'
MNI152 = True

class jubrain:        
    @classmethod
    def probability_map(cls, regionname, coordspace):
        if coordspace is False:
            raise ValueError('Only MNI152 template space is supported')
        if regionname not in dictionaryimages:
            raise ValueError(regionname+' is not present in the database')
        url = dictionaryimages[regionname]
        last = url.split('.')[-1]
        try:
            r = requests.get(url, verify=False)
        except requests.HTTPError as e:
            print(e)
            raise
        if last not in ('nii', 'gz'):
            raise OSError('Not an acceptable file format for rois')
        fp, fp_name = tempfile.mkstemp(suffix='.'+last if last == 'nii' else '.nii.'+last)
        os.write(fp, r.content)
        img_array = nib.load(fp_name)
        os.close(fp)
        return {'name':regionname, 'data':img_array}

