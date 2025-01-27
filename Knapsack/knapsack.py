from gurobipy import Model, GRB

# Data
items = range(5)  # Number of items
weights = [2, 3, 4, 5, 6]  # Weights of items
volumes = [3, 4, 5, 6, 7]  # Volumes of items
profits = [10, 15, 20, 25, 30]  # Profits of items
bag_capacity_weight = 10
bag_capacity_volume = 15
lending_cost = 5

# Model
m = Model("Knapsack with Priority on Own Bag")

# Decision variables
x = m.addVars(items, vtype=GRB.BINARY, name="x")  # Whether to include an item
y = m.addVar(vtype=GRB.BINARY, name="y")  # Whether to use an additional bag
z = m.addVars(items, vtype=GRB.BINARY, name="z")  # Items assigned to the additional bag

# Objective: Maximize profit minus cost for additional bag
m.setObjective(sum(profits[i] * x[i]for i in items) - lending_cost * y, GRB.MAXIMIZE)

# Constraints
# All items selected must either go into the own bag or additional bag
m.addConstrs(x[i] >= z[i] for i in items)  # If an item is in the additional bag, it must be selected
# Weight and volume constraints for the own bag
m.addConstr(sum(weights[i] * (x[i] - z[i]) for i in items) <= bag_capacity_weight, "OwnBagWeight")
m.addConstr(sum(volumes[i] * (x[i] - z[i]) for i in items) <= bag_capacity_volume, "OwnBagVolume")

# Weight and volume constraints for the additional bag
m.addConstr(sum(weights[i] * z[i] for i in items) <= y * bag_capacity_weight, "AddBagWeight")
m.addConstr(sum(volumes[i] * z[i] for i in items) <= y * bag_capacity_volume, "AddBagVolume")

# Additional bag can only be used if necessary
m.addConstr(y == 1, "UseAdditionalBag").Lazy = 1

# Optimize
m.optimize()

# Display results
if m.status == GRB.OPTIMAL:
    print("Selected items:")
    for i in items:
        if x[i].x > 0.5:
            print(f"Item {i} with weight {weights[i]} and volume {volumes[i]} {'(Additional bag)' if z[i].x > 0.5 else ''}")
    print(f"Additional bag used: {'Yes' if y.x > 0.5 else 'No'}")
    print(f"Total Profit: {m.objVal}")
else:
    print("No optimal solution found.")

"""
dict me (key are ith item) value of as value
"""
