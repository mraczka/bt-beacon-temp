loops.everyInterval(10000, function () {
    basic.showIcon(IconNames.Heart)
    bluetooth.advertiseUrl(
    "Temperatura:" + convertToText(input.temperature()),
    7,
    false
    )
    basic.clearScreen()
})
