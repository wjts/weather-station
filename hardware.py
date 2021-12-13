import machine
import ubinascii


def get_chipid():
    return ubinascii.hexlify(machine.unique_id()).decode('utf-8')
