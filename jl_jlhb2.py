#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jlhb
活动名称: 锦鲤红包-助力
Author: SheYu09
cron: 7 9 * * * jl_jlhb2.py
new Env('京东 -*- 锦鲤红包')
'''
import os
if os.path.exists('jd_jlhb.py'):
	os.system('rm -rf jd_jlhb.so')
	os.system('mv jd_jlhb.py jd_jlhb.so')
try:
	from jd_jlhb import start
except:
	print('未知错误...')
	exit()

if __name__ == '__main__':
	start()