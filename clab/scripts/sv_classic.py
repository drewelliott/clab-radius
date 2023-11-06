from pysros.management import connect, sros

c = connect()

output = c.cli("//show version")


print("\n\n=========SHOW VERSION=========\n\n" + output)

