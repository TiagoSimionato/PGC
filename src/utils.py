from os import listdir, mkdir, path


def save(content: str, file_name: str = 'output', output_path: str = 'outputs'):  
  if (not path.isdir(output_path)):
    mkdir(output_path)

  index_offset = len(listdir(output_path))
  with open(f'{output_path}/{index_offset + 1}_{file_name}.txt', 'w', encoding='utf-8') as f:
    f.write(content)

def getText(item):
  return item.get_attribute(name='text')