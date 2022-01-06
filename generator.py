import data


class CmakeGenerator:
    @classmethod
    def generate(self, warnings, save_path):
        with open(save_path, mode='w') as f:
            f.write("GCWFM_C_FLAGS = \"\"\n")
            f.write("GCWFM_CXX_FLAGS = \"\"\n")
            f.write("\n\n")
            for item in warnings:
                if item.lang & data.Warning.LANG.C:
                    f.write("# " + item.description + "\n")
                    f.write("GCWFM_C_FLAGS += " + "-Werror=" + item.warning.lstrip('-W') + "\n")
                elif item.lang & data.Warning.LANG.CPP:
                    f.write("# " + item.description + "\n")
                    f.write("GCWFM_CXX_FLAGS += " + "-Werror=" + item.warning.lstrip('-W') + "\n")

            f.write("\n\n")
