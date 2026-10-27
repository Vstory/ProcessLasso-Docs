<!-- source: https://bitsum.com/apps/process-lasso/docs/interface/graph/ -->

# The Graph

The Process Lasso graph shows a calculation of system responsiveness, overall CPU and GPU utilization, and the memory load. The system responsiveness is calculated using a proprietary algorithm that measures the latency in the user interface (windowing) subsystem.

Highlighted portions of the graph indicate that a ProBalance process restraint occurred during that period. This can help you see the impact of Process Lasso on system responsiveness.

## Highlighted ProBalance Events

During periods when ProBalance takes action to ensure your system responsiveness remains high despite a spike in CPU use, the graph will be highlighted. The log can be referenced to see what actions were taken.

![Lasso Graph](../media/graph-probalance-highlights.png)

Note these colors are reversed in more recent versions!

Hovering over a highlight event will show you the process(es) adjusted (in priority or CPU affinity) at that time.

![Graph tooltip showing processes adjusted during a highlighted event](../media/graph-tooltip.png)

## GPU Performance Data

GPU utilization is shown on the primary graph, a dedicated widget, status bar, and in the process lists.

![](../media/graph-with-core-panels.png)

Since any inspection of GPU performance data incurs *some* amount of overhead, often showing up in ntoskrnl.exe, this data is only collected when Process Lasso is visible. Due to this, some periods of GPU data may be missing from the graph. GPU utilization reporting can also be disabled entirely in the “View / Graph Components” menu.

## Aggregated CPU Use of Selected Processes

With Process Lasso you can see the individual CPU history of process(es) you select in the process list. The CPU utilization history of all processes currently selected (highlighted) in the process list is drawn as a smaller white line on the graph, as indicated by the arrow below. In this example, several CPU-consuming processes were selected, so the line shows their combined CPU use.

![CPU use of selected processes shown as a thin line on the graph](../media/graph-selected-history.png)
