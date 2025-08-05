# This Python script takes an image/poem name, and creates the necessary html in order to insert into the html document.

def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

poem_name = "Flower store"
markdown_file = "poems_and_images/" + poem_name + ".md"

html_text = f"""
<div class="blog-single-post-thumb">
   <div class="blog-post-title">
       <h3 class="neuropol">{poem_name}</h3>
   </div>
   <img src="poems_and_images/{poem_name}.jpg" class="img-responsive">
   <h3 class="neuropol" style="font-style: italic; font-size: 10px">X</h3>\n
"""

with open(markdown_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
if lines[-1] != '\n':
    lines.append('\n')

paragraphs = []
current_paragraph = []

for line in lines:
    stripped = line.strip()
    if stripped == "":
        if current_paragraph:
            paragraphs.append(current_paragraph)
            current_paragraph = []
    else:
        current_paragraph.append(stripped)

# Build HTML as a string
for para in paragraphs:
    html_text += '<p class="reduce-space">\n'
    for line in para:
        html_text += f'    {line}<br>\n'
    html_text += '</p>\n'

html_text += """
    <h3 class="neuropol" style="font-style: italic; font-size: 10px">X</h3>
       <p style="text-align: center; font-size: 20px; margin-top: 30px;" class="neuropol">
           <a href="glitched_memories.html">Back to Gallery</a>
       </p>
</div>
"""



print(html_text)