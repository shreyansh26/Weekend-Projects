import subprocess
import random
import struct
import sys

def load_file(fname):
    with open(fname, "rb") as f:
        return bytearray(f.read())

def save_file(fname, data):
    with open(fname, "wb") as f:
        f.write(data)

def mutate_bits(data):
    count = int(len(data) * 8 * 0.01)
    if count == 0:
        count = 10
    for _ in range(count):
        bit = random.randint(0, len(data)*8 - 1)
        idx_bit = bit % 8
        idx_byte = bit // 8
        data[idx_byte] ^= (int)(1 << idx_bit)
    return data

def mutate_bytes(data):
    count = int(len(data) * 0.01)
    if count == 0:
        count = 1
    for _ in range(count):
        data[random.randint(0, len(data)-1)] = random.randint(0, 255)
    return data

def mutate_magic(data):
    count = int(len(data) * 0.01)
    if count == 0:
        count = 1
    numbers = [
        (1, struct.pack("<B", 0xff)),               # malloc((unsigned char)(text_length + 1))
        (1, struct.pack("<B", 0x7f)),
        (1, struct.pack("<B", 0)),
        (2, struct.pack("<H", 0xffff)),
        (2, struct.pack("<H", 0)),
        (4, struct.pack("<I", 0xffffffff)),
        (4, struct.pack("<I", 0)),
        (4, struct.pack("<I", 0x80000000)),
        (4, struct.pack("<I", 0x40000000)),
        (4, struct.pack("<I", 0x7fffffff)),
    ]
    for _ in range(count):
        n_size, n = random.choice(numbers)
        sz = len(data) - n_size
        if sz < 0:
            continue
        idx = random.randint(0, sz)
        data[idx:idx+n_size] = bytearray(n)

    return data


def mutate(data):
    return random.choice([
        mutate_bits,
        mutate_bytes,
        mutate_magic
    ])(data[::])

def isPlausible(elf):
    subprocess.check_call(["./"+elf, "test.sample"], timeout=5)

def run(elf):
    p = subprocess.Popen(["gdb", "--batch", "-x", "detect.gdb", elf], 
        stdout=subprocess.PIPE,
        stderr=None)
    output, _ = p.communicate()
    if "Program received signal" in str(output):
        return str(output).split("aposkjd9081j239dnm023emtunficjsandf8123")[1]
    
    return None

input_samples = [
    load_file("input.sample")
]

i = 0
while True:
    i += 1
    if True:
        sys.stdout.write(".")
        sys.stdout.flush()

    mutated_sample = mutate(random.choice(input_samples))
    save_file("test.sample", mutated_sample)
    try:
        isPlausible("asdf")
    except subprocess.TimeoutExpired:
        print("No clue?!")
    except subprocess.CalledProcessError:
        print("CRASH!!!")
        output = run("asdf")
        save_file("crash.sample.%i" % i, mutated_sample)
        save_file("crash.samples.%i.txt" % i, bytearray(output, 'utf-8'))