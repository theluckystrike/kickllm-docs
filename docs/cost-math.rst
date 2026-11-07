How a monthly LLM bill is computed
==================================

A bill is four multiplications and one addition per model:

1. **Input tokens** (prompt + system prompt + retrieved context) x input price per
   million tokens.
2. **Cached input tokens**, if the provider discounts them, at the cached rate.
3. **Output tokens** x output price per million tokens.
4. **Reasoning tokens**, where they are billed as output.

Worked example, one conversation with 2,000 input tokens and 600 output tokens on a
model priced at $3 per 1M input and $15 per 1M output:

* input: 2,000 / 1,000,000 x $3 = $0.006
* output: 600 / 1,000,000 x $15 = $0.009
* total: $0.015 per conversation

At 20,000 conversations a month that is $300. The same shape of calculation, run
across every model, is what the `KickLLM calculator <https://kickllm.com/>`_ shows
side by side.

The error people make is comparing headline per-token prices without fixing the
input:output ratio. Output tokens are typically 4-5x the input price, so a workload
that writes long answers behaves very differently from one that classifies short
snippets.
