def local_func():
    var_nonlocal = 22
    def local_inner():
        global var_global
        nonlocal var_nonlocal
        var_global = 111
        var_nonlocal = 222

    local_inner()
    print('local_func output var_global: ', var_global)
    print('local_func output var_nonlocal: ', var_nonlocal)

var_global = 1
var_nonlocal = 2
print('main output var_global: ', var_global)
print('main output var_nonlocal: ', var_nonlocal)
local_func()
print('main output var_global: ', var_global)
print('main output var_nonlocal: ', var_nonlocal)