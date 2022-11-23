import smbus
import math

bus = smbus.SMBus(1)
MPU = 0x68

acc_x_high = bus.read_byte_data(MPU, 0x3b)
acc_x_low = bus.read_byte_data(MPU, 0x3c)
acc_y_high = bus.read_byte_data(MPU, 0x3d)
acc_y_low = bus.read_byte_data(MPU, 0x3e)
acc_z_high = bus.read_byte_data(MPU, 0x3f)
acc_z_low = bus.read_byte_data(MPU, 0x40)

acc_x = (acc_x_high << 8) + acc_x_low
acc_y = (acc_y_high << 8) + acc_y_low
acc_z = (acc_z_high << 8) + acc_z_low

msg['payload'] = {"accele_x": acc_x, "accele_y": acc_y, "accele_z": acc_z}
msg['topic'] = 'MPU-9250'

return msg