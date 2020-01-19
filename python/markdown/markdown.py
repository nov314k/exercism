import re


def parse(markdown):
    lines = markdown.split('\n')
    html = ''
    in_list = False
    for line in lines:
        result = parse_line(line, in_list)
        html += result['line']
        in_list = result['in_list']
    if in_list:
        html += '</ul>'
    return html


def tag_surround(line, tag):
    return f'<{tag}>{line}</{tag}>'


def format_headers(line):
    pattern = '# (.*)'
    for index in range(6):
        if re.match(pattern, line):
            return tag_surround(line[(index + 2):], 'h' + str(index + 1))
        pattern = '#' + pattern
    return line


def format_bold_italic(line, mode='bold'):
    if mode == 'bold':
        pattern = f'(.*)__(.*)__(.*)'
        html_tag = 'strong'
    elif mode == 'italic':
        pattern = f'(.*)_(.*)_(.*)'
        html_tag = 'em'
    match = re.match(pattern, line)
    if match:
        return match.group(1) \
                   + tag_surround(match.group(2), html_tag) \
                   + match.group(3)
    else:
        return None


def parse_line(line, in_list):
    result = format_headers(line)

    for mode in ['bold', 'italic']:
        while format_bold_italic(result, mode=mode):
            result = format_bold_italic(result, mode=mode)

    # Indicates if we need to close a previously opened <ul>
    # before adding the current line
    close_list = False

    list_items = re.match(r'\* (.*)', result)
    if list_items:
        result = tag_surround(list_items.group(1), 'li')
        if not in_list:
            result = '<ul>' + result
            in_list = True
    else:
        if in_list:
            in_list = False
            # Postpone closing the list since
            # the order of operations is important
            close_list = True

    # There is no closing > after h, since it can be h[1-6]
    if not re.match('<h|<ul>|<li>', result):
        result = tag_surround(result, 'p')

    # Close previously opened <ul>
    # before adding the current line
    if close_list:
        result = '</ul>' + result

    return {
        'line': result,
        'in_list': in_list
    }
