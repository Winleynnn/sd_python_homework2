from Figure import Figure
import matplotlib.pyplot as plt
class Square(Figure):
    def calculatePerimeter(self) -> float:
        return 4*self.points[1]
    
    def calculateSquare(self) -> float:
        return self.points[1]**2
    
    def __str__(self) -> str:
        return f'Figure\'s type: {__class__.__name__}, points: {self.points}'
    
    def constructFromSeries(series) -> object:
        left_bottom_vertex = tuple(map(float, series[1].split(":")))
        side_len = float(series[2])
        return Square(points=(left_bottom_vertex, side_len))


    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        x1, y1 = self.points[0]
        side_length = self.points[1]
        x = [x1, x1 + side_length, x1 + side_length, x1, x1]  
        y = [y1, y1, y1 + side_length, y1 + side_length, y1]  
        plt.plot(x, y, label="Square")
        plt.title("Square")
        plt.legend()
        plt.axis('equal')
        plt.show()
        return None