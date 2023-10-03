import os
import warnings

descriptions = []
tutorial_names = []
pdf_links = []
languages = os.listdir(f'{os.getcwd()}/worksheets')

for language in languages:
  tutorials = os.listdir(f'worksheets/{language}')
  
  for i in tutorials:
    file_list = os.listdir(f'worksheets/{language}/{i}')
    text_files = [i for i in file_list if i[-4:] == '.txt']
    pdf_files = [i for i in file_list if i[-4:] == '.pdf']

    # adding to pdf_links
    if len(pdf_files) > 1:
      warnings.warn(f'{i} tutorial has more than one pdf. Ignoring it')
    
    elif len(pdf_files) < 1:
      raise ValueError(f'tutorial {i} has no pdf files')
    
    elif len(pdf_files) == 1:
      pdf_links.append(f'worksheets/{language}/{i}/{pdf_files[0]}')

    # adding to descriptions
    if len(text_files) > 1:
      raise ValueError(f'{i} tutorial has more than one description')
    
    elif len(text_files) == 1:
      tutorial_names.append(text_files[0])

      with open(f'worksheets/{language}/{i}/{tutorial_names[-1]}', 'r') as file:
        descriptions.append(file.read().replace('\n', ''))

template = '''
  <div class="image_desc">
    <a href="--pdf link--">
      <img src="images/python_logo.jpg" height="80" width="80">
      <p>--description--</p>
    </a>
  </div>
'''

filled_templates = []

for (desc, link) in zip(descriptions, pdf_links):
  output = template.replace('--pdf link--', link)
  output = output.replace('--description--', desc)
  filled_templates.append(output)

output = '\n'.join(filled_templates)

with open('template_index.html', 'r') as file:
  content = file.read()

content = content.replace('{{Content}}', output)

with open('index_2.html', 'w') as file:
  file.write(content)