#! /bin/sh

cd neg
wget -nd -r -A "neg-0*.jpg" http://haar.thiagohersan.com/haartraining/negatives/ &&
wget -nd -r -A "neg-1*.jpg" http://haar.thiagohersan.com/haartraining/negatives/ &&
cd ..
