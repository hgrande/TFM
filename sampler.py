from dwave.system.samplers import DWaveSampler

sampler = DWaveSampler()   

print("Connected to sampler", sampler.solver.name)