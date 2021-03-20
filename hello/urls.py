#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:16:22 2021

@author: furuyatomoki
"""

from django.conf.urls import url
from .views import HelloView

urlpatterns = [
        url(r'', HelloView.as_view(), name='index'),
    ]