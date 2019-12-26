#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 下午6:56
# @Author  : Shikang
# @Site    : 
# @File    : index.py
# @Software: PyCharm
from rest_framework import viewsets, status
from rest_framework.response import Response

from UersAnalysis.models import UserAnalysis
from UersAnalysis.serializers import UserAnalysisApiView


class Analysis(viewsets.ModelViewSet):
    queryset = UserAnalysis
    serializer_class = UserAnalysisApiView

    def handle_get(self, request):
        data = {
            "msg": " 首页　ok",
            "status": status.HTTP_200_OK
        }

        return Response(data)
