import dimod
from dwave.system import LeapHybridSampler

sampler = LeapHybridSampler(solver={'category': 'hybrid'})
bqm = dimod.generators.ran_r(1, 300)
sampleset = sampler.sample(bqm)
sampleset.info     
{'qpu_access_time': 41990, 'charge_time': 2991424, 'run_time': 2991424}