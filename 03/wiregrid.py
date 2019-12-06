
class Point():
  
  def __init__(self, x, y):
    self.x = x
    self.y = y  

  def manhattan_distance_from(self, other_point):
    xdist = abs(self.x - other_point.x)
    ydist = abs(self.y - other_point.y)
    return xdist + ydist
  
  def __eq__(self, value):
    return self.x == value.x and self.y == value.y

def next_point_up(point):
  return Point(point.x, point.y + 1)

def next_point_down(point):
  return Point(point.x, point.y - 1)

def next_point_left(point):
  return Point(point.x - 1, point.y)

def next_point_right(point):
  return Point(point.x + 1, point.y)

direction = {
  "U": next_point_up,
  "D": next_point_down,
  "L": next_point_left,
  "R": next_point_right,
}

def parse_points(path):
  commands = path.split(",")
  origin = Point(0,0)
  points = []
  for command in commands:
    move = direction[command[0]]
    scalar = int(command[1:])
    for ii in range(scalar):
      origin = move(origin)
      points.append(origin)

  return points

class Wire():

  def __init__(self, path):
    self.points = parse_points(path)

  def intersections_with(self, other_wire):
    intersections = []
    for point in self.points:
      for other_point in other_wire.points:
        if point == other_point:
          intersections.append(point)
    
    return intersections

ZERO = Point(0, 0)

def nearest_intersection(wire_a, wire_b):
    wire_a = Wire(wire_a)
    wire_b = Wire(wire_b)
    print("Wire a is %d points long" % len(wire_a.points))
    print("Wire b is %d points long" % len(wire_b.points))
    intersections = sorted(
      wire_a.intersections_with(wire_b), 
      key=ZERO.manhattan_distance_from
    )
    distance = ZERO.manhattan_distance_from(intersections[0])
    return distance
