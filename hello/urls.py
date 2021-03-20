#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:16:22 2021

@author: furuyatomoki
"""

from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
    ]