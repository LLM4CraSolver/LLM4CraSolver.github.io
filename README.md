# ChatGPT4CraDiag.github.io

## Benchmark

We focus on crash bugs in the Java programs given their high prevalence. To construct our benchmark, we first select high-quality SO threads from the Stack Overflow data, as well as create a comprehensive list of common Java exception types. Furthermore, we sample 100 threads from the 67,248 threads collected as our RQ1 benchmark.

[SO threads](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Benchmark/all_final_exception_post_info.json), 67248 SO threads related to java crash bugs.

[Java exceptions types](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Benchmark/Java_exception_type_set_with_size.json), the 737 common Java exceptions we parse from Java libraries from Maven Central. 

[100 crash bugs benchmark](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Benchmark/all_final_exception_post_info.json/benchmark_100.json), the 100 SO threads we sample from the 67248 SO threads including 50 code-related crash bugs and 50 environment-related crash bugs.

[41 crash bugs benchmark](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Benchmark/all_final_exception_post_info.json/benchmark_41.json). To validate the effectiveness of our proposed approach, we create a new benchmark consisting of 41 crash bugs (including 11 code-related crash bugs and 30 environment-related crash bugs) that could not be successfully repaired in RQ1 when provided full crash description.

## Result

We focus on how effective ChatGPT is in localizing and repairing crash bugs, including both the code-related crash bugs and the environment-related crash bugs. Our study answer the following two research questions:

**RQ1**: To what extent can ChatGPT be used for error
localization and fixing in software crash bug diagnosis?

[rq1_result](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Result/benchmark_100_result.json), the experimental results of RQ1 on the 100 crash bugs benchmark.

**RQ2**: How can the interaction with ChatGPT be optimized to improve the accuracy and efficiency of software crash bug diagnosis?

The experimental result of RQ2 are listed in the paper. 

Based on the experimental results and research findings, we propose IntDiag-ChatGPT, a novel approach for diagnosing crash bugs by interacting with ChatGPT in a continuous manner. 

[final_result](https://github.com/ChatGPT4CraDiag/ChatGPT4CraDiag.github.io/blob/main/Result/benchmark_41_result.json). We evaluate it on the 41 crash bugs benchmark to validate the effectiveness of our proposed approach.
