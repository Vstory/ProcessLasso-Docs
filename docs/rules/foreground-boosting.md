<!-- source: https://bitsum.com/apps/process-lasso/docs/rules/foreground-boosting/ -->

# Foreground Boosting

- *Menu path: ‘Options / CPU / Foreground Boosting’*

Foreground Boosting will raise the priority class of the process currently in the foreground. Windows already does a foreground priority boost, and further boosting is usually not effective. ProBalance works in the opposite direction, lowering the priority class of problematic background processes, for a reason. Still, Foreground Boosting can be useful in some environments, and on Alder Lake is an easy way to signal to the Windows scheduler that the foreground process should prefer P-cores.

NOTE: Do not confuse Foreground Boosting with the “Thread Boost” submenu that controls Windows Dynamic Thread Priority Boosting.
