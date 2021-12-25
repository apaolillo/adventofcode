from __future__ import annotations

# from typing import Union
# from functools import reduce
# from pprint import pprint
from collections import deque


def distance(p0, p1):
    x0, y0, z0 = p0
    x1, y1, z1 = p1
    result = ((x0-x1)**2) + ((y0-y1)**2) + ((z0-z1)**2)
    return result


def manh_dist(p0, p1):
    x0, y0, z0 = p0
    x1, y1, z1 = p1
    result = (abs(x0-x1)) + (abs(y0-y1)) + (abs(z0-z1))
    return result

def get_distances_from(p0, points):
    return sorted([distance(p0, p1) for p1 in points])


def get_distances(points):
    return {p: get_distances_from(p, points) for p in points}


def vector_prod(v1, v2):
    return tuple(e1 * e2 for e1, e2 in zip(v1, v2))


def vector_sub(v1, v2):
    return tuple(e1 - e2 for e1, e2 in zip(v1, v2))


def vector_add(v1, v2):
    return tuple(e1 + e2 for e1, e2 in zip(v1, v2))


def transfo(i, point):
    x, y, z = point
    if 0 == i:
        return x, y, z
    elif 1 == i:
        return x, z, y
    elif 2 == i:
        return y, x, z
    elif 3 == i:
        return y, z, x
    elif 4 == i:
        return z, x, y
    elif 5 == i:
        return z, y, x
    else:
        raise ValueError(f'Unknown transo id {i}')


def apply_transfo(src_points,
                  direction,
                  transfo_nb):
    tmp_points = [vector_prod(p, direction) for p in src_points]
    dst_points = [transfo(i=transfo_nb, point=p) for p in tmp_points]
    return dst_points


def apply_shift(src_points,
                shift):
    dst_points = [vector_add(p, shift) for p in src_points]
    return dst_points




def find_overlapping_beacons(points0,
                             points1):
    distances0 = get_distances(points0)
    distances1 = get_distances(points1)
    matching_points = []
    for p0 in points0:
        distances_p0 = distances0[p0]
        for p1 in points1:
            distances_p1 = distances1[p1]
            overlapping_distances = [d for d in distances_p1 if d in distances_p0]
            if len(overlapping_distances) >= 12:
                matching_points.append((p0, p1))

    if len(matching_points) == 0:
        return False, 0, 0, 0

    p0m = [p[0] for p in matching_points]
    p1m = [p[1] for p in matching_points]

    for direction in [
        (1,  1,  1),
        (1,  1, -1),
        (1, -1,  1),
        (1, -1, -1),
        (-1,  1,  1),
        (-1,  1, -1),
        (-1, -1,  1),
        (-1, -1, -1),
    ]:
        for transfo_nb in range(6):
            p1mt = apply_transfo(p1m, direction, transfo_nb)
            shifts = [vector_sub(p0, p1) for p0, p1 in zip(p0m, p1mt)]
            different_shifts = len(set(shifts))
            if different_shifts == 1:
                the_transfo = transfo_nb
                the_direction = direction
                the_shift = sorted(set(shifts))[0]
                return True, the_transfo, the_direction, the_shift


def usecase(filename):
    with open(filename, 'r') as input_file:
        fc = input_file.readlines()
    i = 0
    scanners = dict()
    while i < len(fc):
        line = fc[i].strip()
        scan_id = int(line.split('scanner')[-1].split('---')[0])
        scanners[scan_id] = []
        i += 1
        while i < len(fc) and (line := fc[i].strip()) != '':
            x, y, z = [int(e.strip()) for e in line.split(',')]
            scanners[scan_id].append((x, y, z))
            i += 1
        i += 1

    # f1, t1, d1, s1 = find_overlapping_beacons(scanners[0], scanners[1])
    # f4, t4, d4, s4 = find_overlapping_beacons(scanners[1], scanners[4])
    # s14 = apply_transfo([s4], d1, t1)[0]
    # s04 = vector_add(s1, s14)
    # print(s04)

    nb_scanners = len(scanners)

    marked = {i: False for i in range(nb_scanners)}
    succ = dict()
    queue = deque()
    queue.append(0)
    while len(queue) > 0:
        i = queue.popleft()
        marked[i] = True
        for j in range(nb_scanners):
            if not marked[j]:
                f, t, d, s = find_overlapping_beacons(scanners[i], scanners[j])
                if f:
                    if i not in succ:
                        succ[i] = []
                    succ[i].append((j, t, d, s))
                    queue.append(j)
    assert all([marked[i] for i in range(nb_scanners)])
    assert len(queue) == 0

    compute_beacons(scanners=scanners, succ=succ)


def compute_beacons(scanners, succ):
    nb_scanners = len(scanners)
    beacons = dict()
    queue = deque()
    queue.append((0, []))
    marked = {i: False for i in range(nb_scanners)}
    scanners_pos_0 = dict()
    while len(queue) > 0:
        v, transforms = queue.popleft()
        marked[v] = True

        # apply transforms and mark beacons
        dst_points = scanners[v] + [(0,0,0)]
        for (t, d, s) in transforms:
            dst_points = apply_transfo(dst_points, d, t)
            dst_points = apply_shift(dst_points, s)
        origin = dst_points[-1]  # relative to scanner 0
        scanners_pos_0[v] = origin
        for point in dst_points[:-1]:  # we remove origin added earlier
            if point not in beacons:
                beacons[point] = 0
            beacons[point] += 1
        if v in succ:
            for w, t, d, s in succ[v]:
                if not marked[w]:
                    queue.append((w, [(t, d, s)] + transforms))

    mds = []
    for i in range(nb_scanners):
        for j in range(nb_scanners):
            mds.append(manh_dist(scanners_pos_0[i], scanners_pos_0[j]))
    print(len(beacons), max(mds))


def main():
    usecase('sample-input.txt')
    usecase('input.txt')


if __name__ == '__main__':
    main()
