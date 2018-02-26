# pyjugex
Find a set of differentially expressed genes between two user defined volumes of interest based on JuBrain maps. The tool downloads expression values of user specified sets of genes from Allen Brain API. Then, it uses zscores to find which genes are expressed differentially between the user specified regions of interests. This tool is available as a Python package. 


## Dependencies
* numpy
* scipy
* statsmodels
* requests
* nibabel
* xmltodict

### Installation
```
git clone https://github.com/haimasree/pyjugex.git
cd pyjugex
pip install -r requirements.txt 
pip install .
```
### Usage
A typical usage is as follows -
```
from pyjugex import pyjugex
from pyjugex import hbp_human_atlas as atlas
genelist = ['ADRA2A', 'AVPR1B', 'CHRM2']
roi1 = atlas.jubrain.probability_map('FP1', atlas.MNI152)
roi2 = atlas.jubrain.probability_map('FP2', atlas.MNI152)
jugex = pyjugex.Analysis(gene_cache_dir='.pyjugex', verbose=True)
result = jugex.DifferentialAnalysis(genelist, roi1, roi2)
if len([id for id in result if result[id] < .05]) > 0:
    print('Differentially expressed genes/probes are : ')
    print([id for id in result if result[id] < .05])
else:
    print('There are no differentially expressed genes/probes in the given regions')
```

## Versioning
0.6

## Authors

* Big Data Analytics Group, INM-1, Research Center Juelich
## Acknowledgments

* Dr. Sebastian Bludau, Dr. Thomas Mühleisen
* Dr. Timo Dickscheid and other members of BDA-INM1 

