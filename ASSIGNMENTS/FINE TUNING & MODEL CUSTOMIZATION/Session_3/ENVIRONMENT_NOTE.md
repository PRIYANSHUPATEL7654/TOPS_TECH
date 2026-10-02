# Fine-Tuning Runtime Note

The LoRA and QLoRA programs are supplied as runnable source. This package was assembled in an environment without Torch, Transformers, PEFT, Datasets, bitsandbytes, or a CUDA GPU, so no model download, adapter training, parameter-count measurement, or RAM comparison was performed here. The scripts do not include invented metrics or screenshots.

To produce machine-specific evidence, install the optional dependencies in `requirements.txt`, use a compatible CUDA environment for QLoRA, run the LoRA scripts, and capture the operating system's memory monitor during both a full fine-tuning baseline and the quantized run. QLoRA support for an encoder architecture and bitsandbytes backend depends on the environment. The supplied QLoRA example exits with an explanatory message if CUDA is unavailable.
