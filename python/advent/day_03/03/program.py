
from wiregrid import Wire, nearest_intersection, fastest_intersection

def main():

  paths = open("./wire_grid.txt").readlines()
  wire_1 = paths[0]
  wire_2 = paths[1]

  print("NEAREST :", nearest_intersection(wire_1, wire_2))
  print("FASTEST :", fastest_intersection(wire_1, wire_2))


main()