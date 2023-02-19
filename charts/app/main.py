import read_csv
import utilities
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Type Country: =>  ')
  result = utilities.population_by_country(data, country)
  print(result)
  if len(result) > 0:
    country = result[0]
    labels, values = utilities.get_population(country)
  charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
  run()