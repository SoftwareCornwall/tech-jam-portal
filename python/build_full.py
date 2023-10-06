# take list.html
# open index.html
# replace {{ Content }} with variable

with open('content/list.html', 'r') as file:
    list_content = file.read()

with open('content/home.html', 'r') as file:
    home_content = file.read()

with open('content/header.html', 'r') as file:
    header_content = file.read()

with open('content/footer.html', 'r') as file:
    footer_content = file.read()


combined_content = home_content.replace('{{Content}}', list_content)

combined_content = header_content + combined_content
combined_content = combined_content + footer_content

with open('site/index.html', 'w') as file:
    file.write(combined_content)

