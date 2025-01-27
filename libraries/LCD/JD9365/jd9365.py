import utime

#JD9365_800*1280
init_800X1280 = (
0xE0,10,1,0x00,
0xE1,0,1,0x93,
0xE2,0,1,0x65,
0xE3,0,1,0xF8,
0x80,0,1,0x01,#0x03:4lane  0x02:3lane

0xE0,0,1,0x01,
0x00,0,1,0x00,
0x01,0,1,0x44,
0x03,0,1,0x10,
0x04,0,1,0x4B,

0x0C,0,1,0x74,

0x17,0,1,0x00,
0x18,0,1,0xAF,
0x19,0,1,0x00,
0x1A,0,1,0x00,
0x1B,0,1,0xAF,
0x1C,0,1,0x00,

0x35,0,1,0x26,

0x37,0,1,0x09,

0x38,0,1,0x04,
0x39,0,1,0x00,
0x3A,0,1,0x01,
0x3C,0,1,0x78,
0x3D,0,1,0xFF,
0x3E,0,1,0xFF,
0x3F,0,1,0x7F,

0x40,0,1,0x06,
0x41,0,1,0xA0,
0x42,0,1,0x81,
0x43,0,1,0x14,
0x44,0,1,0x23,
0x45,0,1,0x28,

0x55,0,1,0x02,
0x57,0,1,0x69,
0x59,0,1,0x0A,
0x5A,0,1,0x2A,
0x5B,0,1,0x17,

0x5D,0,1,0x7F,
0x5E,0,1,0x6A,
0x5F,0,1,0x5D,
0x60,0,1,0x50,
0x61,0,1,0x4D,
0x62,0,1,0x3E,
0x63,0,1,0x42,
0x64,0,1,0x2C,
0x65,0,1,0x45,
0x66,0,1,0x44,
0x67,0,1,0x44,
0x68,0,1,0x63,
0x69,0,1,0x52,
0x6A,0,1,0x5A,
0x6B,0,1,0x4C,
0x6C,0,1,0x48,
0x6D,0,1,0x3A,
0x6E,0,1,0x27,
0x6F,0,1,0x00,
0x70,0,1,0x7F,
0x71,0,1,0x6A,
0x72,0,1,0x5D,
0x73,0,1,0x50,
0x74,0,1,0x4D,
0x75,0,1,0x3E,
0x76,0,1,0x42,
0x77,0,1,0x2C,
0x78,0,1,0x45,
0x79,0,1,0x44,
0x7A,0,1,0x44,
0x7B,0,1,0x63,
0x7C,0,1,0x52,
0x7D,0,1,0x5A,
0x7E,0,1,0x4C,
0x7F,0,1,0x48,
0x80,0,1,0x3A,
0x81,0,1,0x27,
0x82,0,1,0x00,

0xE0,0,1,0x02,
0x00,0,1,0x02,
0x01,0,1,0x02,
0x02,0,1,0x00,
0x03,0,1,0x00,
0x04,0,1,0x1E,
0x05,0,1,0x1E,
0x06,0,1,0x1F,
0x07,0,1,0x1F,
0x08,0,1,0x1F,
0x09,0,1,0x17,
0x0A,0,1,0x17,
0x0B,0,1,0x37,
0x0C,0,1,0x37,
0x0D,0,1,0x47,
0x0E,0,1,0x47,
0x0F,0,1,0x45,
0x10,0,1,0x45,
0x11,0,1,0x4B,
0x12,0,1,0x4B,
0x13,0,1,0x49,
0x14,0,1,0x49,
0x15,0,1,0x1F,

0x16,0,1,0x01,
0x17,0,1,0x01,
0x18,0,1,0x00,
0x19,0,1,0x00,
0x1A,0,1,0x1E,
0x1B,0,1,0x1E,
0x1C,0,1,0x1F,
0x1D,0,1,0x1F,
0x1E,0,1,0x1F,
0x1F,0,1,0x17,
0x20,0,1,0x17,
0x21,0,1,0x37,
0x22,0,1,0x37,
0x23,0,1,0x46,
0x24,0,1,0x46,
0x25,0,1,0x44,
0x26,0,1,0x44,
0x27,0,1,0x4A,
0x28,0,1,0x4A,
0x29,0,1,0x48,
0x2A,0,1,0x48,
0x2B,0,1,0x1F,

0x2C,0,1,0x01,
0x2D,0,1,0x01,
0x2E,0,1,0x00,
0x2F,0,1,0x00,
0x30,0,1,0x1F,
0x31,0,1,0x1F,
0x32,0,1,0x1E,
0x33,0,1,0x1E,
0x34,0,1,0x1F,
0x35,0,1,0x17,
0x36,0,1,0x17,
0x37,0,1,0x37,
0x38,0,1,0x37,
0x39,0,1,0x08,
0x3A,0,1,0x08,
0x3B,0,1,0x0A,
0x3C,0,1,0x0A,
0x3D,0,1,0x04,
0x3E,0,1,0x04,
0x3F,0,1,0x06,
0x40,0,1,0x06,
0x41,0,1,0x1F,

0x42,0,1,0x02,
0x43,0,1,0x02,
0x44,0,1,0x00,
0x45,0,1,0x00,
0x46,0,1,0x1F,
0x47,0,1,0x1F,
0x48,0,1,0x1E,
0x49,0,1,0x1E,
0x4A,0,1,0x1F,
0x4B,0,1,0x17,
0x4C,0,1,0x17,
0x4D,0,1,0x37,
0x4E,0,1,0x37,
0x4F,0,1,0x09,
0x50,0,1,0x09,
0x51,0,1,0x0B,
0x52,0,1,0x0B,
0x53,0,1,0x05,
0x54,0,1,0x05,
0x55,0,1,0x07,
0x56,0,1,0x07,
0x57,0,1,0x1F,

0x58,0,1,0x40,
0x5B,0,1,0x30,
0x5C,0,1,0x16,
0x5D,0,1,0x34,
0x5E,0,1,0x05,
0x5F,0,1,0x02,
0x63,0,1,0x00,
0x64,0,1,0x6A,
0x67,0,1,0x73,
0x68,0,1,0x1D,
0x69,0,1,0x08,
0x6A,0,1,0x6A,
0x6B,0,1,0x08,

0x6C,0,1,0x00,
0x6D,0,1,0x00,
0x6E,0,1,0x00,
0x6F,0,1,0x88,

0x75,0,1,0xFF,
0x77,0,1,0xDD,
0x78,0,1,0x3F,
0x79,0,1,0x15,
0x7A,0,1,0x17,
0x7D,0,1,0x14,
0x7E,0,1,0x82,

0xE0,0,1,0x04,
0x00,0,1,0x0E,
0x02,0,1,0xB3,
0x09,0,1,0x61,

0x37,0,1,0x58,

0x0E,0,1,0x48,

0xE0,0,1,0x00,

0xE6,0,1,0x02,
0xE7,0,1,0x0C,

0x11,0,1,0x00,

0x29,150,1,0x00,

0x35,50,1,0x00,
)

# 常用颜色定义
red = 0xF800            # 红色
green = 0x07E0          # 绿色
blue = 0x001F           # 蓝色
white = 0xFFFF          # 白色
black = 0x0000          # 黑色
purple = 0xF81F         # 紫色
yellow = 0xffe0         # 黄色
orange = 0xfa20         # 橙色
cyan = 0x867d           # 青色

from machine import LCD
from machine import Pin


def fill(lcd, x_s, y_s, x_e, y_e, color):
    tmp = color.to_bytes(2, 'little')
    count = (x_e - x_s + 1) * (y_e - y_s + 1)

    color_buf = tmp * count

    lcd.lcd_write(color_buf, x_s, y_s, x_e, y_e)


# gpio1 = Pin(Pin.GPIO27, Pin.OUT, Pin.PULL_PU, 1)
gpio2 = Pin(Pin.GPIO8, Pin.OUT, Pin.PULL_PU, 1)
# gpio3 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PU, 1)

mipilcd = LCD()
mipilcd.mipi_init(initbuf=bytearray(init_800X1280), width=800, hight=1280, DataLane=2, VBP=20, VFP=20, HSync=20, VSync=4, HBP=20, HFP=40)
# mipilcd.mipi_init(initbuf=bytearray(init_800X1280), width=800, hight=1280)

def show():
    fill(mipilcd,0,0,800,160,white)
    fill(mipilcd,0,160,800,320,red)
    fill(mipilcd,0,320,800,480,orange)
    fill(mipilcd,0,480,800,640,yellow)
    fill(mipilcd,0,640,800,800,green)
    fill(mipilcd,0,800,800,960,cyan)
    fill(mipilcd,0,960,800,1120,blue)
    fill(mipilcd,0,1120,800,1280,purple)
# mipilcd.lcd_clear(red)

while 1:
    # print("111111111111111")
    mipilcd.lcd_clear(red)
    utime.sleep(2)
    mipilcd.lcd_clear(green)
    utime.sleep(2)
    mipilcd.lcd_clear(yellow)
    utime.sleep(2)
    show()
    utime.sleep(2)

