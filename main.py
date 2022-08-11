# converts html to markdown
import os
import re

import bs4
from markdownify import MarkdownConverter


# Create shorthand method for conversion
def md(soup, **options):
    return MarkdownConverter(**options).convert_soup(soup)


if __name__ == '__main__':
    pattern = re.compile("([\n])|([\ ]{2,})")
    os.makedirs('markdown', exist_ok=True)
    file = open('../../postconf.5.html')
    soup = bs4.BeautifulSoup(file, 'lxml')
    args = soup.select('body>dl>dt>b>a:first-of-type')
    for name in args:
        filename = os.path.join('markdown', name.getText() + '.md')
        markdownFile = open(filename, 'w')
        heading = re.sub(pattern, ' ', name.parent.getText())
        markdownFile.write(f'# {heading}')
        markdownFile.write(md(name.find_next('dd'), strip=['a']))
        markdownFile.close()
