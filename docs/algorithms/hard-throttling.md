<!-- source: https://bitsum.com/apps/process-lasso/docs/algorithms/hard-throttling/ -->

# Hard-Throttling

- *Menu path: ‘Options / CPU / More / Hard Throttles …’*

Hard CPU Throttling is a legacy feature that we don’t recommend most people use. Instead, consider the [CPU Limiter](cpu-limiter.md#cpulimiter) or [CPU Affinity](../rules/cpu-affinities.md#default_affinities) rules. Hard CPU Throttling injects forcible sleeps into a process’s threads to slow the process’s CPU consumption down. This will also slow the process itself down, and potentially cause other side-effects.
