import subprocess
import dataclasses
from enum import Enum

@dataclasses.dataclass
class QData:
    warning: str
    status: str
    
class ParseWarningsQ:
    @classmethod
    def parse(self, gcc_path):
        try:
            res = subprocess.check_output(gcc_path + ' -Q --help=warnings')
        except:
            print("Error.")
            
        # print(res)

        tmps = res.splitlines()
        if not tmps[0].decode('utf-8').startswith('-'):
            tmps.pop(0)
            
        warnings = []

        for tmp in tmps:
            str = tmp.decode('utf-8')[2:]
            if str.startswith('-'):
                if not str.startswith('--') and not str.startswith('-W '):
                    warnings.append(str)
            else:
                if 0 < len(warnings):
                    warnings[-1] += " " + str.lstrip()

        ret = [] 
        for warning in warnings:
            splitedwarning = warning.split(" ", 1)
            deta = QData(warning = splitedwarning[0], status = splitedwarning[1].lstrip())
            ret.append(deta)

        return ret



