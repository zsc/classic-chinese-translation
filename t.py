def proc(fname: str, fname2: str):
    ''' Read lines of two files and make pairs out of corresponding lines. '''
    with open(fname) as f:
        with open(fname2) as f2:
            lines = f.read().replace(' ', '').splitlines()
            lines2 = f2.read().replace(' ', '').splitlines()
            assert len(lines) == len(lines2)
            lines = [(lines[i], lines2[i]) for i in range(len(lines))]
            print(len(lines))

        # dedupe the line in lines by removing those that as first subelement as prefixes of others.
        # First sort the lines alphabetically by first subelement
        lines.sort(key=lambda x: x[0])

        lines = [lines[i] for i in range(len(lines)) if i == len(lines) - 1 or not lines[i + 1][0].startswith(lines[i][0])]

        arr = [{"instruction": "Translate the following sentence from Classic Chinese to Modern Chinese.", "input": x[0], "output": x[1]} for x in lines]
        # dump the arr as json into a file named fname.json
        import json
        with open(fname + '.json', 'w') as f:
            json.dump(arr, f, indent=4)

        print(len(lines))

        return lines

if __name__ == '__main__':
    lines = proc('train.src', 'train.tgt')
    # print random 10 entries from lines
    import random
    for i in range(10):
        print(random.choice(lines))
    from IPython import embed; embed()

