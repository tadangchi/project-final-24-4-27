function Nhietdodoam_DHT11 () {
    dht11_dht22.selectTempType(tempType.celsius)
    nhietdo = dht11_dht22.readData(dataType.temperature)
    doam = dht11_dht22.readData(dataType.humidity)
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P2,
    false,
    false,
    true
    )
    if (dht11_dht22.readDataSuccessful()) {
        I2C_LCD1602.ShowString("Nhiet do:" + Math.round(nhietdo), 0, 0)
        I2C_LCD1602.ShowString("Do am:" + Math.round(doam), 0, 1)
        basic.pause(1000)
    } else {
        I2C_LCD1602.ShowString("Do am" + "Khong co gia tri", 0, 1)
        basic.pause(500)
        basic.showIcon(IconNames.No)
    }
}
function F_anhsang () {
    V_anhsang = pins.analogReadPin(AnalogPin.P1)
    I2C_LCD1602.ShowString("A sang: " + Math.round(V_anhsang), 0, 1)
    basic.pause(500)
}
function chuyendong () {
    cd = pins.analogReadPin(AnalogPin.P0)
    I2C_LCD1602.ShowString("Chuyen dong: " + Math.round(cd), 0, 1)
    basic.pause(500)
}
function Khigas () {
    nongdokhigas = pins.analogReadPin(AnalogPin.P3)
    basic.showNumber(nongdokhigas)
    I2C_LCD1602.ShowString("Khi: " + Math.round(nongdokhigas), 0, 0)
    if (nongdokhigas < 500) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
    basic.pause(500)
}
function Module_Relay_1_Kênh () {
	
}
function Sieuam (KC: number) {
    makerbit.connectUltrasonicDistanceSensor(DigitalPin.P15, DigitalPin.P14)
    KC_SIEUAM = makerbit.getUltrasonicDistance(DistanceUnit.CM)
    if (KC_SIEUAM < KC) {
        I2C_LCD1602.ShowString("Co: " + Math.round(KC_SIEUAM), 0, 0)
        basic.showNumber(makerbit.getUltrasonicDistance(DistanceUnit.CM))
    } else {
        I2C_LCD1602.ShowString("Khong: " + Math.round(KC_SIEUAM), 0, 0)
        basic.showNumber(makerbit.getUltrasonicDistance(DistanceUnit.CM))
    }
}
let KC_SIEUAM = 0
let nongdokhigas = 0
let cd = 0
let V_anhsang = 0
let doam = 0
let nhietdo = 0
I2C_LCD1602.LcdInit(39)
I2C_LCD1602.on()
I2C_LCD1602.BacklightOn()
I2C_LCD1602.BacklightOn()
chuyendong()
I2C_LCD1602.clear()
Sieuam(80)
I2C_LCD1602.clear()
Nhietdodoam_DHT11()
I2C_LCD1602.clear()
F_anhsang()
I2C_LCD1602.clear()
Khigas()
I2C_LCD1602.clear()
basic.forever(function () {
    chuyendong()
    I2C_LCD1602.clear()
    Sieuam(80)
    I2C_LCD1602.clear()
    Nhietdodoam_DHT11()
    I2C_LCD1602.clear()
    F_anhsang()
    I2C_LCD1602.clear()
    Khigas()
    I2C_LCD1602.clear()
})
