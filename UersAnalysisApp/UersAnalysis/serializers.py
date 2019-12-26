#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 下午7:07
# @Author  : Shikang
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers


class UserAnalysisApiView(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "img"]
