#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import codecs
import json
import re
import urllib


with codecs.open('download/package-jsons', encoding='utf-8') as in_file, \
        codecs.open('output.txt', mode='wb', encoding='utf-8') as out_file:
    for package_json in in_file:
        package_dict = json.loads(package_json)
        package_info = package_dict['info']

        # Build abstract
        abstract_lines = []
        summary = package_info['summary']
        if not summary or summary == 'UNKNOWN':
            continue
        abstract_lines.append(re.sub(r'\s', ' ', summary, flags=re.MULTILINE | re.UNICODE))
        abstract_lines.append('Downloads in the last month: %s' % package_info['downloads']['last_month'])

        latest_release_info = package_dict['releases'][package_info['version']]
        if latest_release_info:
            abstract_lines.append('Latest release date: %s' % latest_release_info[0]['upload_time'].split('T')[0])

        for classifier in package_info['classifiers']:
            if classifier.startswith('Development Status'):
                abstract_lines.append('Development status: %s' % classifier.split(' - ')[-1])
                break

        out_file.write('\t'.join([
            package_info['name'],  # Title
            'A',  # Article type
            '',  # No redirect
            '',  # Other uses (ignored)
            '',  # No categories
            '',  # References (ignored)
            '',  # No related topics
            '',  # Further reading (ignored)
            '',  # External links (ignored)
            '',  # Disambiguation (ignored)
            '',  # No images
            '<br>'.join(abstract_lines),
            urllib.quote(package_info['release_url'], safe='/:'),  # Source url
        ]))
        out_file.write('\n')
