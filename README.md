# SortedPie

This is the classical Algorithms Design (or Algorithms Complexity Analysis) course assignment where we have to implement widely known sorting algorithms and benchmark their running times for different types on inputs. This repository also contains the report that I had to write as part of the assignment (currently in Portugueese). I tried my best do to some reflection and point situations where each algorithm may fit better.

The idea on this assignment was to make it full-testable and reproducible. For the first you can simply run`python -m unittest` on the root folder, while for the latter you can execute the `run_all.sh` script to generate the benchmark data. Following you can run `assemble_data.py` to compile all `.csv` files generated on the previous step into a more meaningful file. If you run this script with the option `-g`, it'll generate all the trivial graphs (ie: the ones comparing sorted, partial sorted and unsorted entries) that I've used on the report. It's also possible to do experiments with each sorting algorithm individually. For more information use `python runner.py -h`.

*Notice:* The plotting script can be heavily improved as I tweaked it on the fly to generate different diagrams while writing the text (and ended up figuring that some trivial tasks might become a pain under `matplotlib` :()

## Running

This code is compatible with Python 3.x and can be executed without any external dependencies, unless if you want to generate the graphics. For that `matplotlib` is necessary.

# TODO
- Translate the report to English (this will likely take some time to happen);
- Move the graphs to this readme, or a discussion .md file, so you don't need to go to the full report;
- Comment on the reason for not using `numpy`.

© Luiz Felix, 2017