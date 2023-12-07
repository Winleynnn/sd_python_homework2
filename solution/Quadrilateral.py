from Figure import Figure
import numpy as np
import matplotlib.pyplot as plt
class Quadrilateral(Figure):
    def calculatePerimeter(self) -> float:
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        x3, y3 = self.points[2]
        x4, y4 = self.points[3]
        return (np.sqrt((x2 - x1)**2 + (y2 - y1)**2) +
                np.sqrt((x3 - x2)**2 + (y3 - y2)**2) +
                np.sqrt((x4 - x3)**2 + (y4 - y3)**2) +
                np.sqrt((x1 - x4)**2 + (y1 - y4)**2))
    
    def calculateSquare(self) -> float:
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        x3, y3 = self.points[2]
        x4, y4 = self.points[3]
        return 0.5 * abs(x1*y2 + x2*y3 + x3*y4 + x4*y1 - x2*y1 - x3*y2 - x4*y3 - x1*y4)
    
    def __str__(self) -> str:
        return f'Figure\'s type: {__class__.__name__}, points: {self.points}'
    
    def constructFromSeries(series) -> object:
        first_vertex = tuple(map(float, series[1].split(":")))
        second_vertex = tuple(map(float, series[2].split(":")))
        third_vertex = tuple(map(float, series[3].split(":")))
        fourth_vertex = tuple(map(float, series[4].split(":")))
        return Quadrilateral(points=(first_vertex, second_vertex, third_vertex, fourth_vertex))

    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        x = [point[0] for point in self.points + (self.points[0],)]  
        y = [point[1] for point in self.points + (self.points[0],)]  
        plt.plot(x, y, label="Quadrilateral")
        plt.title("Quadrilateral")
        plt.legend()
        plt.show()
        return None