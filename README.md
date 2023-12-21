# Artifacts for Query Plan Study

This repository contains the artifact for the manuscript "Towards a Unified Query Plan Representation: An Exploratory
Case Study".

Our artifact includes 
1) a website that allows further studying our results and raw data, 
2) the reusable library described in Section 4,
3) the visualization application described in Application 2, Section 5,
4) the benchmarking application described in Application 3, Section 5.

## Structure
* [docs/](docs/): Contains the study results and the first application: visualization, both of which have been deployed on https://unifiedqueryplan.github.io/.
* [tpc-h/](tpc-h/): Contains the scripts to configure TPC-H benchmark and experimental data for the second application: benchmarking.

* Other python files are the reusable library **UPlan** for converting query plans into the unified representation. Please see below for more details.

## UPlan
To transfer an original TiDB query plan into the unified representation, run:
```bash
python3 main.py -t tidb -i tpc-h/queryplan_raw/1.tidb
```
The unified query plan in the text format will be printed on the console.