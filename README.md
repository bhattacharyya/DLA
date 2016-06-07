#        DLA
       Simulation of Diffusion Limited Aggregation
![0.2 stickiness](DLA_simulation.png?raw=true "DLA simulation example")

Run simulation with

```python run_simul.py -s [size of matrix] -k [stickiness or kappa] -n [number of particles]```

For resuming simulation from existing grid.txt file

```python run_simul_fromfile.py -s [size of matrix] -k [stickiness or kappa] -n [number of particles]```

Remember to input kappa in scientific notation e.g. 5e-2

Visualize simulation with 

```python status_GUI.py```

Guess the stickiness factor kappa with

```python analyze.py```

Please check the [wiki discussion page](https://github.com/bhattacharyya/DLA/wiki) for some results and the thinking behind the code
