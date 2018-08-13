# -*- coding: utf-8 -*-
# @Author  : ly
from flask import Blueprint

main = Blueprint("main", __name__)

from . import views, errors

