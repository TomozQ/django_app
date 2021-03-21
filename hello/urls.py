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
        path('create', views.create, name='create'),
        path('edit/<int:num>', views.edit, name='edit'),
        path('delete/<int:num>', views.delete, name='delete'),
    ]