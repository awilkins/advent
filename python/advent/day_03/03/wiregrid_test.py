
import unittest

from wiregrid import Point, Wire, nearest_intersection, fastest_intersection


class TestGrid(unittest.TestCase):

  def test_manhattan_distance(self):
    point_a = Point(0, 0)
    point_b = Point(1, 2)
    self.assertEqual(3, point_a.manhattan_distance_from(point_b))

  def test_case_one(self):
    self.assertEqual(6, nearest_intersection("R8,U5,L5,D3", "U7,R6,D4,L4"))
    self.assertEqual(30, fastest_intersection("R8,U5,L5,D3", "U7,R6,D4,L4"))

  def test_case_two(self):
    self.assertEqual(159, nearest_intersection(
      "R75,D30,R83,U83,L12,D49,R71,U7,L72",
      "U62,R66,U55,R34,D71,R55,D58,R83"
      )
    )
    self.assertEqual(610, fastest_intersection(
      "R75,D30,R83,U83,L12,D49,R71,U7,L72",
      "U62,R66,U55,R34,D71,R55,D58,R83"
      )
    )

  def test_case_three(self):
    self.assertEqual(135, nearest_intersection(
      "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
      "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
      )
    )
    self.assertEqual(410, fastest_intersection(
      "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
      "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
      )
    )