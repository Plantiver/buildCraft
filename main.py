import renderer as rend
import noiseGenerator as noG

def main():
    size = [128]*2
    r = rend.Renderer(size)
    n = noG.NoiseGenerator(size)
    n.blur(2)
    r.render(n.rendering())

if __name__ == "__main__":
    main()