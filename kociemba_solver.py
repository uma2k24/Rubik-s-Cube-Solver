import time
import kociemba

start = time.time()
string = 'ULLFBBUBBRRBUUURRBFUUFLLRUUDFFBFFDRRLDLLDLFDFDDBRRBDDL'
print(kociemba.solve(string))
end = time.time()
print(end - start)