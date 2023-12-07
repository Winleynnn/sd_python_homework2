from Figure import Figure
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
class Ellipse(Figure):
    def calculatePerimeter(self) -> float:
        integrand = lambda t: np.sqrt((self.points[1] * np.sin(t))**2 + (self.points[2] * np.cos(t))**2)
        length, _ = quad(integrand, 0, 2 * np.pi)
        return length
    
    def calculateSquare(self) -> float:
        return np.pi*self.points[1]*self.points[2]
    
    def __str__(self) -> str:
        return f'Figure\'s type: {__class__.__name__}, points: {self.points}'
    
    def constructFromSeries(series) -> object:
        center = tuple(map(float, series[1].split(":")))
        a_curve = float(series[2])
        b_curve = float(series[3])
        return Ellipse(points=(center, a_curve, b_curve))


    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        center = self.points[0]
        a, b = self.points[1], self.points[2]

        theta = np.linspace(0, 2*np.pi, 100)
        x = center[0] + a * np.cos(theta)
        y = center[1] + b * np.sin(theta)

        plt.plot(x, y, label="Ellipse")
        plt.title("Ellipse")
        plt.legend()
        plt.show()
        return None