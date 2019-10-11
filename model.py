# -*- coding: utf-8 -*-
import pyomo.environ as pyomo
from pyomo.opt import SolverFactory


def optimize(data, config):
    # model
    model = pyomo.ConcreteModel()

    # parameters
    shippingcost = {x['seller']: x['shippingcost'] for x in data}
    distance = {x['seller']: x['distance'] for x in data}
    ordercount = {x['seller']: x['ordercount'] for x in data}

    # define sets
    I = list(set(x['product'] for x in data))
    J = list(set(x['seller'] for x in data))
    IJ = [(x['product'], x['seller']) for x in data]

    # decision vaiables
    model.x = pyomo.Var(IJ, domain=pyomo.Integers, bounds=(0, 1), doc='trans')
    model.y = pyomo.Var(J, domain=pyomo.Integers, bounds=(0, 1), doc='sellertrans')

    # constraints
    model.cons = pyomo.ConstraintList(doc='constraints')
    # transport to all demand
    for i in I:
        model.cons.add(sum([model.x[ij] for ij in model.x if ij[0] == i]) == 1)
    # seller transportation constraints
    maxtrans = len(IJ)
    for j in J:
        model.cons.add(sum([model.x[ij] for ij in model.x if ij[1] == j]) <= model.y[j] * maxtrans)

    # objective function
    shippingcost_penalty = 0 if sum(shippingcost.values()) == 0 \
        else 1000000000 * (sum(model.y[j] * shippingcost[j] for j in J) / sum(shippingcost.values()))
    sellertotal_penalty = 0 if len(J) == 0 \
        else 1000000 * (sum(model.y[j] for j in J) / len(J))
    distance_penalty = 0 if sum(distance.values()) == 0 \
        else 1000 * (sum(model.y[j] * distance[j] for j in J) / sum(distance.values()))
    ordercount_penalty = 0 if sum(ordercount.values()) == 0 \
        else 1 * (sum(model.y[j] * ordercount[j] for j in J) / sum(ordercount.values()))
    model.obj = pyomo.Objective(expr = shippingcost_penalty + sellertotal_penalty + distance_penalty + ordercount_penalty, 
                                sense = pyomo.minimize)

    # solve
    if config['app']['solver_path'] == "None":
        s = SolverFactory(config['app']['solver'])
    else:
        s = SolverFactory(config['app']['solver'], executable=config['app']['solver_path'])
    status = s.solve(model)

    # gen output
    x = []
    for ij in model.x:
        if model.x[ij].value > 0:
            x.append({
                "product": ij[0],
                "seller": ij[1],
            })
    y = []
    for j in model.y:
        if model.y[j].value > 0:
            y.append({
                "seller": j,
            })

    output = {
        "status_solver": str(status['Solver'][0]['Status']),
        "status_termination": str(status['Solver'][0]['Termination condition']),
        "total_shippingcost": sum([shippingcost[j['seller']] for j in y]),
        "total_sellers": len(y),
        "total_distance": sum([distance[j['seller']] for j in y]),
        "total_ordercount": sum([ordercount[j['seller']] for j in y]),
        "result": x
             }
    return output