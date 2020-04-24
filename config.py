#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Global constants and settings
scanner = {
    'cookie': '',  # Cookie string used in session
    'protocol': 'http',  # Protocol used (http/https)
    'maximum_id': 99999  # Maximum ID, i.e. http://domain/wp/XXXXX.html
}

analyzer = {
    # Search only between
    # <div class="entry-content">...</div>
    'search_content_only': True,
    'magnet_prefix': 'magnet:?xt=urn:btih:',  # Prefix of magnet links
    'regex_title': r'<title>(.+?)</title>',  # Regex of title tag
    # Regex of content
    'regex_content': r'<article(.*?)<div class="entry-header">',
    # Regex of 40-char magnet link
    'regex_magnets_40': r'[^0-9a-fA-F/]([0-9a-fA-F]{40})[^0-9a-fA-F/]',
    # Regex of 32-char magnet link
    'regex_magnets_32': r'[^0-9a-zA-Z/]([0-9a-zA-Z]{32})[^0-9a-zA-Z/]'
}

output = {
    'json_indent': 4,  # Indent used in JSON
    'json_sort_keys': True,  # Sort keys in JSON object
    'json_ensure_ascii': False,  # Use Unicode characters instead of escaped ones
    'txt_magnet_prefix': '\t'  # Indent used before magnet links in text file
}
