# CSGRAM: A Graph Foundation Model-Based Approach for MRI Image Super-Resolution

CSGRAM is a novel graph-based framework for medical image super-resolution that integrates anatomical structures and multimodal semantic integration. This repository contains the official implementation of the paper "CSGRAM: A Graph Foundation Model-Based Approach for MRI Image Super-Resolution with Multimodal Semantic Integration".

## Key Features

- **Anatomically-Aware Graph Construction**: A flexible graph modeling structure that adapts to different anatomical complexities
- **Clinical Semantic Integration**: Integration of clinical knowledge through a specialized text encoder
- **Hierarchical Attention Mechanism**: A Graph Attention Mechanism (GAM) that respects both local anatomical patterns and global relationships

## Repository Structure

- `basicsr/`: Core implementation of the GraphMSR framework
  - `archs/`: Network architectures including the main GraphMSR architecture
  - `data/`: Data loading and processing utilities, including prompt generation
  - `losses/`: Loss functions used for training
  - `metrics/`: Evaluation metrics (PSNR, SSIM)
  - `models/`: Model implementation and training logic
  - `utils/`: Utility functions for file handling, logging, etc.
- `MSR_kit.py`: Core utilities for graph-based modeling and attention mechanisms
- `parser_setter.py`: Command-line argument parser

## Requirements

- Python 3.7+
- PyTorch 1.8+
- Additional dependencies (listed in requirements.txt)

## Usage

**Note:** The current repository is missing the main execution scripts (`train.py` and `eval.py`). 
These will be added in a future update. The core functionality is available in the existing codebase.

## Citation

If you find this work useful for your research, please cite our paper:

```bibtex


```

## License

This project is licensed under the [LICENSE](LICENSE) - see the LICENSE file for details.

## Coming Soon

- Training and evaluation scripts
- Pre-trained models
- Detailed usage examples
- Configuration files