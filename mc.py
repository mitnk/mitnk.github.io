#! /usr/local/bin/py
import os
os.environ['DJANGO_SETTINGS_MODULE'] = '_src.settings'

import django
django.setup()
from django.template.loader import render_to_string
from pathlib import Path
import datetime
import markdown
import re


def _parse_title(title):
    title = re.sub('[^_a-zA-Z0-9. ]', '', title)
    title = re.sub('  *', ' ', title).strip()
    title = re.sub(' ', '_', title)
    title = re.sub('\.md$', '', title, flags=re.IGNORECASE)
    return title


def _create_md_file(title):
    today = datetime.date.today()
    dir_ = Path('./_src/docs/{:04d}/{:02d}/'.format(today.year, today.month))
    if not dir_.exists():
        dir_.mkdir(parents=True)
        print('created dir: {}'.format(dir_.absolute()))
    file_ = dir_ / '{}.md'.format(title)
    if file_.exists():
        print("ERROR: {} already exists".format(file_.absolute()))
        return
    file_.touch()
    print("created file: {}".format(file_.absolute()))


def create(title):
    title = _parse_title(title)
    _create_md_file(title)


def _create_html_file(md_file):
    today = datetime.date.today()
    title = _parse_title(md_file.split('/')[-1])
    dir_ = Path('./{:04d}/{:02d}/{}/'.format(today.year, today.month, title))
    if not dir_.exists():
        dir_.mkdir(parents=True)
        print('created dir: {}'.format(dir_.absolute()))
    file_ = dir_ / 'index.html'
    return '{}'.format(file_.absolute())


def make_html(md_file):
    with open(md_file, 'r') as f:
        text = f.read()
    content = markdown.markdown(text)
    context = {'content': content}
    html = render_to_string('article.html', context)
    file_html = _create_html_file(md_file)
    with open(file_html, 'w') as f:
        f.write(html)
    print('html generated: {}'.format(file_html))


def compile(md_file):
    html = make_html(md_file)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: mc.py create <title name>")
        exit(1)
    if sys.argv[1].lower() == 'create':
        title = ' '.join(sys.argv[2:])
        create(title)
    elif sys.argv[1].lower() == 'compile':
        title = ' '.join(sys.argv[2:])
        compile(title)
    else:
        raise NotImplementedError()
