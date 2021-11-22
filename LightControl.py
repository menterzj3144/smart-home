from lifxlan import LifxLAN, BLUE


def main():
    print("Getting lights...\n")
    lan = LifxLAN()

    lights = lan.get_lights()
    print("Found", len(lights), "lights")

    for light in lights:
        print(light.get_color())
        light.set_color(BLUE)
        print(light.get_color(), "\n")


if __name__ == "__main__":
    main()
