from pymodbus.client.sync import ModbusSerialClient
from time import sleep
from pymodbus.client.common import ModbusClientMixin
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
import urllib2

UNIT=0x01
l1=""

client = ModbusSerialClient(
    method='rtu',
    port='/dev/ttyUSB0',
    baudrate=9600,
    timeout=0.3,
    parity='N',
    stopbits=1,
    bytesize=8
)

#WriteRegisterResponse 0 => 28871
finalList =[]
connection=client.connect()
print(connection)
while True:
    str1 = ""
    for i in range(4):
        read=client.read_holding_registers(address=0,count=3,unit=UNIT)
        x=str(read)
        y = x[21:].strip()
        str1 = str1 + y[0]
        str1 = str1+","
        str1 = str1 + y[4:].strip()
        if(i!=3):
            str1 = str1+","
        
    #listTostr=''.join(map(str,finalList))    
        
    sleep(3)
client.close()