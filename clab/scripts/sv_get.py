from pysros.management import connect
from pysros.pprint import printTree

c = connect()

output = c.running.get("/state/system/version")
output = output['version-string'].data
output = output.split("\n")

print("\n\n=========SHOW VERSION FROM STATE YANG=========\n\n")
print(output)
for x in output:
    print(x)
