# nlp

## Author

- Hutan Mihai Alexandru
- Github: [hutanmihai](https://github.com/hutanmihai)
- LinkedIn: [Mihai-Alexandru Hutan](https://www.linkedin.com/in/hutanmihai/)
- Portfolio: [mihaihutan.ro](https://mihaihutan.ro)

## How to run the project

### 1. Install required libraries using conda and pip

This is the recommended way of installing the required libraries.
You can also not use conda and install the libraries using pip, but you will have to make sure that you have the correct
version of python installed (3.11.5).

- Create environment

```bash
conda create --name nlp python=3.11.8
conda activate nlp
```

- Install the required libraries

```bash
pip install jupyter numpy
```

- Install pytorch

```bash
# If you have a CUDA enabled GPU (Windows)
pip install torch torchvision--index-url https://download.pytorch.org/whl/cu121

# If you have a CUDA enabled GPU (Linux)
pip install torch torchvision

# If you have MacOS (CPU) / Windows (CPU)
pip install torch torchvisio
```

### 2. Set the PYTHONPATH

Make sure you are in the root directory of the project.

- Windows - Powershell:

```bash
$env:PYTHONPATH='.'
```

- Windows - CMD:

```bash
set PYTHONPATH=.
```

- Linux / MacOS:

```bash
export PYTHONPATH=.
```
