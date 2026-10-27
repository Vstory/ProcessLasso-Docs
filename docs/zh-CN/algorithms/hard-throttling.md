<!-- source: https://bitsum.com/apps/process-lasso/docs/algorithms/hard-throttling/ -->

<a id="hard-throttling"></a>

# 硬性节流

- *菜单路径：「选项 / CPU / 更多 / 硬性节流 …」*

硬性 CPU 节流是一项旧功能，我们不建议大多数人使用。可以改用 [CPU 限制器](cpu-limiter.md#cpulimiter)或 [CPU 相关性](../rules/cpu-affinities.md#default_affinities)规则。硬性 CPU 节流会向进程的线程注入强制休眠，以降低该进程的 CPU 消耗。这同时也会让进程本身变慢，并可能引发其他副作用。
