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
            "shippingcost": 1000,
            "distance": 100,
            "ordercount": 10
        },
        {
            "product": "b",
            "seller": "2",
            "shippingcost": 2000,
            "distance": 200,
            "ordercount": 20
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
    "total_shippingcost": 3000,
    "total_sellers": 2,
    "total_distance": 300,
    "total_ordercount": 30,
    "result": [
        {
            "product": "a",
            "seller": "1",
            "shippingcost": 1000
        },
        {
            "product": "b",
            "seller": "2",
            "shippingcost": 2000
        }
    ]
}
```
