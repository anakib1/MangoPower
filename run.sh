python "multiplier.py" &

powermetrics -i 500 -n 10 -o bin.txt --samplers cpu_power -a --hide-cpu-duty-cycle
python MangoPower.py