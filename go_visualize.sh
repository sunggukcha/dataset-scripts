dataset='pascal'
origin_dir="../../datasets/VOCdevkit/VOC2012/JPEGImages"
prediction_dir="../../0.6261"
save_dir='./prd'

mkdir $save_dir
echo "mkdir $save_dir"

python visualize.py --dataset $dataset --original-dir $origin_dir --prediction-dir $prediction_dir --save-dir $save_dir

