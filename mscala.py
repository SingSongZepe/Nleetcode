import os
import sys
import subprocess
import typing

LC_ = 'lc'
_SCALA_ = '_scala'

LC_SCALA_TEMPLATE_ = 'lc_scala_template'

def make_template(index) -> bool:
    powershell_command = f"copy {LC_SCALA_TEMPLATE_} ./lc{index}_scala -recurse"
    result = subprocess.run(["powershell", "-Command", powershell_command], shell=True)
    if result.returncode == 0:
        return True
    else:
        return False

def find_index() -> int:
    index = 1
    while os.path.exists(LC_ + str(index) + _SCALA_):
        index += 1
    return index

def exist_index(index) -> bool:
    return os.path.exists(LC_ + str(index) + _SCALA_)

def main() -> int:
    if not os.path.exists(LC_SCALA_TEMPLATE_):
        raise Exception('lc_template not found, may be deleted or renamed.')

    # get indecies
    indexes: typing.List[str] = []
    if len(sys.argv) > 1: # has a 1
        for p in sys.argv[1:]:
            if not p.isnumeric():
                lcs = p.split('-')
                if len(lcs) == 2 and lcs[0].isnumeric() and lcs[1].isnumeric():
                    for i in range(int(lcs[0]), int(lcs[1])+1):
                        if exist_index(str(i)):
                            print(f'WARNING: lc{i}_scala already exists. will not create.')
                            continue
                        indexes.append(str(i))
                else:
                    raise("unknown parameter")
            else:
                if exist_index(p):
                    print(f'WARNING: lc{p}_scala already exists. will not create.')
                    continue
                indexes.append(p)
    else:
        indexes.append(find_index())

    # print(indexes)
    if len(indexes) == 0:
        print('No index specified or found.')
        return 1 # error code
    
    for index in indexes:
        if make_template(index):
            print(f'lc{index}_scala created successfully.')
        else:
            print(f'Failed to create lc{index}_scala.')
    
    return 0


if __name__ == '__main__':
    main()
