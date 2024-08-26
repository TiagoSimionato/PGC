from os import listdir, mkdir, path

from configs import OUTPUT_PATH


def save(content: str, file_name: str = 'output', output_path: str = OUTPUT_PATH):  
  if (not path.isdir(output_path)):
    mkdir(output_path)

  index_offset = len(listdir(output_path))
  with open(f'{output_path}/{index_offset + 1}_{file_name}.txt', 'w', encoding='utf-8') as f:
    f.write(content)

def load(file_path: str):
  with open(file_path, 'r', encoding='utf-8') as f:
    return f.read()

BASE_CODE = load('./src/base_code.py')
CODE_EXAMPLE_SUM = load('./src/example_code_sum.txt')
CODE_EXAMPLE_SUB = load('./src/example_code_subtraction.txt')
FINAL_LINES = 'if __name__ == \'__main__\':\n  unittest.main()'

def getText(item):
  return item.get_attribute(name='text')

def parseResponse(response: str):
  try:
    [tested_features_string, code,_] = response.split('\'\'\'')

    tested_features = tested_features_string
    for char in ['[', ']', ' ', '\'', '"', '\n', ';']:
      tested_features = tested_features.replace(char, '')

    tested_features = tested_features.split(':')[1].split(',')
    
    return [tested_features, code]
  except:
    print(response)