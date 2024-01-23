# PGC : Mobile testing with LLM

## Dependencies

### Virtual Environment

First setup de python virtual environment

```bash
python -m venv .venv
```

### Packages

The necessary packages and the corresponding versions are declared under `requirements.txt` file. Note that langchain requires C++ build tools in order to be installed.

```bash
pip install -r requirements.txt
```

In case `langserve` is not installed sucessfully try the following:

```bash
pip install "langserve[all]"
```

### LLM Models

[Download the Mini Orca LLM Model](https://gpt4all.io/models/gguf/orca-mini-3b-gguf2-q4_0.gguf)

[Download the GPT4ALL Falcon LLM Model](https://gpt4all.io/models/gguf/gpt4all-falcon-q4_0.gguf)

[Download the WizardLM (larger) LLM Model](https://gpt4all.io/models/gguf/wizardlm-13b-v1.2.Q4_0.gguf)

By default, models should be stored inside a `models` folder, but the desired path can be adjusted in `configs.py`

### Tesseract

The project uses Tesseract, an open source OCR library made by Google. To install it, follow the [Official Instructions](https://github.com/tesseract-ocr/tesseract)

## Running

Activating venv

```bash
.venv\Scripts\activate.bat
```

Start by initializing the server

```bash
python llmServer.py
```

it will train the model run the a REST API app under the port `8000` and path `/query`

By default it searches for the Wizard language model at the models directory, but it can be specified when initializing the server. Use options `1`, `2` or `3` according to the size of the model desired, being `3` the largest.

```bash
python llmServer.py [your_path_here]
```
