from Figure import Figure
import matplotlib.pyplot as plt
class Rectangle(Figure):
    def calculatePerimeter(self) -> float:
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        return 2 * (abs(x2 - x1) + abs(y2 - y1))
    
    def calculateSquare(self) -> float:
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        return abs(x2 - x1) * abs(y2 - y1)
    
    def __str__(self) -> str:
        return f'Figure\'s type: {__class__.__name__}, points: {self.points}'
    
    def constructFromSeries(series) -> object:
        left_bottom_vertex = tuple(map(float, series[1].split(":")))
        right_up_vertex = tuple(map(float, series[2].split(":")))
        return Rectangle(points=(left_bottom_vertex, right_up_vertex))

    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        plt.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], label="Rectangular")
        plt.title("Rectangular")
        plt.legend()
        plt.show()
        return None