from os import listdir, path, mkdir

def save(content: str, output_path):
  file_name = 'output'
  
  if (not path.isdir(output_path)):
    mkdir(output_path)

  index_offset = len(listdir(output_path))
  with open(f'{output_path}/{file_name}_{index_offset + 1}.txt', 'w') as f:
    f.write(content)

def getText(item):
  return item.get_attribute(name='text')