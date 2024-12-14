import numpy as np
from scipy.ndimage import gaussian_filter


class NoiseGenerator:
    def __init__(self, size:tuple[int,int]):
        self.size = size
        self.noise = np.random.random(size)
    def __str__(self):
        return str(self.noise)
    def rendering(self):
        return np.array([(self.noise*255).astype(int)]*3).swapaxes(0,2)#.reshape(self.size+[3])
    def blur(self, sigma):
        self.noise = gaussian_filter(self.noise, sigma)

if __name__=="__main__":
    t = NoiseGenerator([16]*2)
    print(t.rendering())