# transfinite

`transfinite` introduces transfinite ordinals to Python. These ordinal objects interact naturally with Python's positive integers (finite ordinals) and support fundamental arithmetic operations. Ordinals are printed in LaTeX for easy reading. It's a useful tool for developing an intuition about the basics of infinite ordinals.

Work to `transfinite` is ongoing, meaning that features may be added or the interface may be changed. The simple core of the module should be preserved, however.

## Installation

Works with Python 3.2 and higher. Use of the Jupyter/IPython notebook/qtconsole is highly recommended so that LaTeX output is properly displayed.

To install, clone the repository (e.g. `git clone https://github.com/ajcr/transfinite.git`), navigate to the new directory and run `python setup.py install`.

## Usage

For a very basic introduction to ordinal arithmetic, look at the notebook [here](https://github.com/ajcr/transfinite/blob/master/notebooks/ordinal_arithmetic_basics.ipynb).

Here's a quick demonstration showing arithmetic with the first transfinite ordinal, omega (denoted as `w`):

![alt tag](https://github.com/ajcr/transfinite/blob/master/images/transfinite_demo.png)

## Future

To be implemented one day soon:

- The Veblen function and some larger countable ordinals.
- A method to visualise countable ordinals.

