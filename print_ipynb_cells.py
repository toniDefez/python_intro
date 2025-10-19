import json
import io
path = r'text_transfer_learning\\text_transfer.ipynb'
with io.open(path, encoding='utf-8') as f:
    data = json.load(f)
for idx, cell in enumerate(data['cells']):
    print('Cell {} [{}]'.format(idx, cell['cell_type']))
    print('-'*40)
    src = ''.join(cell.get('source', ''))
    if cell['cell_type'] == 'markdown':
        print(src.strip())
    else:
        lines = src.strip().splitlines()
        for line in lines[:10]:
            print(line)
        if len(lines) > 10:
            print('...')
    print('')
