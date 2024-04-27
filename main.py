from microbit import *
# Các chân kết nối cảm biến và thiết bị ngoại vi
temperature_pin = pin0 #Nhiệt
light_pin = pin1 #ánh sáng
motion_pin = pin13 #siêu âm bắt chuyển động
smoke_sensor_pin = pin3 #khói bụi mịn
gas_sensor_pin = pin4 #khí ga
speaker_pin = pin8 #speaker
#pin 10 đèn xanh
#pin 11 đèn vàng
#pin 12 đèn đỏ
#pin 13 gắn đèn leb có chỉnh sáng

# Hàm đọc giá trị từ cảm biến nhiệt độ
def read_temperature():
    temperature_value = temperature_pin.read_analog()  # Đọc giá trị từ cảm biến
    return temperature_value

# Hàm điều chỉnh ánh sáng LED dựa trên giá trị nhiệt độ
def adjust_light_based_on_temperature():
    '''
    temperature = read_temperature()
    # Chuyển đổi giá trị nhiệt độ thành mức sáng cho đèn LED (0-9)
    brightness = int(temperature / 1023 * 9)
    display.set_brightness(brightness)
'''
    green_led_pin = pin10
    yellow_led_pin = pin11
    red_led_pin = pin12
    temp_value = temp_pin.read_analog()  # Đọc giá trị nhiệt độ
    if temp_value < 256:  # Nhiệt độ thấp
        display.show(Image.CHESSBOARD)  # Hiển thị màu xanh
        green_led_pin.write_digital(1)  # Bật đèn LED xanh
        yellow_led_pin.write_digital(0)  # Tắt đèn LED vàng
        red_led_pin.write_digital(0)  # Tắt đèn LED đỏ
    elif temp_value < 512:  # Nhiệt độ trung bình
        display.show(Image.HAPPY)  # Hiển thị màu vàng
        green_led_pin.write_digital(0)  # Tắt đèn LED xanh
        yellow_led_pin.write_digital(1)  # Bật đèn LED vàng
        red_led_pin.write_digital(0)  # Tắt đèn LED đỏ
    else:  # Nhiệt độ cao
        display.show(Image.SAD)  # Hiển thị màu đỏ
        green_led_pin.write_digital(0)  # Tắt đèn LED xanh
        yellow_led_pin.write_digital(0)  # Tắt đèn LED vàng
        red_led_pin.write_digital(1)  # Bật đèn LED đỏ

# Hàm kiểm tra mức độ ánh sáng và bật/tắt đèn
def check_light_and_control():
    light_level = light_pin.read_analog()  # Đọc mức độ ánh sáng
    if light_level < 200:  # Giả định ngưỡng ánh sáng để bật đèn
        display.show(Image.YES)  # Hiển thị biểu tượng đèn bật trên màn hình
        pin13.write_digital(1)  # Bật đèn LED trên mạch Microbit
    else:
        display.show(Image.NO)  # Hiển thị biểu tượng đèn tắt trên màn hình
        pin13.write_digital(0)  # Tắt đèn LED trên mạch Microbit

# Hàm kiểm tra cảm biến chuyển động và bật/tắt đèn
def check_motion_and_control():
    if motion_pin.read_digital() == 1:  # Nếu phát hiện chuyển động
        pin13.write_digital(1)  # Bật đèn LED trên mạch Microbit
    else:
        pin13.write_digital(0)  # Tắt đèn LED trên mạch Microbit

# Hàm kiểm tra cảm biến khói/bụi mịn và cảm biến khí ga và phát cảnh báo
def check_gas_and_smoke_sensor():
    smoke_level = smoke_sensor_pin.read_analog()  # Đọc giá trị từ cảm biến khói/bụi mịn
    gas_level = gas_sensor_pin.read_analog()  # Đọc giá trị từ cảm biến khí ga
    if smoke_level > 512 or gas_level > 512:  # Nếu phát hiện khói/bụi mịn hoặc khí ga
        display.scroll("Nguy hiem co khoi va khi ga!")  # Cuộn thông báo trên màn hình
        speaker_pin.write_digital(1)  # Bật loa
    else:
        speaker_pin.write_digital(0)  # Tắt loa

# Vòng lặp chính
while True:
    adjust_light_based_on_temperature()  # Điều chỉnh ánh sáng dựa trên nhiệt độ
    check_light_and_control()  # Kiểm tra ánh sáng và điều khiển đèn
    check_motion_and_control()  # Kiểm tra chuyển động và điều khiển đèn
    check_gas_and_smoke_sensor()  # Kiểm tra cảm biến khói/bụi mịn và cảm biến khí ga
    sleep(1000)  # Chờ 1 giây trước khi lặp lại
