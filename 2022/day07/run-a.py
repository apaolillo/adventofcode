from pprint import pprint
from typing import List, Tuple


# filename = 'example.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

fsd = dict()
fsd = {
    '.': fsd,
    '..': fsd,
}

cwd = fsd

mode_list = False
for line in lines:
    if line.startswith('$'):
        mode_list = False
        if line.startswith('$ cd '):
            new_dir = line[5:]
            if new_dir.startswith('/'):
                cwd = fsd
                new_dir = new_dir[1:]

            if new_dir:
                path = new_dir.split('/')
                for p in path:
                    if p not in cwd:
                        cwd[p] = dict()
                        cwd[p]['.'] = cwd[p]
                        cwd[p]['..'] = cwd
                    cwd = cwd[p]
        elif line.startswith('$ ls'):
            mode_list = True
    elif mode_list:
        if line.startswith('dir '):
            pass  # TODO?
        else:
            size, name = line.split()
            actual_size = int(size)
            if not size.isdigit():
                raise ValueError('unable to parse size')
            if name in cwd:
                expected_size = cwd[name]
                if expected_size != actual_size:
                    raise ValueError(f'incoherent size of {name}: {expected_size} {actual_size}')
            else:
                cwd[name] = actual_size
    else:
        raise ValueError('unable to parse')

pprint(fsd, indent=4)


def size(d) -> int:
    if type(d) == int:
        return d

    sizes = [size(d[n]) for n in d if n not in ['.', '..']]
    # atmost_sizes = [e if e <= atmost else 0 for e in sizes]
    return sum(sizes)


def all_dirs(d) -> List[Tuple[str, int]]:
    if type(d) == int:
        return []
    result = []
    for k, v in d.items():
        if type(v) != int and k not in ['.', '..']:
            result += [(k, size(v))] + all_dirs(v)
    return result


dirs = all_dirs(fsd)
pprint(dirs)
atmost = 100000
result_a = sum([e[1] for e in dirs if e[1] <= atmost])
print(result_a)

total_size = 70000000
total_required_size = 30000000
fs_size = size(fsd)
required_size = total_required_size - (total_size - fs_size)
print(required_size)

result_b = sorted([e[1] for e in dirs if e[1] >= required_size])[0]
print(result_b)
