#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 下午6:55
# @Author  : Shikang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url

from UersAnalysis import views

urlpatterns = [
    url(r'^first/$', view=views.Analysis.as_view(
        actions={
            "get": "handle_get",
        }
    ))
]
