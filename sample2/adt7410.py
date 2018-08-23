import smbus
from time import sleep

ADDR_ADT7410 = 0x48
REG_TEMPERATURE = 0x00


def get_data_adt7410():
    data = bus.read_i2c_block_data(ADDR_ADT7410, REG_TEMPERATURE, 2)
    temperature = (data[0] << 8 | data[1]) >> 3
    if temperature >= 4096:
        temperature -= 8192
    return temperature*0.0625


if __name__ == "__main__":
    bus = smbus.SMBus(1)

    try:
        while True:
            value = get_data_adt7410()
            print(value)
            sleep(0.5)

    except KeyboardInterrupt:
        pass