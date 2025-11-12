# A simple exercise where I wanted to confirm the variables were scoped to the module.

str = "In main module"
print(str)

import investigate_module_scope_import

print(str)
