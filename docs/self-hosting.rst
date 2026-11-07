Self-hosting versus API pricing
===============================

Per-token API pricing and GPU-hour pricing are not directly comparable, so the
comparison needs a utilisation assumption. A single rented GPU instance costs
roughly $1,000-$10,000 a month depending on the card, and it produces a fixed
number of tokens per hour. Below a certain utilisation the API is cheaper; above
it, owned capacity wins.

The break-even is dominated by two variables: tokens per second actually achieved
on your workload, and how many hours per month the box is busy. Idle capacity is
the most expensive token you will ever buy.
