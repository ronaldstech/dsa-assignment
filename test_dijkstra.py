import contextlib
import io
import unittest

import dijkstra


class DijkstraTests(unittest.TestCase):

    def test_route_from_town_to_itself_has_zero_distance(self):
        self.assertEqual(
            dijkstra.dijkstra(dijkstra.graph, "Lilongwe", "Lilongwe"),
            (0, ["Lilongwe"]),
        )

    def test_known_route_in_malawi_graph(self):
        result = dijkstra.dijkstra(dijkstra.graph, "Chitipa", "Blantyre")

        self.assertIsNotNone(result)
        distance, path = result
        self.assertEqual(distance, 1080)
        self.assertEqual(path[0], "Chitipa")
        self.assertEqual(path[-1], "Blantyre")

    def test_unknown_town_returns_none_and_prints_error(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = dijkstra.dijkstra(dijkstra.graph, "Unknown", "Blantyre")

        self.assertIsNone(result)
        self.assertIn("Error: Town not found in the graph.", output.getvalue())

    def test_display_result_prints_route_and_distance(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            dijkstra.display_result("Chitipa", "Blantyre")

        self.assertIn("Chitipa -> Karonga", output.getvalue())
        self.assertIn("Shortest distance: 1080 km", output.getvalue())


if __name__ == "__main__":
    unittest.main()
