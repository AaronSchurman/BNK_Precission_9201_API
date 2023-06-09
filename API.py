#############API for operatin the BK Precsion 9201 over PyVisa serial communication ############################################
class PowerSup:
    #function will initailize communication to device with given address
    #an error will be raised if communication is not established
    def __init__(self,address):
        rm = visa.ResourceManager()
        try:
            self.BigK = rm.open_resource(address)
            #check we are connected to the correct device
            name = self.BigK.query("*IDN?")
            #responce should be "B&K Precision, 9201, 602243010727220091,  1.10-1.06"
            if ((str(name[0]) == 'B') & (name[1] == '&')):
                print('Connected to BigK')
            else:
                print('device did not respond with correct name')
                logging.error('device did not respond with correct name')
        except:
            print("Error connecting to device")
            logging.error("Error connecting to device")
    #funcion writes the voltage value given to power supply
    def writeVolt(self,voltage):
        try:
            #writes voltage to power supply
            self.BigK.write('SOUR:VOLT ' + str(voltage))
            #wait one second as to not send commands to quickly
            time.sleep(1)
            #querry for voltage output of power supply. This will be zero no matter what if power supply is off
            actualVolt = self.BigK.query('FETC:VOLT?')
            #if the voltage read is within +/- .1 of the voltage requested it prints voltage written correctly
            if ((float(voltage) < (float(actualVolt) +.1)) & (float(voltage) > (float(actualVolt) - .1))) :
                print('')
            else:
                print('voltage read does not match voltage written or power supply not currently outputting vlotage')
                logging.error('voltage read does not match voltage written or power supply not currently outputting vlotage')
        except Exception as e:
            print('voltage write failed')
            logging.error('voltage write failed')
            print(e)
            
    #funcion writes the current value given to power supply
    def writeCurr(self,current):
        try:
            #writes Current to power supply
            self.BigK.write('SOUR:CURR ' + str(current))
            #wait one second as to not send commands to quickly
            time.sleep(1)
            #querry for current output of power supply. This will be zero no matter what if power supply is off
            actualCURR = self.BigK.query('FETC:CURR?')
            #if the voltage read is within +/- .1 of the voltage requested it prints voltage written correctly
            if ((float(current) < (float(actualCURR) +.1)) & (float(current) > (float(actualCURR) - .1))) :
                print('')
            else:
                print('Current read does not match current written or power supply not currently outputting current.')
                logging.error('Current read does not match current written or power supply not currently outputting current.')
        except  Exception as e:
            print('current write failed')
            logging.error('current write failed')
            print(e)
            
    #function reads current from power supply
    def readCurr(self):
        try:
            current = self.BigK.query('FETC:CURR?')
            return current
        except Exception as e:
            print('current read failed')
            logging.error('current read failed')
            print(e)
            
    #function reads voltage from power supply        
    def readVolt(self):
        try:
            voltage = self.BigK.query('FETC:VOLT?')
            return voltage
        except Exception as e:
            print('voltage read failed')
            logging.error('voltage read failed')
            print(e)
            
    #function will close device
    def close(self):
        try:
            self.BigK.close()
        except Exception as e:
            print('faild to close BK Precision 9201')
            logging.error('faild to close BK Precision 9201')
            print(e)
    
    #function writes to device
    def write(self,com):
        try:
            self.BigK.write(com)
        except Exception as e:
            print('failed to send command to BK Precision 9201')
            logging.error('failed to send command to BK Precision 9201')
            print(e)
