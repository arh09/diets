# -*- coding: utf-8 -*-
import requests

from odoo import api, fields, models, _, tools

class FoodComponent(models.Model):
    _name = "component"
    _description = "Food Component"

    name = fields.Text('Name', required=True)

    _sql_constraints = [
        ('name', 'unique (name)', 'That component already exists!')
    ]
