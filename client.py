from langserve import RemoteRunnable
import sys

prompt = " ".join(sys.argv[1:]) if (len(sys.argv) > 1) else 'say hello'

remote_chain = RemoteRunnable('http://localhost:8000/query/')
response = remote_chain.invoke({"prompt" : prompt})

print(response)