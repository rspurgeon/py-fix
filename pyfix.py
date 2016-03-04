import argparse
import operator

def build_map(record):
    soh = ''
    tid = '='
    kvps = record.split(soh)
    rv = dict()
    for kvp in kvps:
        tmp = kvp.split(tid)
        if len(tmp) > 1:
            key = tmp[0]
            value = tmp[1]
            rv[key] = value
    return rv

def build_messages(file):
    rv = []
    with open(file) as f:
        for record in f:
            rv.append(build_map(record))
    return rv

def get_unique_values(file, tag):
    unique_results = dict()
    all_msgs = build_messages(file)
    for msg in all_msgs:
        if tag in msg:
            value = msg[tag]
            if value not in unique_results:
                unique_results[value] = 1
            else:
                unique_results[value] += 1

    print("{0} unique results".format(len(unique_results)))
    for k, v in sorted(unique_results.items(), key=operator.itemgetter(1), reverse=True):
        print("{0}\t\tof {1}".format(str(v), str(k)))

    return unique_results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tag", help="Specify a tag to operate on")
    parser.add_argument(
        "-u", "--unique_values", help="Print the unique values for given tag (-t)",
        dest="getuniquevalues", action="store_true")
    parser.add_argument("file")
    args = parser.parse_args()

    if args.getuniquevalues:
        get_unique_values(args.file, args.tag)
    else:
        print(parser.print_help())

if __name__ == '__main__':
    main()
