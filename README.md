# gcwfm

This script creates a makefile that changes the gcc warning to error.

# usage

```
python main.py path_to_your_gcc save_file_name
```

# output sample

```
GCWFM_C_FLAGS = ""
GCWFM_CXX_FLAGS = ""


# Warn if the NSObject attribute is applied to a non-typedef.
GCWFM_C_FLAGS += -Werror=NSObject-attribute
# Warn about things that will change when compiling with an ABI-compliant compiler.
GCWFM_C_FLAGS += -Werror=abi
# Warn if a subobject has an abi_tag attribute that the complete object type does not have.
GCWFM_CXX_FLAGS += -Werror=abi-tag
# Warn about things that change between the current -fabi-version and the specified version.
GCWFM_C_FLAGS += -Werror=abi=
# Warn on suspicious calls of standard functions computing absolute values.
GCWFM_C_FLAGS += -Werror=absolute-value
# Warn about suspicious uses of memory addresses.
GCWFM_C_FLAGS += -Werror=address
# Warn when the address of packed member of struct or union is taken.
GCWFM_C_FLAGS += -Werror=address-of-packed-member
・・・
```

And then, please edit the details manually.

for example:

```
GCWFM_C_FLAGS += -Werror=alloc-size-larger-than=<bytes>
```
to
```
GCWFM_C_FLAGS += -Werror=alloc-size-larger-than=10485760
```