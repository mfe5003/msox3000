from msox3000 import setting


class TimebaseSettings(setting.BaseSettings):

    def add_settings(self):
        base_cmd = ['TIM']
        # mode
        vals = ['MAIN', 'WIND', 'XY', 'ROLL']
        self.settings['mode'] = setting.EnumeratedSetting(base_cmd + ['MODE'], value=vals[0], value_set=vals)
        # position
        self.settings['position'] = setting.NumericalSetting(base_cmd + ['POS'], value=0)
        # range
        self.settings['range'] = setting.NumericalSetting(base_cmd + ['RANG'], value=50e-6)
        # reference
        vals = ['LEFT', 'CENT', 'RIGH']
        self.settings['reference'] = setting.EnumeratedSetting(base_cmd + ['REF'], value=vals[0], value_set=vals)

    def reset(self, instrument):
        pass
