import os
current_folder = os.getcwd()
parent_folder = os.path.dirname(current_folder)
print("the folder is here" , current_folder)


def combine(html_files):
    # Initialize an empty string to store the combined HTML content
    combined_html = ""

    # Iterate through each HTML file and append its content to the combined_html string
    for html_file in html_files:
        html_file = str(current_folder+html_file)
        with open(html_file, "r") as file:
            combined_html += file.read()

# Write the combined HTML content to the output file
    with open(output_file, "w") as output:
        output.write(combined_html)

    print(f"Combined HTML written to {output_file}")

# List of HTML file names to be combined


html_files = ["/partials/header.html", "/content/home.html", "/partials/footer.html"]

# Output file name for the combined HTML
output_file = "index.html"

combine(html_files)



# List of HTML file names to be combined
html_files = ["/partials/header.html", "/content/list.html", "/partials/footer.html"]

# Output file name for the combined HTML
output_file = "python.html"

combine(html_files)