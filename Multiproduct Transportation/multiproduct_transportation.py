from gurobipy import Model, GRB
import gurobipy as gp


prob = Model("Multiproduct Transportation")

## input parameters

warehouse = ["w1", "w2"]
customer = [1, 2, 3]
product = ["A", "B", "C"]
trans_cost = {}
warehouse_cap = {}

cap = [50, 40, 60, 30, 50, 40]
cost_trans = [3, 4, 6, 2, 3, 5, 4, 2, 4, 5, 3, 4, 3, 2, 3, 2, 5, 2]
demand = [40, 30, 50, 20, 30, 20, 20, 30, 30]
customer_demand = {}

index = 0
for w in warehouse:
    for p in product:
        warehouse_cap[(w, p)] = cap[index]
        index += 1
#print(warehouse_cap)
index = 0
for w in warehouse:
    for c in customer:
        for p in product:
            trans_cost[(w, c, p)] = cost_trans[index]
            index += 1

index = 0
for c in customer:
    for p in product:
        customer_demand[(c, p)] = demand[index]
        index += 1


prod_qty = {
    (w, c, p): prob.addVar(name="x_{0}_{1}_{2}".format(w, c, p), vtype=GRB.CONTINUOUS)
    for w in warehouse
    for c in customer
    for p in product
}
#print(prod_qty)

obj = gp.quicksum(
    prod_qty[(w, c, p)] * trans_cost[(w, c, p)]
    for w in warehouse
    for c in customer
    for p in product
)

prob.setObjective(obj, sense=GRB.MINIMIZE)


## constraint

for c in customer:
    for p in product:
        prob.addConstr(
            gp.quicksum(prod_qty[(w, c, p)] for w in warehouse) == customer_demand[(c, p)]
        )


for w in warehouse:
    for p in product:
        prob.addConstr(
            gp.quicksum(prod_qty[(w, c, p)] for c in customer) <= warehouse_cap[(w,p)]
        )


prob.optimize()

for var in prob.getVars():
    print(f"{var} = {var.x:.2f}")

prob.write(r'C:\Users\ADMIN\Desktop\OR\lp\multitransportation.lp')
