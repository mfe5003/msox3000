import time


class Setting(object):

    def __init__(self, command_str, value=""):
        """Create a setting object that includes methods for setting and writing to a SCPI style regsiter.

        :param command_str: The hierarchical command path as a list ex: ['TRIGger','DELay','ARM','SLOPE']
        :param value: The value that will be sent to the instrument
        """
        self._command_str = command_str
        self._value = value

    def write(self, instrument, check_result=True):
        """Write the current setting value to the instrument.

        :param instrument: An instrument communication object
        :return: True on success, False on error
        """

        instrument._instWrite('{} {}'.format(self.command_str(), self._value))
        if not check_result:
            return True
        # verify the write was successful
        result = self.read(instrument)
        if result == self._value:
            return True
        print('result: {}, expected: {}'.format(result, self._value))
        return False

    def read(self, instrument):
        return instrument._instQuery('{}?'.format(self.command_str()))

    def set_value(self, value):
        self._value = value

    def command_str(self):
        return ':'.join(self._command_str)


class NumericalSetting(Setting):

    def read(self, instrument):
        return float(super(NumericalSetting, self).read(instrument))


class EnumeratedSetting(Setting):

    def __init__(self, command_str, value='', value_set=['']):
        self.check_value(value=value, value_set=value_set)
        super(EnumeratedSetting, self).__init__(command_str, value=value)
        self._value_set = value_set

    def check_value(self, value=None, value_set=None, exception=True):
        if value is None:
            value = self._value
        if value_set is None:
            value_set = self._value_set

        if value not in value_set:
            if exception:
                raise TypeError('The value specified: {}, is not contained in the value set: {}'.format(value, value_set))
            return False
        return True

    def set_value(self, value):
        if self.check_value(value=value):
            super(EnumeratedSetting, self).set_value(value)


class BaseSettings(object):

    def __init__(self):
        self.settings = {}
        self.add_settings()

    def write(self, instrument):
        self.reset(instrument)

        for s in self.settings:
            if not self.settings[s].write(instrument):
                print('An error occurred while setting: {}'.format(self.settings[s].command_str()))
            time.sleep(0.1)

    def add_settings(self):
        """This should be overriden with the default settings"""
        pass

    def reset(self, instrument):
        pass
