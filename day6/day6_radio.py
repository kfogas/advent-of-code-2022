import re


def detect_duplicates(slice):
    for i in slice:
        matches = re.findall(i, slice)
        if len(matches) > 1:
            return True
    return False


def start_packet(data, marker_length):
    for i in range(len(data)):
        slice = data[i:i+marker_length]
        if not detect_duplicates(slice):
            return i+marker_length


if __name__ == '__main__':
    with open('input') as f:
        data = f.read()
        print(start_packet(data, 4))
        print(start_packet(data, 14))
