
def classify_age(row):
    year = extractYear(row)
    return assignAge(year)

def extract_year(row):
  year_in_parens = re.compile('(?<=\()(\d{4})(?=\))')
  result = year_in_parens.search(row['title'])
  if result:
    return result.group(0)
  else: 
    return None
  
def assign_age(year):
    if year == None:
      return "unknown"
    year = dt.datetime(int(year), 1, 1)
    if year < dt.datetime(1970, 1, 1):
        return "old"
    elif year < dt.datetime(1990, 1, 1):
        return "medium"
    else:
        return "new"
        
