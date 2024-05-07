#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/data
shared_models=$base/shared_models

# download preprocessed data
# client url curl -L location, -o output file, -C continue at (extraction destination)

curl -L https://files.ifi.uzh.ch/cl/archiv/2021/mt21/data.tar.gz -o $base/data.tar.gz
tar -xzvf $base/data.tar.gz -C $base

rm $base/data.tar.gz

# download shared models (which, in this case, is only the vocabulary)

curl -L https://files.ifi.uzh.ch/cl/archiv/2021/mt21/shared_models.tar.gz -o $base/shared_models.tar.gz
tar -xzvf $base/shared_models.tar.gz -C $base

rm $base/shared_models.tar.gz

# sizes
echo "Sizes of data files:"
wc -l $data/*

echo "Sizes of shared_model files:"
wc -l $shared_models/*

# sanity checks
echo "At this point, please make sure that 1) number of lines are as expected, 2) language suffixes are correct and 3) files are parallel"