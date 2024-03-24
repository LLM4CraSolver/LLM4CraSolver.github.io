# Exploring Large Language Models in Resolving Crash Bugs: Localizing and Repairing

## Benchmark

We focus on crash bugs in the Java programs given their high prevalence. To construct our benchmark, we first select high-quality SO threads from the Stack Overflow data, as well as create a comprehensive list of common Java exception types. Furthermore, we sample 100 threads from the 67,248 threads collected as our RQ1 benchmark.

[SO threads](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Benchmark/all_final_exception_post_info.json), 67248 SO threads related to java crash bugs.

[Java exceptions types](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Benchmark/Java_exception_type_set_with_size.json), the 737 common Java exceptions we parse from Java libraries from Maven Central. 

[100 crash bugs benchmark](https://github.com/LLM4CraSolver/LLM4CraSolver.github.io/blob/main/Benchmark/benchmark_100.json), the 100 SO threads we sample from the 67248 SO threads including 50 code-related crash bugs and 50 environment-related crash bugs.

[41 crash bugs benchmark](https://github.com/LLM4CraSolver/LLM4CraSolver.github.io/blob/main/Benchmark/benchmark_41.json). To validate the effectiveness of our proposed approach, we create a new benchmark consisting of 41 crash bugs (including 11 code-related crash bugs and 30 environment-related crash bugs) that could not be successfully repaired in RQ1 when provided full crash description.

## Result

**RQ1 (Basic Prompt Effectiveness)**: To what extent can ChatGPT, utilizing basic prompts with varying levels of contextual information, accurately localize and repair both code-related and environment-related crash bugs?

[rq1_result](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Result/rq1_result.json), the experimental results of RQ1 on the 100 crash bugs benchmark.

**RQ2 (Enhancing Resolution with Advanced Prompts)**: In what ways do advanced prompts enhance ChatGPT’s ability to resolve crash bugs more effectively?

The experimental result of RQ2 are listed in the paper.

**RQ3 (Evaluation of IntDiagSolver)**: How effectively does IntDiagSolver perform in resolving crash bugs?

– RQ3.a (Effectiveness of IntDiagSolver): To what extent can IntDiagSolver effectively resolve crash bugs?

[rq3_a_result](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Result/rq3_a_result.json), the experimental results of effectiveness of IntDiagSolver on the 41 crash bugs benchmark.

– RQ3.b (Generalizability of IntDiagSolver): To what extent can the effectiveness of IntDiagSolver in crash bug resolution be generalized across different LLMs?

[rq3_b_result](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Result/rq3_b_result), the experimental results of generalizability of IntDiagSolver on the 41 crash bugs benchmark.
