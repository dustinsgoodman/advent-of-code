"""Solution to Day 13"""
from ast import literal_eval
from functools import cmp_to_key

DIVIDER_PACKETS = [
    [[2]],
    [[6]],
]


def get_packet_pairs(file):
    """get packet pairs from input"""
    pairs = []
    pair = []
    for line in file:
        if line.strip() == '':
            pairs.append(pair)
            pair = []
            continue
        pair.append(literal_eval(line.strip()))

    pairs.append(pair)
    return pairs


def list_of_packets(file):
    """get all packets from input"""
    packets = [packet for packet in DIVIDER_PACKETS]
    for line in file:
        if line.strip() == '':
            continue
        packets.append(literal_eval(line.strip()))

    return packets


def is_int(val):
    """return true if val is int"""
    return isinstance(val, int)


def is_list(val):
    """return true if val is list"""
    return isinstance(val, list)


def is_boolean(val):
    """return true if val is bool"""
    return isinstance(val, bool)


def is_packet_valid(left, right):
    """determine if a packet is valid"""
    left_len = len(left)
    right_len = len(right)
    for idx in range(min([len(left), len(right)])):
        left_val = left[idx]
        right_val = right[idx]
        if is_int(left_val) and is_int(right_val):
            if left_val < right_val:
                return True
            elif left_val > right_val:
                return False
        elif is_list(left_val) and is_list(right_val):
            ret = is_packet_valid(left_val, right_val)
            if is_boolean(ret):
                return ret
        else:
            if is_int(left_val):
                ret = is_packet_valid([left_val], right_val)
                if is_boolean(ret):
                    return ret
            elif is_int(right_val):
                ret = is_packet_valid(left_val, [right_val])
                if is_boolean(ret):
                    return ret

    if left_len < right_len:
        return True
    elif left_len > right_len:
        return False

    return None


def packet_compare(left, right):
    """convert packet validation to compare func"""
    if is_packet_valid(left, right):
        return -1
    else:
        return 1


def main():
    """Program main"""
    # part 1
    with open('input.txt', encoding="utf8") as file:
        pairs = get_packet_pairs(file)

    valid_packets = 0
    for pair_idx, pair in enumerate(pairs):
        left, right = pair
        if is_packet_valid(left, right):
            valid_packets += (pair_idx + 1)

    print(valid_packets)

    # part 2
    with open('input.txt', encoding="utf8") as file:
        packets = list_of_packets(file)

    packets = sorted(packets, key=cmp_to_key(packet_compare))
    result = 1
    for packet_idx, packet in enumerate(packets):
        if packet in DIVIDER_PACKETS:
            result *= (packet_idx + 1)
    print(result)


main()
