import parse_warnings
import parse_warnings_q
import marge_warnings
import data
import generator
import sys
import os

def main():

    argc = len(sys.argv)
    if 3 != argc:
        print("")
        print("usage:")
        print("python main.py path_to_your_gcc save_file_name")
        return -1

    gcc_path = sys.argv[1]
    save_file_name = sys.argv[2]

    pwq = parse_warnings_q.ParseWarningsQ()
    pwqData = pwq.parse(gcc_path)

    pw = parse_warnings.ParseWarnings()
    pwData = pw.parse(gcc_path)

    mg = marge_warnings.MargeWarnings()
    margedData = mg.marge(pwqData, pwData)

    save_path = os.getcwd() + "\\" + save_file_name
    gen = generator.CmakeGenerator.generate(margedData, save_path)

    print("generated " + save_file_name + " at " + os.getcwd())
    return 0


if __name__ == "__main__":
    main()