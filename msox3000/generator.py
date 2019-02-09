from msox3000 import setting


class GeneratorSettings(setting.BaseSettings):

    def add_settings(self):
        base_cmd = ['WGEN']
        # frequency
        self.settings['frequency'] = setting.NumericalSetting(base_cmd + ['FREQ'], 1e6)
        # signal type
        vals = ['SIN', 'SQU', 'RAMP', 'PULE', 'NOISE', 'DC']
        self.settings['function'] = setting.EnumeratedSetting(base_cmd + ['FUNC'], value=vals[1], value_set=vals)
        # voltages
        v_cmd = base_cmd + ['VOLT']
        # high
        self.settings['amp'] = setting.NumericalSetting(v_cmd, value=3.3e0)
        # low
        self.settings['offset'] = setting.NumericalSetting(v_cmd + ['offset'], value=3.3/2)
        # turn on
        self.settings['output'] = setting.EnumeratedSetting(base_cmd + ['OUTP'], value='1', value_set=['0', '1'])

    def reset(self, instrument):
        setting.Setting(['WGEN', 'RST']).write(instrument, check_result=False)
