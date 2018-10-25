'''
Python script to find the solution of the transportation problem given in
https://www.youtube.com/watch?v=WZIyL6pcItY
'''

import pulp

# Supplies
Supply_B, Supply_T = [300, 500]
# Demands
Demand1, Demand2, Demand3 = [200, 300, 250]
# Transportation costs
Tp_costs = [5, 6, 4, 6, 3, 7]

# Transportation problem formulation
Tp_prob = pulp.LpProblem("Transportation_Problem", pulp.LpMinimize)

# Decision variables
xB1 = pulp.LpVariable("xB1", lowBound=0, cat='Continuous')
xB2 = pulp.LpVariable("xB2", lowBound=0, cat='Continuous')
xB3 = pulp.LpVariable("xB3", lowBound=0, cat='Continuous')
xT1 = pulp.LpVariable("xT1", lowBound=0, cat='Continuous')
xT2 = pulp.LpVariable("xT2", lowBound=0, cat='Continuous')
xT3 = pulp.LpVariable("xT3", lowBound=0, cat='Continuous')

# Objective function to be minimized
Tp_prob += pulp.lpDot(Tp_costs, [xB1,xB2,xB3,xT1,xT2,xT3])

# Constraints
Tp_prob += xB1 + xB2 + xB3 <= Supply_B # Boston's supply
Tp_prob += xT1 + xT2 + xT3 <= Supply_T # Toronto's supply
Tp_prob += xB1 + xT1 == Demand1 # DC1's demand
Tp_prob += xB2 + xT2 == Demand2 # DC2's demand
Tp_prob += xB3 + xT3 == Demand3 # DC3's demand

# Solution
status = Tp_prob.solve()

# Printing results
print (pulp.LpStatus[status])
for var in [xB1,xB2,xB3]:
    print (str(var) + " = " + str(pulp.value(var)))
for var in [xT1,xT2,xT3]:
    print (str(var) + " = " + str(pulp.value(var)))
print("Total Costs = ", pulp.value(Tp_prob.objective))
