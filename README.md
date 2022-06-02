# Spaces
Python portion of GRASP control

### Installation

Prerequisites:
- Anaconda
- Python >= 3.7

```bash
git clone git@github.com:ubcdsci/spaces.git
cd spaces
conda env create --file environment.yaml
conda activate spaces
```

If you would like to enable linting as a pre-commit hook, run:
```
pre-commit install
```

[Add pytorch to your conda environment](https://pytorch.org/get-started/locally/)

Be sure to select `Conda` as your package.
If you have a GPU that is CUDA-enabled, it's also recommended to install and use CUDA. Once that's done be sure to select the correct version to use with pytorch.


## Updating the Environment
 
In the case of an update that adds, removes, or updates packages, run:
```bash
conda env update --file environment.yaml
```
