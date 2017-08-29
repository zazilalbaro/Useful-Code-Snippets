my_file = "C:/Users/Zazil/Documents/Adobe Web Data/fields.txt"

field = []

file_obj = open(my_file)

output_filename = 'C:/Users/Zazil/Documents/Adobe Web Data/schema_values.txt'
output = open(output_filename, 'w')

for line in file_obj.readlines():
  field.append(line.strip())

for eafield in field:
  print >> output, '{{"name":"{0}","type":"string"}},'.format(eafield)

output.close()




