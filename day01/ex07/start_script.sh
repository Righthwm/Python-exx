#!/bin/bash

python3 ../ex06/stres_test.py >> output1.txt &
python3 ../ex06/stres_test.py > output2.txt &
python3 ../ex06/stres_test.py > std_out_err.txt 2>&1 &
python3 ../ex06/stres_test.py >&1 2>>str_err_four.txt &
