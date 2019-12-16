
class Point():

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"Point({self.x}, {self.y})"

  def manhattan_distance_from(self, other_point):
    xdist = abs(self.x - other_point.x)
    ydist = abs(self.y - other_point.y)
    return xdist + ydist

  def __eq__(self, value):
    return self.x == value.x and self.y == value.y

def next_point_up(point, scalar=1):
  return Point(point.x, point.y + scalar)

def next_point_down(point, scalar=1):
  return Point(point.x, point.y - scalar)

def next_point_left(point, scalar=1):
  return Point(point.x - scalar, point.y)

def next_point_right(point, scalar=1):
  return Point(point.x + scalar, point.y)

direction = {
  "U": next_point_up,
  "D": next_point_down,
  "L": next_point_left,
  "R": next_point_right,
}

def parse_vertices(path):
  commands = path.split(",")
  origin = Point(0,0)
  points = []
  points.append(origin)
  for command in commands:
    move = direction[command[0]]
    scalar = int(command[1:])
    origin = move(origin, scalar)
    points.append(origin)
  return points


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

def between(a, o, b):
  a, b = sorted([a, b])
  return a <= o <= b

class Edge():

  def __init__(self, pointa, pointb):
    self.a = pointa
    self.b = pointb

  def intersection_with(self, other):
    if self.a.x == self.b.x and other.a.y == other.b.y:
      if between(self.a.y, other.a.y, self.b.y) and between(other.a.x, self.a.x, other.b.x):
        return Point(self.a.x, other.a.y), True
    if self.a.y == self.b.y and other.a.x == other.b.x:
      if between(self.a.x, other.a.x, self.b.x) and between(other.a.y, self.a.y, other.b.y):
        return Point(other.a.x, self.a.y), True
    return None, False

class Wire():

  def __init__(self, path):
    # self.points = parse_points(path)
    self.vertex = parse_vertices(path)

  def edges(self):
    for ii in range(1, len(self.vertex)):
      yield Edge(self.vertex[ii - 1], self.vertex[ii])

  def intersections_with(self, other_wire):
    intersections = []
    for edge in self.edges():
      for other_edge in other_wire.edges():
        intersection, hit = edge.intersection_with(other_edge)
        if hit:
          if ZERO != intersection:
            intersections.append(intersection)

    return intersections

ZERO = Point(0, 0)

def nearest_intersection(wire_a, wire_b):
    wire_a = Wire(wire_a)
    wire_b = Wire(wire_b)
    intersections = sorted(
      wire_a.intersections_with(wire_b),
      key=ZERO.manhattan_distance_from
    )
    distance = ZERO.manhattan_distance_from(intersections[0])
    return distance
