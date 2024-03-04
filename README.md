# PGC : Mobile testing with LLM

## Todo

- gemini api
- use saved cache
- remove unnecessary dependencies
- example.txt

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

### Appium

The project uses appium for android emulator automation. It aims to extract ui data to feed the LLM prompt so it can generate test to run with the Appium tool itself.

```bash
npm i -g appium

appium driver install uiautomator2
appium driver install espresso
```

version: v2.5.1

uiautomator2@3.0.1
espresso@2.36.1

It is required to set `ANDROID_HOME` and `JAVA_HOME` environment variables

## Running

Activating venv

```bash
.venv\Scripts\activate.bat
```

Start by initializing the server

```bash
python llmServer.py
```

it will load the model and serve it as a REST API under the port `8000` and path `/query`

By default it searches for the Wizard language model at the models directory, but it can be specified when initializing the server. Use options `1`, `2` or `3` according to the size of the model desired, being `3` the largest.

```bash
python llmServer.py [your_path_here]
```
