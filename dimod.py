import dimod
x = dimod.Binary('x')
y = dimod.Integer('y')
cqm = dimod.CQM()
objective = cqm.set_objective(x+y)
cqm.add_constraint(y <= 3) 