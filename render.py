import os
import shutil
from markdown import Markdown
from xml.etree.ElementTree import Element

HEADER_TAG = 'h1'
ARTICLE_TAG = 'h2'
ARTICLE_TAGS = [HEADER_TAG, ARTICLE_TAG]
BUILD_DIRECTORY = 'build'
m = Markdown()
template = None
with open('template.html', 'r') as fh:
    template = fh.read()


def create_markdown(input_path, output_path, depth):
    title = "Cheatsheet"  # the title of the cheatsheet
    output = None
    with open(input_path, 'r') as fh:
        tree = m.parser.parseDocument(fh.read().split("\n"))
        root_node = tree.getroot()
        new_root = Element('section')
        div_element = None
        for node in root_node:
            if node.tag in ARTICLE_TAGS:
                if div_element is not None:
                    new_root.append(div_element)
                div_element = Element('article')
            if node.tag == ARTICLE_TAG:
                div_element.attrib['class'] = 'column'
            if node.tag == HEADER_TAG:
                title = node.text
            if div_element is not None:
                div_element.append(node)
        if div_element is not None:
            new_root.append(div_element)
        output = m.serializer(new_root)
    if output:
        with open(output_path, 'w+') as output_fh:
            output_fh.write(template.format(**{
                'title': title,
                'body': output,
                'depth': '../' * depth
            }))
    return title


def render_index(cheatsheet_links):
    root = Element('ul')
    for name, link in cheatsheet_links.items():
        link_element = Element('a')
        link_element.text = name
        link_element.attrib['href'] = link
        li_element = Element('li')
        li_element.append(link_element)
        root.append(li_element)
    with open(os.path.join(BUILD_DIRECTORY, 'index.html'), 'w+') as fh:
        fh.write(template.format(**{
            'title': "Index",
            'body': m.serializer(root),
            'depth': ""
        }))


def main():
    cheatsheet_links = {}
    for (dirpath, dirnames, filenames) in os.walk("cheatsheets"):
        directories = list(os.path.split(dirpath)[1:])
        depth = len(directories)
        for filename in filter(lambda x: x.lower().endswith('md'), filenames):
            output_filename = filename[:-2] + "html"
            input_path = os.path.join(dirpath, filename)
            output_directory = os.path.join(*(["build"] + directories))
            output_path = os.path.join(output_directory, output_filename)
            print "Creating {0}...".format(output_path)
            if not os.path.isdir(output_directory):
                os.makedirs(output_directory)
            title = create_markdown(input_path, output_path, depth)
            cheatsheet_links[title] = os.path.join(*(directories + [output_filename]))
    print "Rendering index..."
    render_index(cheatsheet_links)
    static_source = "static"
    static_target = os.path.join("build", "static")
    if os.path.exists(static_target):
        print "Removing old statics..."
        shutil.rmtree(static_target)
    print "Copying statics..."
    shutil.copytree(static_source, static_target)

if __name__ == '__main__':
    main()
