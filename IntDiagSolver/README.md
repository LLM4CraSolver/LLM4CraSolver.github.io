
# IntDiagSolver Description

Based on our experimental findings, we propose IntDiagSolver, a novel approach for addressing crash bugs through continuous interaction with LLMs. The proposed framework operates through a continuous interaction cycle between the user and the LLM, comprising three main phases: 

- Phase 1: Contextual Information Completion via LLM Self-Planning. Given the bug report, this phase utilizes the LLM’s self-planning capabilities to automatically generate and iteratively refine queries. These queries aim to gather essential contextual information that enriches the original bug report. 

- Phase 2: Iterative Solution Generation. Utilizing the enriched context from the previous phase and the initial bug report, the LLM generates potential solutions. This generation process involves iterative refinement prompts designed to progressively yield a specific and actionable detailed solution. During this process, any follow-up questions asked by the LLM will be answered by the user.

- Phase 3: Solution Validation. In the final phase, we evaluate the correctness of the detailed solution through execution validation. If the execution succeeds, the verified correct solution is returned directly to the user. Conversely, if the execution fails, the LLM iteratively refines and generates a revised solution. To ensure the reliability of this evaluation, the validation process is currently performed manually, and feedback is entered by the user to assist the LLM in further diagnosis and repair.

## Directory Structure

```bash
/
├── README.md                   # Documentation for IntDiagSolver
├── controller.py               # Main pipeline script for IntDiagSolver
├── prompt_template.py          # All prompt templates used in IntDiagSolver
└── utils/                      # Utility scripts directory
    ├── data_utils.py           # Data loading and management utilities
    └── path_utils.py           # Path management utilities
```

## Usage Steps:

1. **Configure API key**: Set your own API key and base URL by editing the `api_key` and `base_url` parameters in `controller.py`.
2. **Set parameters**: Modify `model_name`, `benchmark_data_path`, and `result_data_path` in `controller.py` to the desired parameters for your experiment.
3. **Run IntDiagSolver**: Execute the `controller.py` script to start resolving crash bugs.

## Notes

- During the iterative solution generation process, the LLM may ask targeted follow-up questions. The user should respond to these questions as instructed.

- Once a specific solution is generated, IntDiagSolver will automatically proceed to the validation phase. To ensure the reliability of evaluation at this stage, validation is currently performed manually. Users should determine the result as instructed (i.e, enter 0 for "incorrect," 1 for "correct," or 2 if the LLM's response is correct but "not specific enough").

