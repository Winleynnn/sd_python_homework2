from Figure import Figure
from numpy import pi
import matplotlib.pyplot as plt
class Circle(Figure):
    def calculatePerimeter(self) -> float:
        return 2*pi*self.points[1]
    
    def calculateSquare(self) -> float:
        return pi*self.points[1]**2
    
    def __str__(self) -> str:
        return f'Figure\'s type: {__class__.__name__}, points: {self.points}'
    
    def constructFromSeries(series) -> object:
        center = tuple(map(float, series[1].split(":")))
        radius = float(series[2])
        return Circle(points=(center, radius))


    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        fig, ax = plt.subplots()
        circle = plt.Circle(self.points[0], self.points[1], label="Circle")
        ax.add_patch(circle)
        ax.set_aspect('equal', adjustable='box')
        ax.set_aspect( 1 )
        plt.title("Circle")
        plt.legend()
        plt.autoscale()
        plt.show()
        return None
    
