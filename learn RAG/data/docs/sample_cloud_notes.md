# Sample cloud notes (use your own docs)

## Well-Architected basics
In a cloud architecture review, you typically evaluate workloads across pillars such as reliability, security, cost optimization, operational excellence, and performance efficiency.

Common reliability practices include:
- using multiple availability zones
- implementing health checks and auto-healing
- defining SLOs/SLAs and monitoring key indicators

## Caching
Caching reduces latency and cost by serving repeated requests from a faster store. Typical patterns include:
- read-through cache
- write-through cache
- cache-aside (lazy loading)

Risks and trade-offs:
- stale data
- cache invalidation complexity
- hot keys and uneven load

## Observability
Observability typically combines logs, metrics, and traces. For debugging distributed systems, tracing is often critical to locate latency sources across services.

