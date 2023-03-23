shopping_list={"piekarnia":['chleb', 'pączek', 'bułki'],"warzywniak":['marchew', 'seler', 'rukola','brukselka']}
for key, value in shopping_list.items():
  print(f"Idę do {key.capitalize()}, kupuję tu następujące rzeczy:{[x.capitalize() for x in value]}")