# CrossLangIOTest

CrossLangIOTest is a framework designed to verify the consistency of function inputs and outputs across different programming languages. This project automates the generation of test cases and comparisons to ensure that functions produce equivalent results when implemented in multiple languages.

## Features

- **Automatic Directory and File Creation**: Easily set up the necessary directories and files for your test cases.
- **Multi-language Support**: Generate unit tests for functions in both Python and C++.
- **Input/Output Configuration**: Automatically generate configuration files listing input and output parameters.
- **Result Comparison**: Tools to compare the outputs from different language implementations to ensure consistency.

## Setup

1. **Create the Directory Structure**:
    The script will automatically create a directory named after the function being tested and populate it with necessary files.

2. **Generate Input and Output Files**:
    The framework generates input and output files for each parameter and language, organizing them for easy comparison.

## How to Use

1. **Define Function and Parameters**:
    Edit the script to specify the function name, input parameters, and output return parameters.

2. **Run the Script**:
    Execute the script to create the directory structure and files:
    ```python
    python create_test_structure.py
    ```

3. **Implement Unit Tests**:
    Implement the generated unit test files in the respective languages.

4. **Compare Results**:
    Use the result comparator tool to ensure that the outputs are consistent across languages.
