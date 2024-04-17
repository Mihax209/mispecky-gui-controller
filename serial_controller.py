import serial
import time

from common import retry

class MispeckySerialController():
    def __init__(self):
        self.serial = serial.Serial(
            port='COM7',
            baudrate=57600,
            timeout=0.2
        )
    
    def send_brightness_command(self, value: int) -> bool:
        return self.__send_command('B', value)
    
    def send_effect_command(self, value: int) -> bool:
        return self.__send_command('E', value)

    @retry(max_retries=10, wait_time=0)
    def __send_command(self, command_char: chr, command_value: int) -> bool:
        command_str = f'{command_char} {command_value}\n'

        self.serial.write(command_str.encode())
        
        try:
            response = self.serial.readline().decode().strip()

            if not response.startswith('ACK'):
                return False
        except serial.SerialTimeoutException:
            return False

        return True
