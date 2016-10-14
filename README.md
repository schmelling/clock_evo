[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/schmelling/clock_evo/issues)
[![Twitter](https://img.shields.io/badge/Tweet-@DerSchmelling-green.svg?style=social)](https://twitter.com/derschmelling)

## Evolution of circadian clocks using digital organisms

This repository contains all materials and resources related to this project.

#### Short project description

Within this project I'll try to elucidate the mechanisms underlying the evolution of circadian clocks. Circadian clocks are cellular mechanisms that anticipate the occurence of events and thus present an advantage to organisms, which contain such a timing mechanism. Since it is hard to study the fitness advantage in a laboratory setting, I'll work with digital organisms in the Avida software platform. Digital organisms have a great advantage over standard experimental setting, because it is easy to measure anything with arbitrary precision. For more information about the circadian clocks and digital organisms, please visit the [wiki](https://github.com/schmelling/clock_evo/wiki) of this GitHub repository. A detailed despription of the experimental set up can be found in the [roadmap](https://github.com/schmelling/clock_evo/blob/master/ROADMAP.md), and notes and orther thoughts relating my progress can be found in my [open lab notebook](https://github.com/schmelling/clock_evo/tree/master/open_notebook).

### How to contribute

If you are interested in contributing to the project, please read the [contribution instructions](https://github.com/schmelling/clock_evo/blob/master/CONTRIBUTING.md) first.

### Installation

#### Avida

All of the evolutionary experiments will be run in the Avida platform for digital evolution. For the installation, please read their installation instructions on their [GitHub repository](https://github.com/devosoft/avida). For Mac OS X and Windows, a binary installer is available on [devosoft.org](http://avida.devosoft.org).

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
