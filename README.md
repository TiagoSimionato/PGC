# PGC : Mobile testing with LLM

## Dependencies

### Virtual Environment

 First setup de python virtual environment

```bash
python -m venv .venv
```

### Packages

 The necessary packages and the corresponding versions are declared under `requirements.txt` file

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

## Running

 Start by initializing the server 

```bash
python llmServer.py
```

 it will train the model run the a REST API app under the port `8000` and path `/query`

 By default it searches for the Falcon model at the root directory, but it can be specified when initializing the server

 ```bash
 python llmServer.py [your_path_here]
 ```