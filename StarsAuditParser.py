from lxml.html import parse

while True:
    try:
        page = parse(input("Please enter audit file name (*.html): "))
        break
    except OSError:
        print("Cannot open file, try again.")

rows = page.xpath("body/table")[0].findall("tr")
data = []

for row in rows:
    data.append([c.text_content() for c in row.getchildren()])

count = 0
result = 0

start_rb = float(data[2][13]
                      .replace(',','')
                      .replace('.','')
                      .replace(' ',''))/10000

end_rb = float(data[-1][13]
                      .replace(',','')
                      .replace('.','')
                      .replace(' ',''))/10000

rakeback = end_rb - start_rb

for row in data[2:]:
    if ("[#?SpinGo#]" in row[3]) or ("Spin & Go" in row[3]):
        if '(' in row[5]:
            count += 1
        delta = float(row[5]
                      .replace('(','-')
                      .replace(')','')
                      .replace(',','')
                      .replace('.','')
                      .replace(' ',''))/100
        result += delta
    elif '(' in row[7]:
        rakeback += float(row[7]
                      .replace('(','')
                      .replace(')','')
                      .replace(',','')
                      .replace('.','')
                      .replace(' ',''))/10000


print("\nTotal number of Spin&Gos played: {}".format(count))
print("Total profit from Spin&Gos: ${:.2f}".format(result))
print("Total rakeback from StarsCoins: ${:.2f}".format(rakeback))

print("\nTotal profit+RB to split: ${:.2f}".format(result+rakeback))

input("\nPress enter to exit: ")