#!/bin/bash

s="HVite -A -D -T 1"
#-i reco.mlf -w net.slf dict.txt hmmlist.txt

for i in "pasang" "alarm" "hapus" "nyalakan" "matikan" "pukul" "jam" "setengah" "seperempat" "kurang" "lebih" "nol" "satu" "dua" "tiga" "empat" "lima" "enam" "tujuh" "delapan" "sembilan" "sepuluh" "sebelas" "belas" "puluh" "sil"; do
	#echo "HInit -A -D -T 1 -S trainlist.txt -M model/hmm0 -H model/proto/$i -l $i -L data/train/lab/ model/proto/$i"
	#echo "HCompV -A -D -T 1 -S trainlist.txt -M model/hmm0flat -H model/proto/$i -f 0.01 model/proto/$i"
	# for j in {0..19}; do
	# 	k=$((j+1))
	# 	echo "HRest -A -D -T 1 -S trainlist.txt -M model/hmm$k -H model/hmm$j/$i -l $i -L data/train/lab/ model/hmm$j/$i"
	# done
	s="$s -H model/hmm20/$i"
done

s="$s -i reco.mlf -w net.slf dict.txt hmmlist.txt"
echo $s