# Deep Learning Kidney Disease Classification

This project involves deep learning models implemented in Python. We use `conda` for managing the environment and `pip` for installing additional dependencies.

> **Note:** The project is still under development.

## Table of Contents

- [Deep Learning Kidney Disease Classification](#deep-learning-kidney-disease-classification)
  - [Table of Contents](#table-of-contents)
  - [Workflows](#workflows)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Contributing](#contributing)
  - [License](#license)
  - [Additional Files](#additional-files)

## Workflows

1. Update config/config.yaml
2. Update secrets.yaml [Optional]
3. Update src/kidney_dl/params.yaml
4. Update the entity
5. Update the configuration manager in src/config/configuration.py
6. Update the components (data ingestion, model preparation, model evalutation, etc.)
7. Update the pipeline (training & prediction pipelines)
8. Update the main.py (containing endpoints)
9. Update the dvc.yaml (tracking the pipeline)
10. Update the app.py

## Installation

### Prerequisites

Ensure you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed on your system.

### Steps

1. **Clone the repository**

   ```bash
    git clone https://github.com/tanayvaswani/kidney-dl.git
    cd kidney-dl
   ```

2. **Create and activate the conda environment**

   ```bash
    conda create -p venv python=3.10 -y
    conda activate venv/
   ```

3. **Install dependencies**

   We use pip to install dependencies.

   ```bash
    pip install -r requirements.txt
   ```

## Contributing

We welcome contributions! Please see CONTRIBUTING.md for details on how to get involved.

## License

<!-- This project is licensed under the MIT License - see the LICENSE file for details. -->

## Additional Files

- **`requirements.txt`**: This file lists the pip dependencies.
- **`CONTRIBUTING.md`**: This file should outline the guidelines for contributing to the project.
- **`LICENSE`**: This file should contain the license information for the project.
