from msox3000 import setting


ACHANS = 4
DCHANS = 8

class TriggerSettings(setting.BaseSettings):

    def add_settings(self):
        base_cmd = ['TRIG']
        # mode
        vals = ['NORM', 'AUTO']
        self.settings['sweep'] = setting.EnumeratedSetting(base_cmd + ['SWEep'], value=vals[0], value_set=vals)
        # signal type
        vals = ['EDGE', 'GLIT', 'PATT', 'TV', 'DEL', 'EBUR', 'OR', 'RUNT', 'SHOL', 'TRAN', 'SBUS1', 'USB']
        self.settings['function'] = setting.EnumeratedSetting(base_cmd + ['MODE'], value=vals[0], value_set=vals)

        # edge triggering ##############################################################################################
        cmd = base_cmd + ['EDGE']
        # coupling
        vals = ['AC', 'DC', 'LFReject']
        self.settings['e_couping'] = setting.EnumeratedSetting(cmd + ['COUP'], value=vals[1], value_set=vals)
        # trigger level
        self.settings['e_level'] = setting.NumericalSetting(cmd + ['LEV'], value=3.3/2)
        # slope
        vals = ['POS', 'NEG', 'EITH', 'ALT']
        self.settings['e_slop'] = setting.EnumeratedSetting(cmd + ['SLOP'], value=vals[0], value_set=vals)
        # source
        vals = ['CHAN{}'.format(i+1) for i in range(ACHANS)] + ['DIG{}'.format(i) for i in range(DCHANS)]
        vals += ['EXT', 'LINE', 'WGEN']
        self.settings['e_source'] = setting.EnumeratedSetting(cmd + ['SOUR'], value='CHAN1', value_set=vals)

    def reset(self, instrument):
        pass
