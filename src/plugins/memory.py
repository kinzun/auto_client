import os

from .base import BasePlugins
from lib import convert


class Memory(BasePlugins):

    def win(self, handler, hostname):
        '''
        获取内存信息
        :param handler:
        :param hostname:
        :return:
        '''
        result = handler.cmd('top -l 1 | head -n 10 | grep PhysMem',
                             hostname)
        return result

    def linux(self, handler, hostname):
        if self.debug:
            with open(os.path.join(self.base_dir, 'files/memory.out'), mode='r')as fd:
                output = fd.read()

        else:
            shell_command = "sudo dmidecode  -q -t 17 2>/dev/null"
            output = handler.cmd(shell_command, hostname)

        return self.parse(output)

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        ram_dict = {}
        key_map = {
            'Size': 'capacity',
            'Locator': 'slot',
            'Type': 'model',
            'Speed': 'speed',
            'Manufacturer': 'manufacturer',
            'Serial Number': 'sn',

        }
        devices = content.split('Memory Device')
        for item in devices:
            item = item.strip()
            if not item:
                continue
            if item.startswith('#'):
                continue
            segment = {}
            lines = item.split('\n\t')
            for line in lines:
                if len(line.split(':')) > 1:
                    key, value = line.split(':')
                else:
                    key = line.split(':')[0]
                    value = ""
                if key in key_map:
                    if key == 'Size':
                        segment[key_map['Size']] = convert.convert_mb_to_gb(value, 0)
                    else:
                        segment[key_map[key.strip()]] = value.strip()
            ram_dict[segment['slot']] = segment

        return ram_dict
