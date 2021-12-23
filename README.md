# HydrogenCloud

水素原子の電子雲を波動関数から計算する

## usage

```dosbatch
> \<exe path>\pconsole.exe \<repository path>\HydrogenCloud\produire\水素原子_位相.rdr <target function n, l, m (optional)> <sample size (optional)> <suggestion distribution width x, y, z (optional)> <initial value x, y, z (optional)> > <output file>
> python hydro_shower.py <output files>... <MCMC skip step>
> python hydro_shower_p.py <output file> <MCMC skip step>
```

例
```dosbatch: example
> \<exe path>\pconsole.exe \<repository path>\HydrogenCloud\produire\水素原子_位相.rdr 2 0 1 50000 > hydrogen_2p1.csv
> python hydro_shower_p.py hydrogen_2p1.csv 10
```
