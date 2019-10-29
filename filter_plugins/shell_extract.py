import re
from ansible.module_utils.six import string_types


# We're not exactly rigorous here, but, there are a number
# of things we can say for sure don't include lines that we're interested
# in parsing.
def _is_var(line):
    if line.strip() == '}':
        return False
    if len(line) == 0:
        return False
    if line[0] == ' ' or line[0] == "\t":
        return False
    if "=" not in line:
        return False
    if line.startswith("BASH_FUNC"):
        return False
    return True


def split_lines(lines):
    if isinstance(lines, string_types):
        line_list = lines.split("\n")
    else:
        line_list = lines
    return [l.split("=", 1) for l in line_list if _is_var(l)]


def is_wanted(item, only):
    name = item[0]
    for regex in only:
        if re.match(regex, name):
            return True
    return False


def env_to_dict(env, only=[r'.*']):
    if isinstance(only, string_types):
        only = [only]
    splits = split_lines(env)
    parsed_env = {i[0]: i[1] for i in splits if is_wanted(i, only)}
    return parsed_env


class FilterModule(object):
    def filters(self):
        filters = {
            'env_to_dict': env_to_dict
        }

        return filters
