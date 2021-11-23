from lifxlan import LifxLAN, RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK, WHITE, COLD_WHITE, WARM_WHITE, GOLD


def main():
    lan = LifxLAN()

    stop = False
    while not stop:
        user = input("\nEnter light group name, type ALL for all lights, or Q to quit: ")
        if user == "q":
            break
        elif user.lower() == "all":
            lights = lan.get_lights()
        else:
            lights = lan.get_devices_by_group(user).get_device_list()

        if len(lights) == 0:
            print("Group does not exist/has no devices.")
        else:
            light_menu(lights)


def light_menu(lights):
    print("Found", len(lights), "light(s).")
    back = False
    while not back:
        print("\n1. Turn on/off lights")
        print("2. Set lights to color")
        print("3. Change light brightness")
        user = input("Enter choice, or B to go back: ")
        if user.lower() == "b":
            return

        if user == "1":
            set_power(lights)
        elif user == "2":
            set_color(lights)
        elif user == "3":
            change_brightness(lights)


def set_power(lights):
    for light in lights:
        power = light.get_power()
        if power == 0:
            light.set_power("on", False)
        else:
            light.set_power("off", False)


def set_color(lights):
    print("\n1. White")
    print("2. Red")
    print("3. Orange")
    print("4. Yellow")
    print("5. Green")
    print("6. Cyan")
    print("7. Blue")
    print("8. Purple")
    print("9. Pink")
    print("10. Cold White")
    print("11. Warm White")
    print("12. Gold")
    user = input("Select color: ")

    for light in lights:
        if light.supports_color():
            color = WHITE

            if user == "2":
                color = RED
            elif user == "3":
                color = ORANGE
            elif user == "4":
                color = YELLOW
            elif user == "5":
                color = GREEN
            elif user == "6":
                color = CYAN
            elif user == "7":
                color = BLUE
            elif user == "8":
                color = PURPLE
            elif user == "9":
                color = PINK
            elif user == "10":
                color = COLD_WHITE
            elif user == "11":
                color = WARM_WHITE
            elif user == "12":
                color = GOLD

            light.set_color(color)
        else:
            print(light.get_label(), "does not support color.")


def change_brightness(lights):
    user = int(input("\nEnter brightness percentage: "))
    if user < 0 or user > 100:
        print("Invalid brightness level.")
    else:
        brightness = user * .01 * 65535
        for light in lights:
            light.set_brightness(brightness, 2000, False)


if __name__ == "__main__":
    main()
