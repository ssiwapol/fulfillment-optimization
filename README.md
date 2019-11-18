# Optimization model

Mixed Integer Linear Programming (MIP)

Dimensions: product, seller

Objective: Find the appropriate route for distribute product from seller by prioritizing shipping cost, amount of items, distance and order count respectively

Constraints: Distribute to all demands

# Instruction

## Request
---

### Request headers
apikey: [AUTH_KEY]

### Request body

```
{
    "data":
    [
        {
            "product": "a",
            "seller": "1",
            "shippingcost": 100,
            "distance": 100,
            "ordercount": 100
        },
        {
            "product": "b",
            "seller": "2",
            "shippingcost": 200,
            "distance": 200,
            "ordercount": 200
        }
    ]
}
```

## Responses
---

### Resposnes JSON

```
{
    "status_solver": "ok",
    "status_termination": "optimal",
    "total_shippingcost": 300,
    "total_distance": 300,
    "result": [
        {
            "product": "a",
            "seller": 1,
            "shippingcost": 1000
        },
        {
            "product": "b",
            "seller": 2,
            "shippingcost": 2000
        }
    ]
}
```

# Tools
- Code: [Python](https://www.python.org/)
- Optimization Libraries: [Pyomo](http://www.pyomo.org/)
- Solver Engine: [CBC](https://projects.coin-or.org/Cbc)
- API: [Flask](https://palletsprojects.com/p/flask/)
