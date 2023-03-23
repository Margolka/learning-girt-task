shopping_list={"piekarnia":['chleb', 'pączek', 'bułki'],"warzywniak":['marchew', 'seler', 'rukola','brukselka']}
total_items=0
for key, value in shopping_list.items():
  print(f"Idę do {key.capitalize()}, kupuję tu następujące rzeczy:{[x.capitalize() for x in value]}")
  total_items=total_items+len(value)
print(f"W sumie kupuję {total_items} produktów")