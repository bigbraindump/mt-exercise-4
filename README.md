# MT Exercise 4: Layer Normalization for Transformer Models

This repo is a collection of scripts showing how to install [JoeyNMT](https://github.com/joeynmt/joeynmt), download
data and train & evaluate models, as well as the necessary data for training your own model

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3.10 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

Clone this repository or your fork thereof in the desired place:

    git clone https://github.com/moritz-steiner/mt-exercise-4

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Make sure to install the exact software versions specified in the the exercise sheet before continuing.

Download Moses for post-processing:

    ./scripts/download_install_packages.sh


Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved. It is also possible to continue training from there later on.

Training pre- and post- normalisation:

Edit the .configs/.yaml files to include pre/post normalisation techniques.
Run the train.sh script for the respective normalisation instance. 

Example (pre-normalisation): ./scripts/train.sh

# Training comparisons

A line plot comparison for pre- and post- normalisation training was conducted against the baseline.log file. 
The pre- and normalisation training, output '*.logs', and logs_table.py files were shared and collaborated on from user kmanaa.
In addition please *note* that the post-normalisation training was completed on the UZH cluster from user stariq after training on the local CPU failed multiple times, the log files were subsequently copied to the current repository.

# Generating perplexity logs linechart

Usage: python3 linechart.py

# Changes for Windows compatibility

-edited make_virtualenv.sh to use absolute python PATH, python3 was not recognized despite having python 3.10 installed
-edited virtual env activation command for windows system, source $base/venvs/torch3/Scripts/activate"
-edited download scripts, wget to curl

# AI use

OpenAI ChatGPT used for debugging, specifically while editing the plots.py file.