!# /bin/sh

mkdir data info neg pos pos_burned &&
chmod +x download_neg.sh &&
./download_neg.sh &&
python bg_descriptor.py &&
python sample_creator.py 128 24 24 &&
chmod +x sample_creator.sh &&
./sample_creator.sh &&
cd info &&
cat pos-*_burned.txt > positives.txt &&
cd .. &&
opencv_createsamples -info info/positives.txt -bg bg.txt -vec vectors.vec -num 1920 -w 24 -h 24 &&
opencv_traincascade -data data -vec vectors.vec -bg bg.txt -numPos 1700 -numNeg 900 -numStages 5 -precalcValBufSize 8192 -precalcIdxBufSize 8192 -featureType HAAR -minHitRate 0.995 -maxFalseAlarmRate 0.5 -w 24 -h 24 -acceptanceRatioBreakValue 10e-4
