# -*- coding: utf-8 -*-

import os
import fnmatch

def all_files(root, patterns='*', single_level=False,yield_folders=False):
      '遍历文件夹目录和文件'
      '''---doc:
        用法：all_files(搜索路径，搜索文件格式用;隔开)
        '''
      patterns = patterns.split(';')

      for path,subdirs,files in os.walk(root):
##            print path
##            print subdirs
##            print files
##            if yield_folders:
##                  files.extend(subdirs)
##            files.sort()

            for name in files:
                  for pattern in patterns:
                        if fnmatch.fnmatch(name,pattern):
                              yield os.path.join(path,name)
                              break
##            if single_level:
##                  break

for path in all_files('e:\\','.docx'):
      print path
