import networkx as nx
import pygeoip
import sys

def lookUpCountryOne(inIP):
  GEOIP = pygeoip.GeoIP(sys.argv[2], pygeoip.MEMORY_CACHE)
  country = GEOIP.country_name_by_addr(inIP)
  return country

def load_and_display_file(filepath):
  graph1 = nx.read_graphml(filepath)
  
  print(graph1)
  
  all_nodes = graph1.nodes()
  print('# of Nodes:', len(all_nodes()))
  
  all_edges = graph1.edges()
  print('# of Edges', len(all_edges))
  max_degree = max(graph1.degree(node) for node in all_nodes())
  min_degree = min(graph1.degree(node) for node in all_nodes())
  
  print('max degree', max_degree)
  for node in all_nodes:
    if(graph1.degree(node) == max_degree):
      print("Max Nodes:" + node + ":degree = ", + graph1.degree(node))

  print('min degree', min_degree)
  for node in all_nodes:
    if(graph1.degree(node) == min_degree):
      print("Min Nodes:" + node + ":degree = ", + graph1.degree(node))

  print("10 Nodes highest degree desc:")
  sorted_nodes = sorted(graph1.degree, key=lambda x: x[1], reverse=True)
  count = 0
  while (count < 10):
    node_ip = sorted_nodes[count][0]
    node_degree = sorted_nodes[count][1]
    node_country = lookUpCountryOne(node_ip)
    print("Node IP:" + node_ip + " Node degree:" + str(node_degree) + " Country: " + node_country)
    count = count + 1

  dict = {}
  print("Top 5 countries most nodes:")
  for node in sorted_nodes:
    node_ip = node[0]
    node_country = lookUpCountryOne(node_ip)
    if node_country in dict:
      dict[node_country] = dict[node_country] + 1
    else:
      dict[node_country] = 1
  
  sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
  count = 0
  while (count < 5):
    print(sorted_dict[count][0] + ":" + str(sorted_dict[count][1]))
    count = count + 1

def main():
  load_and_display_file(sys.argv[1])

if __name__ == "__main__":
  main()

