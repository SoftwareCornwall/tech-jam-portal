import os
import warnings

descriptions = []
titles = []
pdf_links = []
difficulties = []
images = []
languages = os.listdir(f'{os.getcwd()}/worksheets')

languages = [i for i in languages if not i.startswith('.') and not i.endswith('.py')]

for language in languages:
    tutorials = os.listdir(f'worksheets/{language}')
    tutorials = [i for i in tutorials if not i.startswith('.')]

    for tut in tutorials:
        file_list = os.listdir(f'worksheets/{language}/{tut}')
        text_files = [i for i in file_list if i.endswith('.txt')]
        pdf_files = [i for i in file_list if i.endswith('.pdf')]

        # adding to pdf_links
        if len(pdf_files) > 1:
            warnings.warn(f'{tut} tutorial has more than one pdf. Ignoring it')

        elif len(pdf_files) < 1:
            raise ValueError(f'tutorial {tut} has no pdf files')

        elif len(pdf_files) == 1:
            pdf_links.append(f'worksheets/{language}/{tut}/{pdf_files[0]}')

        if len(text_files) > 1:
            raise ValueError(f'{tut} tutorial has more than one description')

        elif len(text_files) == 1:
            title = text_files[0]
            title = title.replace('.txt', '')
            title = title.replace('_', ' ')
            title = title.title()
            titles.append(title)

            with open(f'worksheets/{language}/{tut}/{text_files[0]}', 'r') as file:
               descriptions.append(file.readline())
               diff_level = file.readline()
               print(diff_level)
               if diff_level == '':
                   difficulties.append('Not set')
               else:
                   difficulties.append(diff_level)

        # image
        if 'website-image.png' in file_list:
            image = f'worksheets/{language}/{tut}/website-image.png'
        else:
            image = 'images/tech-jam-website-logo-1280x1280.png'
        images.append(image)

# get list item template

with open('partials/list_item.html', 'r') as file:
   template = file.read()

# fill in template

filled_templates = []

for (desc, link, title, image, difficulty_level) in zip(descriptions, pdf_links, titles, images, difficulties):
    output = template.replace('{{pdf link}}', link)
    output = output.replace('{{description}}', desc)
    output = output.replace('{{title}}', title)
    output = output.replace('{{difficulty level}}', difficulty_level)
    output = output.replace('{{image}}', image)
    filled_templates.append(output)

output = '\n'.join(filled_templates)

# get full list template

with open('partials/list_full.html', 'r') as file:
   full_template = file.read()

# fill in template

full_html = full_template.replace('{{Content}}', output)

# save full list

with open('content/list.html', 'w') as file:
    file.write(full_html)
