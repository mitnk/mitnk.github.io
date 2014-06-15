#! /usr/local/bin/py
import os
os.environ['DJANGO_SETTINGS_MODULE'] = '_src.settings'

import django
django.setup()
from django.template.loader import render_to_string
from pathlib import Path
import datetime
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


def add(title):
    title = _parse_title(title)
    _create_md_file(title)


def _create_html_file(title, year, month):
    dir_ = Path('./{:04d}/{:02d}/{}/'.format(year, month, title))
    if not dir_.exists():
        dir_.mkdir(parents=True)
        print('created dir: {}'.format(dir_.absolute()))
    file_ = dir_ / 'index.html'
    return '{}'.format(file_.absolute())


def make_html(md_file):
    strings = md_file.split('/')
    title = _parse_title(strings[-1])
    month = int(strings[-2])
    year = int(strings[-3])
    with open(md_file, 'r') as f:
        content = f.read()
    context = {
        'content': content,
        'title': title.replace('_', ' ').title(),
        'time_added': datetime.datetime.now(),
    }
    html = render_to_string('article.html', context)
    file_html = _create_html_file(title, year, month)
    with open(file_html, 'w') as f:
        f.write(html)
    print('html generated: {}'.format(file_html))


def find_md_file_list():
    md_list = []
    for root, dirs, files in os.walk("./_src/docs/"):
        for file in files:
            if file.endswith(".md") or file.endswith(".MD"):
                md_list.append(os.path.join(root, file))
    return md_list


def compile(md_file):
    if md_file == 'all':
        md_list = find_md_file_list()
        for f in md_list:
            make_html(f)
    else:
        html = make_html(md_file)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: mc.py add <article title>")
        exit(1)
    if sys.argv[1].lower() == 'add':
        title = ' '.join(sys.argv[2:])
        add(title)
    elif sys.argv[1].lower() == 'compile':
        title = ' '.join(sys.argv[2:])
        compile(title)
    else:
        raise NotImplementedError()
