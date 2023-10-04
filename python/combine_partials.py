import os
current_folder = os.getcwd()

def combine(html_files , output_file):
    # Initialize an empty string to store the combined HTML content
    combined_html = ""
    # Iterate through each HTML file and append its content to the combined_html string
    for html_file in html_files:
        html_file = str(current_folder+html_file)
        with open(html_file, "r") as file:
            combined_html += file.read()
    with open(output_file, "w") as output:
        output.write(combined_html)

# List of HTML file names to be combined
html_home = ["/partials/header.html", "/content/home.html", "/partials/footer.html"]
combine(html_home , output_file="index.html")

html_list = ["/partials/header.html", "/content/list.html", "/partials/footer.html"]
combine(html_list, output_file="python.html")