import llvmlite.ir as ir
import llvmlite.binding as llvm

#loading a lib perm llvmlite.binding.load_library_permanently

# Create a module with a function definition
module = ir.Module(name="example")
func_type = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)])
func = ir.Function(module, func_type, name="add_func")

# Function arguments
a, b = func.args
a.name = 'a'
b.name = 'b'

# Function body
block = func.append_basic_block(name='entry')
builder = ir.IRBuilder(block)

# The function body simply adds the two arguments and returns the result
result = builder.add(a, b, name='result')
builder.ret(result)

# Convert textual LLVM IR into an in-memory representation
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

target = llvm.Target.from_default_triple()
target_machine = target.create_target_machine()
compiled_mod = llvm.parse_assembly(str(module))
engine = llvm.create_mcjit_compiler(compiled_mod, target_machine)

# Now we can access the function as if it were a regular Python function
add_func = engine.get_function_address('add_func')

from ctypes import CFUNCTYPE, c_int32

cfunc = CFUNCTYPE(c_int32, c_int32, c_int32)(add_func)

# Now we can call the function
print('1 + 2 =', cfunc(1, 2))  # prints: 1 + 2 = 3