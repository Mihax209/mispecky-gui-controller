import serial
import time

from common import retry

class MispeckySerialController():
    def __init__(self):
        self.serial = serial.Serial(
            port='COM7',
            baudrate=115200,
            timeout=0.2
        )
    
    def send_brightness_command(self, value: int) -> bool:
        return self.__send_command('B', value)
    
    def send_effect_command(self, value: int) -> bool:
        return self.__send_command('E', value)

    def send_custom_color_command(self, value: str) -> bool:
        return self.__send_command('C', value)

    @retry(max_retries=20, wait_time=0.05)
    def __send_command(self, command_char: chr, command_value) -> bool:
        command_str = f'{command_char} {command_value}\n'
        print(f"Sending: {command_str}")

        self.serial.write(command_str.encode())
        
        try:
            response = self.serial.readline().decode().strip()

            if not response.startswith('ACK'):
                return False
        except serial.SerialTimeoutException:
            return False

        return True
