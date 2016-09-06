[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/schmelling/clock_evo/issues)
[![Twitter](https://img.shields.io/badge/Tweet-@DerSchmelling-green.svg?style=social)](https://twitter.com/derschmelling)

## Evolution of circadian clocks using digital organisms [under construction]

This repository contains all materials and resources related to this project.

#### Short project description

Add some text here please.

### How to contribute

If you are interested in contributing to the project, please read the [contribution instructions](https://github.com/schmelling/clock_evo/blob/master/CONTRIBUTING.md) first.

### Installation

#### AVIDA

All of the evolutionary experiments will be run in the AVIDA platform for digital evolution. For the installation, please read their installation instructions on their [GitHub repository](https://github.com/devosoft/avida). For Mac OS X and Windows, a binary installer is available on [devosoft.org](http://avida.devosoft.org).

Alternatively, you can run AVIDA inside of a [docker container](https://www.docker.com/what-docker). To do this, download and install [docker](https://www.docker.com/products/overview) and run:

```bash
$ docker pull bigscience/avida
```

#### Python

This project uses Python and the following packages:

Python version 3.5  
`ipython` with notebook support: [ipython.org](http://ipython.org)  
`numpy`: [numpy.org](http://www.numpy.org)  
`scipy`: [scipy.org](http://www.scipy.org)  
`matplotlib`: [matplotlib.org](http://matplotlib.org)    
`seaborn`: [seaborn](https://stanford.edu/~mwaskom/software/seaborn/)

The easiest way to get these is to use the [conda](https://www.continuum.io/why-anaconda) environment manager. I suggest downloading and installing [miniconda](http://conda.pydata.org/miniconda.html).

Once this is installed, the following command will install all required packages in your Python environment:

```bash
$ conda install -y numpy scipy matplotlib scikit-learn ipython-notebook seaborn
```

Alternatively, you can download and install the (very large) Anaconda software distribution, found at [https://store.continuum.io/downloads](https://www.continuum.io/downloads).

### License

The project is released under the CC0 license. You can find more information [here](https://github.com/schmelling/clock_evo/blob/master/LICENSE.md).
