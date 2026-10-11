# structure
```
project/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── quadrature/
│   │   ├── __init__.py
│   │   ├── simpson.py
│   │   ├── trapezoid.py
│   │   ├── monte_carlo.py
│   │   └── error_control.py
│   ├── functions/
│   │   ├── __init__.py
│   │   ├── gaussian.py
│   │   ├── integral_logarithm.py
│   │   └── primes.py
│   └── tasks/
│       ├── __init__.py
│       ├── task1_1_gaussian_integral.py
│       ├── task1_2_normal_table.py
│       ├── task2_li_trapezoid.py
│       ├── task2_li_monte_carlo.py
│       └── task2_compare_pi.py
├── data/
│   ├── input/
│   └── output/
│       ├── normal_table.csv
│       ├── normal_table.tex
│       ├── li_results.csv
│       └── figures/
├── tests/
│   ├── test_simpson.py
│   ├── test_trapezoid.py
│   ├── test_monte_carlo.py
│   └── test_tasks.py
└── scripts/
    ├── run_all.py
    └── make_report.sh

```