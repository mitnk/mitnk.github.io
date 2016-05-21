#! /usr/bin/env python
import os
os.environ['DJANGO_SETTINGS_MODULE'] = '_src.settings'

import django
django.setup()
from django.template.loader import render_to_string
from pathlib import Path
import datetime
import re


def _parse_title(title):
    title = re.sub('[^-_a-zA-Z0-9. ]', '', title)
    title = re.sub('  *', ' ', title).strip()
    title = re.sub(' ', '-', title)
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


def create_html_file(md_path, wiki=False):
    if wiki:
        target_dir = '_src/wiki/'
    else:
        target_dir = '_src/docs/'

    if not md_path.startswith(target_dir):
        raise ValueError(
            'Must put md files under {} '
            'and run scripts under project\'s root dir'.format(
                target_dir,
        ))

    tokens = re.sub('^{}'.format(target_dir), '', md_path).split('/')
    slug = _parse_title(tokens.pop())
    try:
        year = int(tokens[0])
        month = int(tokens[1])
        return _create_blog_html_file(slug, year, month, wiki=wiki)
    except (IndexError, ValueError):
        return _create_other_html_file(tokens, slug)


def _create_other_html_file(tokens, slug):
    dir_ = Path('./' + '/'.join([x.lower() for x in tokens]) + '/{}/'.format(slug.lower()))
    if not dir_.exists():
        dir_.mkdir(parents=True)
        print('created dir: {}'.format(dir_.absolute()))
    file_ = dir_ / 'index.html'
    return '{}'.format(file_.absolute())


def _create_blog_html_file(slug, year, month, wiki=False):
    if wiki:
        dir_ = Path('./wiki/{:04d}/{:02d}/{}/'.format(year, month, slug.lower()))
    else:
        dir_ = Path('./{:04d}/{:02d}/{}/'.format(year, month, slug.lower()))

    if not dir_.exists():
        dir_.mkdir(parents=True)
        print('created dir: {}'.format(dir_.absolute()))
    file_ = dir_ / 'index.html'
    return '{}'.format(file_.absolute())


def get_title_with_markdown_format(md_file):
    with open(md_file) as f:
        result = re.findall(r'^([^\n]*)\n==*\n', f.read().strip())
        return result[0] if result else None


def make_html(md_file, wiki=False, use_br=False):
    file_html = create_html_file(md_file, wiki=wiki)
    slug = _parse_title(md_file.split('/')[-1])
    title = get_title_with_markdown_format(md_file) or slug
    with open(md_file, 'r') as f:
        content = f.read()
        result = re.findall(r'^[^\n]*\n==*\n', content)
        if result:
            content = content.replace(result[0], '')
    context = {
        'content': content,
        'title': title.replace('[-_]', ' ').title(),
        'time_added': datetime.datetime.now(),
        'use_br': use_br,
        'is_wiki': wiki,
    }
    html = render_to_string('article.html', context)
    with open(file_html, 'w') as f:
        f.write(html)
    print('html generated: {}'.format(file_html))


def find_md_file_list(wiki=False):
    md_list = []
    dir_ = './_src/wiki/' if wiki else './_src/docs/'
    for root, dirs, files in os.walk(dir_):
        for file in files:
            if file.endswith(".md") or file.endswith(".MD"):
                md_list.append(os.path.join(root, file))
    return md_list


def compile_to_html(md_file, wiki=False, use_br=False):
    if '_src/wiki/' in md_file:
        wiki = True

    if md_file == 'all':
        md_list = find_md_file_list(wiki)
        for f in md_list:
            make_html(f, wiki=wiki, use_br=use_br)
    else:
        make_html(md_file, wiki=wiki, use_br=use_br)


def generatesitemap():
    dir_ = './site_map/'
    if not os.path.exists(dir_):
        os.mkdir(dir_)

    html = '<html><head><title>Site Map</title></head><body>'
    for root, dirs, files in os.walk('./'):
        if not (root.startswith('./2') or root.startswith('./wiki')):
            continue
        for file in files:
            if file == 'index.html':
                html += '<a href="{}/">{}</a><br>\n'.format(root[1:], root.split('/')[-1])
                print('=== {} {}'.format(root, file))

    html += 'Hi Google.</body></html>'
    with open('./site_map/index.html', 'w') as f:
        f.write(html)


def find_latest_articles(count=10):
    article_list = []
    for root, dirs, files in os.walk('./'):
        if not root.startswith('./2'):
            continue
        for file in files:
            if file != 'index.html':
                continue
            article_list.append(os.path.join(root, file))
    article_list.sort(reverse=True)
    return article_list[:count]


def generateindex():
    class _Article(object):
        pass

    article_list = []
    result = find_latest_articles()
    for item in result:
        obj = _Article()
        obj.url = item[1:].rstrip('index.html')
        obj.title = ' '.join(item.split('/')[-2].split('-')).title()
        article_list.append(obj)

    context = {
        'article_list': article_list,
    }
    html = render_to_string('index.html', context)
    with open('./index.html', 'w') as f:
        f.write(html)
    print('index.html generated.')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Article Maker')
    parser.add_argument('--add', '-a')
    parser.add_argument('--compile', '-c')
    parser.add_argument('--wiki', action='store_true', default=False)
    parser.add_argument('--use_br', action='store_true')
    args = parser.parse_args()

    if args.add:
        args = parser.parse_args()
        add(args.add)
    elif args.compile:
        compile_to_html(args.compile, wiki=args.wiki, use_br=args.use_br)
