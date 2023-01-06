def on_every_interval():
    basic.show_icon(IconNames.HEART)
    bluetooth.advertise_url("temperatura:" + convert_to_text(input.temperature()) + " stopni celcjusza",
        7,
        False)
    basic.clear_screen()
loops.every_interval(10000, on_every_interval)
