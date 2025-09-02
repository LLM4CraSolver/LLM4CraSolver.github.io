# Exploring Large Language Models in Resolving Crash Bugs: Localizing and Repairing

## Benchmark

We focus on crash bugs in the Java programs given their high prevalence. To construct our benchmark, we first select high-quality SO threads from the Stack Overflow data, as well as create a comprehensive list of common Java exception types. Furthermore, we sample 100 threads from the 67,248 threads collected as our RQ1 benchmark.

[SO threads](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Benchmark/all_final_exception_post_info.json), 67248 SO threads related to java crash bugs.

[Java exceptions types](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Benchmark/Java_exception_type_set_with_size.json), the 737 common Java exceptions we parse from Java libraries from Maven Central. 

[100 crash bugs benchmark](https://github.com/LLM4CraSolver/LLM4CraSolver.github.io/blob/main/Benchmark/java_benchmark_100.json), the 100 SO threads we sample from the 67248 SO threads including 50 code-related crash bugs and 50 environment-related crash bugs.

[41 crash bugs benchmark](https://github.com/LLM4CraSolver/LLM4CraSolver.github.io/blob/main/Benchmark/java_benchmark_41.json), To validate the effectiveness of our proposed approach, we create a new benchmark consisting of 41 crash bugs (including 11 code-related crash bugs and 30 environment-related crash bugs) that could not be successfully repaired in RQ1 when provided full crash description.

[42 crash bugs benchmark](https://github.com/LLM4CraSolver/LLM4CraSolver.github.io/blob/main/Benchmark/multi_language_benchmark_42.json),To build this multilingual dataset, we invited the same two participants from Section 5.2 to follow the data collection procedures described in Section 2.1. We collected a total of 42 environment-related crash bugs spanning Java, C/C++, and Python for further generalization evaluation (with 13 cases for java, 20 for Python, and 9 for C/C++). To further assess the effectiveness of LLMs on previously unseen data, all 42 crash bugs were sourced fromStack Overflow posts published after 2024.
## Result

**RQ1 (Basic Prompt Effectiveness)**: To what extent can ChatGPT, utilizing basic prompts with varying levels of contextual information, accurately localize and repair both code-related and environment-related crash bugs?

[rq1_result](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Result/rq1_result.json), the experimental results of RQ1 on the 100 crash bugs benchmark.

**RQ2 (Enhancing Resolution with Advanced Prompts)**: In what ways do advanced prompts enhance ChatGPT’s ability to resolve crash bugs more effectively?

The experimental result of RQ2 are listed in the paper.

**RQ3 (Evaluation of IntDiagSolver)**: How effectively does IntDiagSolver perform in resolving crash bugs?

**RQ4 (Generalizability of IntDiagSolver)**:How well does IntDiagSolver generalize to differentscenarios?

- RQ4.a (Generalizability across LLMs):To what extent can the effectiveness of IntDiagSolver in resolving crash bugs be generalized across different LLMs?
- 
[rq4_a_result](https://github.com/LLM4CraSolver/LLM4CraSolver.github.io/tree/main/Result/rq4_a_result), the experimental results of Generalizability across LLMs on the 41 crash bugs benchmark.

- RQ4.b (Generalizability across Programming Languages):To what extent can the effectiveness of IntDiagSolver in resolving crash bugs be generalized across different programming languages?

[rq4_b_result](https://github.com/LLM4CraSolver/LLM4CraSolver.github.io/tree/main/Result/rq4_b_result), the experimental results of Generalizability across Programming Languages on the 42 crash bugs benchmark.
