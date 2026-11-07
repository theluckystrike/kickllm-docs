Model coverage
==============

The calculator tracks the current published API prices for the Claude, GPT, Gemini
and open-weight provider lines it lists. Prices are per million tokens and are
refreshed when a provider changes its price sheet.

Two caveats worth keeping in mind:

* List price is not effective price. Batch discounts, prompt caching and committed
  throughput can move a real bill by more than the difference between two models.
* A cheaper model that needs two attempts per task is not cheaper. Cost per
  successful task, not cost per call, is the number that survives contact with
  production.
