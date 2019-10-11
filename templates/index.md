# FULFILLMENT OPTIMIZATION

## Request
---

### Request URL
[please copy this url](/api)

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
            "seller": 1
        },
        {
            "product": "b",
            "seller": 2
        }
    ]
}
```
