import data
    
class MargeWarnings:
    @classmethod
    def marge(self, warnq, warn):

        ret = []

        for i in range(len(warn)):
            lang = data.Warning.LANG.UNKNOWN
            if "[enabled]" in warnq[i].status:
                lang |= data.Warning.LANG.C
            elif "[disabled]" in warnq[i].status:
                lang |= data.Warning.LANG.C
            elif "[available in C++]" in warnq[i].status:
                lang |= data.Warning.LANG.CPP                              
            elif "[available in C++, ObjC++]" in warnq[i].status:
                lang |= data.Warning.LANG.CPP              
                lang |= data.Warning.LANG.OBJCPP              
            elif "[available in D]" in warnq[i].status:
                lang |= data.Warning.LANG.D                
            elif "[available in Go]" in warnq[i].status:
                lang |= data.Warning.LANG.GO
            elif "[available in Fortran]" in warnq[i].status:
                lang |= data.Warning.LANG.FORTRAN                
            elif "[available in ObjC, ObjC++]" in warnq[i].status:
                lang |= data.Warning.LANG.OBJC         
                lang |= data.Warning.LANG.OBJCPP         
            elif "c++" in warnq[i].status:
                lang |= data.Warning.LANG.CPP              
            else:
                lang |= data.Warning.LANG.C


            ret.append(data.Warning(warning = warn[i].warning, description = warn[i].description, lang = lang))

        return ret