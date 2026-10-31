# Modeling Trust in AI Systems

This Math 60 final project uses Monte Carlo simulation to model how a person's
trust in an AI system changes over repeated interactions.

Each AI response produces one of three trust updates:

- **Confident and correct:** trust increases.
- **Confident and wrong:** trust decreases.
- **Uncertain:** trust changes by a small random amount.

Trust is kept between 0 (no trust) and 1 (complete trust).

## Project files

- `Individual_Simulation.py` simulates one person's trust over time.
- `Percent_Dist.py` compares trust across 1,000 simulated people.
- `CC_increase.py` implements the confident-and-correct update.
- `CW_decrease.py` implements the confident-and-wrong update.
- `Uncertain_move.py` implements random fluctuation after an uncertain answer.

## Run the project

Install the required packages:

```powershell
python -m pip install numpy matplotlib
```

Run one individual simulation:

```powershell
python Individual_Simulation.py
```

Run the population comparison and generate the plots:

```powershell
python Percent_Dist.py
```

Because the simulations use random samples, the numerical results may differ
slightly each time the programs are run.
